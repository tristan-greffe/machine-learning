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
