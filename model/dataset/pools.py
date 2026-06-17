import requests

# ============================================================
# Constants / Configuration
# ============================================================

# https://wiki.openstreetmap.org/wiki/Overpass_API
OVERPASS_URL = "https://overpass-api.de/api/interpreter"


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

# 1. Download tiles → mosaic centred on the zone → bounds
# 2. Fetch pool polygons from OSM Overpass (leisure=swimming_pool) for those bounds
# 3. Convert GPS polygons → pixel bounding boxes
# 4. Crop a 640×640 window with jitter and write labels
def prepare_pools():
    session = requests.Session()
    pass
