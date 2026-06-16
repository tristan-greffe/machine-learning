import requests

# 1. Fetch building polygons from BD TOPO WFS (BDTOPO_V3:batiment) for each zone
# 2. Download tiles → mosaic covering the zone
# 3. Convert GPS polygons → pixel bounding boxes
# 4. Slide 640×640 windows over the mosaic and write labels
def prepare_buildings():
    session = requests.Session()
    pass
