import io
import math
import time
from pathlib import Path
from PIL import Image

# ============================================================
# Constants
# ============================================================

# https://cartes.gouv.fr/aide/fr/guides-utilisateur/utiliser-les-services-de-la-geoplateforme/diffusion/wmts/
WMTS_URL = (
    "https://data.geopf.fr/wmts?"
    "SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0"
    "&LAYER=ORTHOIMAGERY.ORTHOPHOTOS"
    "&STYLE=normal&TILEMATRIXSET=PM"
    "&TILEMATRIX={z}&TILEROW={y}&TILECOL={x}"
    "&FORMAT=image/jpeg"
)
TILE_SIZE_PIXELS = 256
ZOOM = 19

# On-disk cache: avoids re-downloading tiles shared across nearby windows
_CACHE_DIR = Path(__file__).parent / "_tilecache"


# ============================================================
# Tile math
# ============================================================

# Convert (latitude, longitude) to (tile_x, tile_y) at the given zoom level
def latitude_longitude_to_tile(latitude, longitude, zoom):
    n = 2 ** zoom
    tile_x = int((longitude + 180) / 360 * n)
    latitude_radians = math.radians(latitude)
    tile_y = int((1 - math.log(math.tan(latitude_radians) + 1 / math.cos(latitude_radians)) / math.pi) / 2 * n)
    return tile_x, tile_y


# Convert (tile_x, tile_y) to the (latitude, longitude) of the tile's top-left corner
def tile_to_latitude_longitude(tile_x, tile_y, zoom):
    n = 2 ** zoom
    longitude = tile_x / n * 360 - 180
    latitude_radians = math.atan(math.sinh(math.pi * (1 - 2 * tile_y / n)))
    latitude = math.degrees(latitude_radians)
    return latitude, longitude


# ============================================================
# Tile download
# ============================================================

# Download a single WMTS tile; use disk cache when available.
# Returns a PIL RGB image, or None if the tile is unavailable.
def download_tile(tile_x, tile_y, zoom, session, retries=3):
    cache_path = _CACHE_DIR / f"{zoom}_{tile_x}_{tile_y}.jpg"
    if cache_path.exists():
        try:
            return Image.open(cache_path).convert("RGB")
        except Exception:
            pass  # corrupt cache entry — refetch

    url = WMTS_URL.format(x=tile_x, y=tile_y, z=zoom)
    for attempt in range(retries):
        try:
            response = session.get(url, timeout=15)
            if response.status_code == 200:
                _CACHE_DIR.mkdir(parents=True, exist_ok=True)
                cache_path.write_bytes(response.content)
                return Image.open(io.BytesIO(response.content)).convert("RGB")
            if response.status_code == 404:
                return None
        except Exception:
            pass
        time.sleep(1 + attempt)
    return None


# Assemble a grid×grid mosaic of IGN WMTS tiles centred on (latitude, longitude).
# Returns (PIL image, bounds) where bounds = (north, west, south, east),
# or None if any tile fails to download.
def download_mosaic(latitude, longitude, grid, session):
    centre_tile_x, centre_tile_y = latitude_longitude_to_tile(latitude, longitude, ZOOM)

    # Top-left tile of the grid
    half_grid = grid // 2
    top_left_x = centre_tile_x - half_grid
    top_left_y = centre_tile_y - half_grid

    mosaic = Image.new("RGB", (TILE_SIZE_PIXELS * grid, TILE_SIZE_PIXELS * grid))
    for row in range(grid):
        for col in range(grid):
            tile = download_tile(top_left_x + col, top_left_y + row, ZOOM, session)
            if tile is None:
                return None
            mosaic.paste(tile, (col * TILE_SIZE_PIXELS, row * TILE_SIZE_PIXELS))

    north, west = tile_to_latitude_longitude(top_left_x, top_left_y, ZOOM)
    south, east = tile_to_latitude_longitude(top_left_x + grid, top_left_y + grid, ZOOM)
    return mosaic, (north, west, south, east)


# ============================================================
# GPS → pixel conversion
# ============================================================

# Convert a (longitude, latitude) GPS point to (pixel_x, pixel_y) within the mosaic
def longitude_latitude_to_pixel(longitude, latitude, bounds, image_width, image_height):
    north, west, south, east = bounds
    pixel_x = (longitude - west)  / (east - west)  * image_width
    pixel_y = (north - latitude) / (north - south) * image_height
    return pixel_x, pixel_y


# Convert a GPS polygon ring [(lon, lat), ...] to a pixel bounding box (x0, y0, x1, y1)
def polygon_to_pixel_bbox(polygon_points_lon_lat, bounds, image_width, image_height):
    pixel_xs, pixel_ys = [], []
    for longitude, latitude in polygon_points_lon_lat:
        pixel_x, pixel_y = longitude_latitude_to_pixel(longitude, latitude, bounds, image_width, image_height)
        pixel_xs.append(pixel_x)
        pixel_ys.append(pixel_y)
    return min(pixel_xs), min(pixel_ys), max(pixel_xs), max(pixel_ys)


# Group polygon rings that share at least one GPS vertex (within tolerance degrees).
# BD TOPO splits large buildings into multiple features with shared edge vertices —
# this clusters them so each building gets a single bounding box.
# Returns a list of lists of ring indices, one group per connected component.
def group_touching_polygons(rings, tolerance=1e-5):
    number_of_rings = len(rings)
    if number_of_rings == 0:
        return []

    def snap(vertex):
        return (round(vertex[0] / tolerance) * tolerance,
                round(vertex[1] / tolerance) * tolerance)

    snapped = [frozenset(snap(vertex) for vertex in ring) for ring in rings]
    parent = list(range(number_of_rings))

    def find(index):
        while parent[index] != index:
            parent[index] = parent[parent[index]]
            index = parent[index]
        return index

    def union(a, b):
        a, b = find(a), find(b)
        if a != b:
            parent[b] = a

    for i in range(number_of_rings):
        for j in range(i + 1, number_of_rings):
            if snapped[i] & snapped[j]:
                union(i, j)

    groups = {}
    for i in range(number_of_rings):
        root = find(i)
        groups.setdefault(root, []).append(i)
    return list(groups.values())


# Merge pixel bounding boxes whose intersection covers at least minimum_overlap
# of the smaller box area. Adjacent boxes (touching edges, zero intersection) are NOT merged.
# boxes: list of (class_id, x0, y0, x1, y1). Returns the same format with fewer entries.
def merge_overlapping_boxes(boxes, minimum_overlap=0.1):
    changed = True
    while changed:
        changed = False
        used = [False] * len(boxes)
        result = []
        for i in range(len(boxes)):
            if used[i]:
                continue
            class_id, x0, y0, x1, y1 = boxes[i]
            for j in range(i + 1, len(boxes)):
                if used[j]:
                    continue
                _, x0j, y0j, x1j, y1j = boxes[j]
                intersection_x0, intersection_y0 = max(x0, x0j), max(y0, y0j)
                intersection_x1, intersection_y1 = min(x1, x1j), min(y1, y1j)
                if intersection_x0 >= intersection_x1 or intersection_y0 >= intersection_y1:
                    continue
                intersection_area = (intersection_x1 - intersection_x0) * (intersection_y1 - intersection_y0)
                area_i = (x1 - x0) * (y1 - y0)
                area_j = (x1j - x0j) * (y1j - y0j)
                if intersection_area / max(min(area_i, area_j), 1) >= minimum_overlap:
                    x0, y0 = min(x0, x0j), min(y0, y0j)
                    x1, y1 = max(x1, x1j), max(y1, y1j)
                    used[j] = True
                    changed = True
            result.append((class_id, x0, y0, x1, y1))
            used[i] = True
        boxes = result
    return boxes
