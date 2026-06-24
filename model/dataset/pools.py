import math
import random
import time
import requests
from model.dataset.config import POOL_ZONES, DATASET_DIR
from model.dataset.utils import (
    download_mosaic, polygon_to_pixel_bbox, longitude_latitude_to_pixel,
    boxes_in_window, YoloDatasetWriter, WINDOW_SIZE,
)

# ============================================================
# Constants / Configuration
# ============================================================

# https://wiki.openstreetmap.org/wiki/Overpass_API
OVERPASS_URL = "https://overpass-api.de/api/interpreter"
# 4×4 tiles = 1024px mosaic — enough room to crop a 640×640 window with jitter
POOL_GRID = 4
# Maximum pool-centred windows saved per zone (avoids over-representing large zones)
POOL_MAXIMUM_WINDOWS_PER_ZONE = 200
# Jitter range in pixels applied to the window centre (improves position invariance)
JITTER_RANGE = 120
# Only keep pools whose bounding dimension falls in [MIN, MAX] metres
POOL_MINIMUM_SIZE_METERS = 1.5
POOL_MAXIMUM_SIZE_METERS = 35.0


# ============================================================
# Utility Functions
# ============================================================

# Fetch pool polygons from OSM Overpass for the given bounds (north, west, south, east).
# Retries on 5xx errors (Overpass returns 504 when overloaded) with a growing delay.
def fetch_pool_polygons(bounds, session, retries=3):
    north, west, south, east = bounds
    query = (
        f"[out:json][timeout:90];"
        f"(way[leisure=swimming_pool]({south},{west},{north},{east});"
        f" relation[leisure=swimming_pool]({south},{west},{north},{east}););"
        f"out geom;"
    )
    # User-Agent required — server returns HTTP 406 without it
    headers = {"User-Agent": "geo-ml/1.0 (research)"}
    for attempt in range(retries):
        response = session.get(OVERPASS_URL, params={"data": query},
                               headers=headers, timeout=100)
        if response.status_code == 200:
            return response.json().get("elements", [])
        if response.status_code < 500:
            response.raise_for_status()  # 4xx — no point retrying
        if attempt < retries - 1:
            wait = 60 * (attempt + 1)
            print(f" retry in {wait}s (HTTP {response.status_code})", flush=True)
            time.sleep(wait)
    response.raise_for_status()
    return []


# Return the max bounding dimension of a pool element in metres
def pool_size_in_meters(element):
    geometry = element.get("geometry", [])
    if len(geometry) < 2:
        return 0
    latitudes  = [p["lat"] for p in geometry]
    longitudes = [p["lon"] for p in geometry]
    delta_lat  = (max(latitudes)  - min(latitudes))  * 111_000
    delta_lon  = (max(longitudes) - min(longitudes)) * 111_000 * math.cos(math.radians(latitudes[0]))
    return max(delta_lat, delta_lon)


# ============================================================
# Main
# ============================================================

# 1. Compute zone bounds from (latitude, longitude, half_extent_deg)
# 2. Fetch pool polygons from OSM Overpass (leisure=swimming_pool) for those bounds
# 3. For each pool: download mosaic centred on that pool
# 4. Crop a 640×640 window with jitter, label ALL visible pools, write to dataset
def prepare_pools():
    session = requests.Session()
    rng = random.Random(42)
    dataset_writer = YoloDatasetWriter(DATASET_DIR / "pools", ["pool"])

    for name, (latitude, longitude, half) in POOL_ZONES.items():
        print(f"  {name:<24} ...", end="\r", flush=True)

        # Step 1: compute zone bounds from half_extent_deg
        zone_bounds = (latitude + half, longitude - half, latitude - half, longitude + half)

        # Step 2: fetch pool polygons for those bounds
        all_elements = fetch_pool_polygons(zone_bounds, session)
        # Filter by physical size to remove noise (tags on points, huge areas, etc.)
        valid_pools = [
            element for element in all_elements
            if POOL_MINIMUM_SIZE_METERS < pool_size_in_meters(element) < POOL_MAXIMUM_SIZE_METERS
            and len(element.get("geometry", [])) >= 3
        ]
        if not valid_pools:
            print(f"  {name:<24} ✗ no valid pools ({len(all_elements)} OSM elements)")
            continue

        # Shuffle and cap: iterate over at most POOL_MAXIMUM_WINDOWS_PER_ZONE pool centres
        pool_centres = list(valid_pools)
        rng.shuffle(pool_centres)
        pool_centres = pool_centres[:POOL_MAXIMUM_WINDOWS_PER_ZONE]

        windows_before = len(dataset_writer)
        for element in pool_centres:
            geometry_points = element.get("geometry", [])
            pool_latitude  = sum(p["lat"] for p in geometry_points) / len(geometry_points)
            pool_longitude = sum(p["lon"] for p in geometry_points) / len(geometry_points)

            # Step 3: download mosaic centred on this pool
            pool_result = download_mosaic(pool_latitude, pool_longitude, POOL_GRID, session)
            if pool_result is None:
                continue
            pool_mosaic, pool_bounds = pool_result
            image_width, image_height = pool_mosaic.size

            # Compute pixel bboxes for ALL valid pools in this mosaic
            # (avoids teaching false negatives when other pools appear in the window)
            all_boxes = []
            for pool_element in valid_pools:
                polygon_lon_lat = [(p["lon"], p["lat"]) for p in pool_element.get("geometry", [])]
                if len(polygon_lon_lat) < 3:
                    continue
                x0, y0, x1, y1 = polygon_to_pixel_bbox(polygon_lon_lat, pool_bounds, image_width, image_height)
                all_boxes.append((0, x0, y0, x1, y1))

            # Centre of the current pool in pixels
            pool_center_x, pool_center_y = longitude_latitude_to_pixel(
                pool_longitude, pool_latitude, pool_bounds, image_width, image_height)

            # Step 4: crop 640×640 window with jitter, clamped to mosaic, and write labels
            jitter_x = rng.randint(-JITTER_RANGE, JITTER_RANGE)
            jitter_y = rng.randint(-JITTER_RANGE, JITTER_RANGE)
            window_x = max(0, min(int(pool_center_x - WINDOW_SIZE / 2 + jitter_x), image_width  - WINDOW_SIZE))
            window_y = max(0, min(int(pool_center_y - WINDOW_SIZE / 2 + jitter_y), image_height - WINDOW_SIZE))

            crop = pool_mosaic.crop((window_x, window_y,
                                     window_x + WINDOW_SIZE, window_y + WINDOW_SIZE))
            label_lines = boxes_in_window(all_boxes, window_x, window_y)
            if not label_lines:
                continue  # pool slipped outside window after jitter — skip
            dataset_writer.add(crop, label_lines)

        windows_added = len(dataset_writer) - windows_before
        print(f"  {name:<24} {len(all_elements):>4} OSM → {len(valid_pools):>4} valid  +{windows_added} win")

    print(f"  {'total':<24} {len(dataset_writer)} images · {dataset_writer.number_of_boxes()} boxes\n")
