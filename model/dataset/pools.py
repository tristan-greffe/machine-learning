import requests

# 1. Fetch pool polygons from OSM Overpass (leisure=swimming_pool) for each zone
# 2. For each pool: download tiles → mosaic centred on the pool
# 3. Convert GPS polygons → pixel bounding boxes
# 4. Crop a 640×640 window with jitter and write labels
def prepare_pools():
    session = requests.Session()

    pass
