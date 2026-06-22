import requests
from model.dataset.config import BUILDING_ZONES, DATASET_DIR
from model.dataset.utils import (
    download_mosaic, polygon_to_pixel_bbox,
    group_touching_polygons, merge_overlapping_boxes,
    iter_windows, boxes_in_window, YoloDatasetWriter,
)


# ============================================================
# Constants / Configuration
# ============================================================

# https://cartes.gouv.fr/rechercher-une-donnee/dataset/IGNF_BD-TOPO
WFS_URL = (
    "https://data.geopf.fr/wfs/ows"
    "?SERVICE=WFS&VERSION=2.0.0&REQUEST=GetFeature"
    "&TYPENAMES=BDTOPO_V3:batiment"
    "&OUTPUTFORMAT=application/json"
    "&COUNT=5000"
    "&SRSNAME=EPSG:4326"
    "&BBOX={west},{south},{east},{north},EPSG:4326"
)


# ============================================================
# Utility Functions
# ============================================================

# Fetch building polygons from BD TOPO WFS for the given bounds (north, west, south, east)
def fetch_building_polygons(bounds, session):
    north, west, south, east = bounds
    url = WFS_URL.format(north=north, west=west, south=south, east=east)
    response = session.get(url, timeout=40)
    response.raise_for_status()
    return response.json().get("features", [])


# ============================================================
# Main
# ============================================================

# 1. Download tiles → mosaic covering the zone → bounds
# 2. Fetch building polygons from BD TOPO WFS (BDTOPO_V3:batiment) for those bounds
# 3. Convert GPS polygons → pixel bounding boxes
# 4. Slide 640×640 windows over the mosaic and write labels
def prepare_buildings():
    session = requests.Session()
    dataset_writer = YoloDatasetWriter(DATASET_DIR / "buildings", ["building"])

    for name, (latitude, longitude, grid) in BUILDING_ZONES.items():
        print(f"  zone {name} ({latitude}, {longitude}) grid={grid}")

        # Step 1: download tiles → mosaic + bounds
        result = download_mosaic(latitude, longitude, grid, session)
        if result is None:
            print(f"  tiles unavailable, skipping")
            continue
        mosaic, bounds = result
        print(f"  mosaic {mosaic.size[0]}×{mosaic.size[1]} px")

        # Step 2: fetch building polygons for those bounds
        features = fetch_building_polygons(bounds, session)
        print(f"  {len(features)} features")

        # Step 3: convert GPS polygons → pixel bounding boxes
        image_width, image_height = mosaic.size
        all_rings = []
        for feature in features:
            geometry = feature.get("geometry", {})
            geometry_type = geometry.get("type", "")
            coordinates = geometry.get("coordinates", [])
            if geometry_type == "Polygon":
                raw_rings = [coordinates[0]] if coordinates else []
            elif geometry_type == "MultiPolygon":
                raw_rings = [polygon[0] for polygon in coordinates if polygon]
            else:
                continue
            for ring in raw_rings:
                points = [(c[0], c[1]) for c in ring]
                if len(points) >= 3:
                    all_rings.append(points)

        groups = group_touching_polygons(all_rings)
        boxes = []
        for group_indices in groups:
            all_points = [point for index in group_indices for point in all_rings[index]]
            x0, y0, x1, y1 = polygon_to_pixel_bbox(all_points, bounds, image_width, image_height)
            boxes.append((0, x0, y0, x1, y1))
        boxes = merge_overlapping_boxes(boxes)
        print(f"  {len(boxes)} bounding boxes after grouping/merging")

        # Step 4: slide 640×640 windows over the mosaic and write labels
        windows_before = len(dataset_writer)
        for window_x, window_y in iter_windows(image_width, image_height):
            crop = mosaic.crop((window_x, window_y,
                                window_x + 640, window_y + 640))
            label_lines = boxes_in_window(boxes, window_x, window_y)
            dataset_writer.add(crop, label_lines)
        print(f"  +{len(dataset_writer) - windows_before} windows")

    print(f"\n{len(dataset_writer)} images / {dataset_writer.number_of_boxes()} boxes → {DATASET_DIR / 'buildings'}")
