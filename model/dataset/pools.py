import requests
from model.dataset.config import POOL_ZONES
from model.dataset.utils import download_mosaic, polygon_to_pixel_bbox

# ============================================================
# Constants / Configuration
# ============================================================

# https://wiki.openstreetmap.org/wiki/Overpass_API
OVERPASS_URL = "https://overpass-api.de/api/interpreter"
# 4×4 tiles = 1024px mosaic — enough room to crop a 640×640 window with jitter
POOL_GRID = 4


# ============================================================
# Utility Functions
# ============================================================

# Fetch pool polygons from OSM Overpass for the given bounds (north, west, south, east)
def fetch_pool_polygons(bounds, session):
    north, west, south, east = bounds
    query = (
        f"[out:json][timeout:90];"
        f"(way[leisure=swimming_pool]({south},{west},{north},{east});"
        f" relation[leisure=swimming_pool]({south},{west},{north},{east}););"
        f"out geom;"
    )
    # User-Agent required - server returns HTTP 406 without it
    response = session.get(OVERPASS_URL, params={"data": query}, headers={"User-Agent": "geo-ml/1.0 (research)"}, timeout=100)
    response.raise_for_status()
    return response.json().get("elements", [])


# ============================================================
# Main
# ============================================================

# 1. Compute zone bounds from (latitude, longitude, half_extent_deg)
# 2. Fetch pool polygons from OSM Overpass (leisure=swimming_pool) for those bounds
# 3. For each pool: download mosaic centred on that pool
# 4. Crop a 640×640 window with jitter and write labels
def prepare_pools():
    session = requests.Session()
    for name, (latitude, longitude, half) in POOL_ZONES.items():
        print(f"  zone {name} ({latitude}, {longitude}) half={half}°")

        # Step 1: compute zone bounds from half_extent_deg
        bounds = (latitude + half, longitude - half, latitude - half, longitude + half)

        # Step 2: fetch pool polygons for those bounds
        elements = fetch_pool_polygons(bounds, session)
        print(f"  {len(elements)} pools")

        # Step 3: for each pool → download mosaic centred on that pool + pixel bbox
        for element in elements:
            geometry_points = element.get("geometry", [])
            if len(geometry_points) < 3:
                continue
            pool_latitude = sum(p["lat"] for p in geometry_points) / len(geometry_points)
            pool_longitude = sum(p["lon"] for p in geometry_points) / len(geometry_points)

            pool_result = download_mosaic(pool_latitude, pool_longitude, POOL_GRID, session)
            if pool_result is None:
                continue
            pool_mosaic, pool_bounds = pool_result
            image_width, image_height = pool_mosaic.size

            polygon_lon_lat = [(p["lon"], p["lat"]) for p in geometry_points]
            x0, y0, x1, y1 = polygon_to_pixel_bbox(polygon_lon_lat, pool_bounds, image_width, image_height)
            pool_box = (0, x0, y0, x1, y1)

            # Step 4: crop 640×640 window with jitter and write labels
