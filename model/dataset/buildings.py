import requests
from model.dataset.config import BUILDING_ZONES
from model.dataset.utils import download_mosaic


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
        # Step 4: slide 640×640 windows over the mosaic and write labels
