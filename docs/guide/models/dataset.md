# Dataset

In **geo-ml**, there is **no manual annotation**. That is the core principle of the project: labels already exist as free, open vector data covering all of France. Building polygons come from **BD TOPO IGN**, pool polygons from **OpenStreetMap**.

The pipeline's role is purely mechanical: download IGN satellite tiles, assemble mosaics, convert GPS polygons into pixel bounding boxes, then slice everything into 640×640 windows in the format expected by YOLO.

:::tip No manual annotation
Labels cover all of France. We download, convert, train - without ever drawing a box by hand.
:::

## Label sources

| Object | Source | Layer / tag |
| --- | --- | --- |
| **Buildings** | [BD TOPO IGN](https://geoservices.ign.fr/bdtopo) | `BDTOPO_V3:batiment` |
| **Pools** | [OpenStreetMap](https://www.openstreetmap.org/) | `leisure=swimming_pool` |

Both sources return **GPS polygons** (GeoJSON) that the pipeline converts into pixel bounding boxes.

## YOLO format

YOLOv8 expects a dataset structured around a `dataset.yaml` configuration file that describes paths and class names. See the [official Ultralytics format](https://docs.ultralytics.com/datasets/detect#supported-dataset-formats).

```
model/dataset/<model>/
├── dataset.yaml          ← paths + class names
├── images/
│   ├── train/  *.jpg     ← 640×640 windows (80 %)
│   └── val/    *.jpg     ← 640×640 windows (20 %)
└── labels/
    ├── train/  *.txt     ← one line per object
    └── val/    *.txt
```

:::tip `train/` vs `val/`
The dataset is split **80 % / 20 %** at write time:

- **`train/`**: images the model sees during training. It computes its errors on them and updates its weights at each pass.
- **`val/`**: images the model **never sees** during training. They are used solely to measure real quality at the end of each epoch.
If performance on `val` degrades while `train` keeps improving, this signals **overfitting**.
:::

### Label file structure

Each image `images/train/000042.jpg` has an associated file `labels/train/000042.txt`. Each line in the `.txt` describes **one object**:

```
0  0.666  0.655  0.156  0.181
↑    ↑      ↑      ↑      ↑
class  cx    cy     w      h    (all normalised to [0.0, 1.0])
```

:::tip Field details
- **`class`**: class identifier (`0` = building or pool depending on the model). A single integer.
- **`cx`, `cy`**: coordinates of the **centre** of the box, normalised between `0.0` and `1.0` (`0` = left/top edge, `1` = right/bottom edge).
- **`w`, `h`**: **width** and **height** of the box, normalised the same way.
All values are relative to the 640×640 image - no absolute pixels.
:::

```yaml
# dataset.yaml (auto-generated)
path: /abs/path/to/model/dataset/buildings
train: images/train
val:   images/val
names:
  0: building
```

## Pipeline overview

The pipeline starts from two distinct data sources - one vector (annotations), one raster (imagery) - that converge to produce the final dataset.

<img src="/guide/dataset_pipeline_overview.png" style="display:block;margin:1.5rem auto;width:100%;height:auto;">

**1. Fetching annotations (vector source)**
- Download GPS polygons from open data: **BD TOPO** (via WFS) and **OpenStreetMap** (via Overpass).
- These polygons delimit the objects to detect (pools, buildings).

**2. Fetching imagery (raster source)**
- Download **256×256 px** tiles from **IGN WMTS** (`data.geopf.fr`) at zoom 19 (~20 cm/px).
- Disk-cached in `model/dataset/_tilecache/` to avoid re-downloading the same tiles.

**3. Assembling the mosaic**
- Stitch **4×4 tiles** into a **1024×1024 px mosaic** (~200 m × 200 m on the ground) at native resolution.

**4. Coordinate conversion**
- GPS polygons are projected onto the mosaic: **GPS → pixel** conversion, producing **bounding boxes** expressed in pixels.

**5. Window slicing**
- The mosaic is sliced into **640×640 px windows** (YOLO's input size), using a slicing strategy specific to each model.

**6. Final dataset generation**
- Each window produces an image + annotation pair, split between training and validation:
  - `images/train/` and `images/val/` → `*.jpg` images
  - `labels/train/` and `labels/val/` → `*.txt` annotations (YOLO format)

### Why assemble a mosaic?

A raw IGN tile is 256×256 px - too small for a 640×640 YOLO window. Upscaling blurs the image and defeats the purpose of using high-resolution IGN imagery. By assembling 4×4 tiles, we get a 1024×1024 px mosaic at native resolution from which we can cut multiple 640×640 windows. It is also exactly the same scale as at inference time, ensuring the model sees the same resolution during training and in production.

<img src="/guide/mosaique.png" style="display:block;margin:1.5rem auto;width:100%;height:auto;">

## Two strategies by density

Buildings and pools are distributed very differently. The pipeline adapts its slicing strategy to each object type.

### Buildings - sliding window on a grid

Buildings are **dense and uniformly distributed**. For each zone, we assemble a large mosaic then **slide a 640×640 window with 25% overlap** across the entire surface, ensuring exhaustive coverage without cutting objects at the edges.

<img src="/guide/dataset_batiments.png" style="display:block;margin:1.5rem auto;width:100%;height:auto;">

**Steps per zone:**

1. Download IGN tiles → assemble the mosaic.
2. Query **BD TOPO WFS** for building polygons in the zone.
3. Convert GPS polygons → pixel bboxes on the mosaic.
4. Slide the 640×640 window → write image + YOLO labels.

### Pools - object-centred window with jitter

Pools are **rare and scattered**: grid slicing would mostly produce empty images. Instead, for **each pool**, we download a mosaic centred on it, then cut a window with a random offset (**jitter ±120 px**) to improve position invariance.

<img src="/guide/dataset_piscines.png" style="display:block;margin:1.5rem auto;width:100%;height:auto;">

**Steps per zone:**

1. Query **OSM Overpass** → `leisure=swimming_pool` polygons.
2. Filter out out-of-range pools (`< 1.5 m` or `> 35 m`).
3. For each pool: download a centred mosaic.
4. Cut a 640×640 window with jitter → label **all** visible pools → write.

:::warning Label every pool in the window
If a window contains 3 pools but only one is marked, we teach the model that the other 2 are background → **false negatives**. The script therefore labels **all** pools present in the window, not just the one used for centring.
:::

## Download the dataset

```bash
conda activate geoml

python -m model.dataset.main              # buildings + pools (default)
python -m model.dataset.main --buildings  # buildings only
python -m model.dataset.main --pools      # pools only
```

| Argument | Description |
| --- | --- |
| *(none)* | Generates both datasets (buildings + pools) |
| `--buildings` | Generates only the buildings dataset (BD TOPO WFS) |
| `--pools` | Generates only the pools dataset (OSM Overpass) |

:::info Dataset imprecision
BD TOPO and OSM polygons are not always **perfectly aligned** with the IGN orthophoto - a 1–2 m offset is common. Bounding boxes may therefore be slightly shifted from the real object. YOLO tolerates this label noise well, but it is the main source of dataset imprecision.
:::
