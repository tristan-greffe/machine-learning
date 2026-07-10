# Training - `model/train.py`

`model/train.py` is the single entry point for training a model and exporting the weights to `.onnx`. It orchestrates three steps: argument parsing, YOLOv8 training, and ONNX export to the frontend.

```bash
python model/train.py --model buildings
python model/train.py --model pools
```

<img src="/guide/train_flow.png" style="display:block;margin:1.5rem auto;width:100%;height:auto;">

## Arguments

| Argument | Default | Description |
| --- | --- | --- |
| `--model` | *(required)* | Dataset to train on: `buildings` or `pools` |
| `--epochs` | `80` | Number of full passes over the dataset |
| `--batch` | `16` | Number of images per iteration |
| `--patience` | `20` | Early stopping: halts if mAP does not improve for N epochs |
| `--base` | `yolov8n.pt` | Starting checkpoint for fine-tuning |
| `--resume` | `False` | Resume from `model/runs/<model>/weights/last.pt` |
| `--no-export` | `False` | Skip ONNX export after training |

:::tip Best quality config
```bash
python model/train.py --model buildings --base yolov8s.pt --epochs 150 --batch 32 --patience 40
```
`yolov8s` is more accurate than `yolov8n` (~22 MB ONNX vs ~6 MB) but still loadable in the browser.
:::

## Script structure

The script is split into three independent functions, corresponding to the three steps in the diagram above.

### 1. `parse_arguments()`

Declares and parses the CLI arguments, then returns the `args` object.

### 2. `run_training(args)`

Runs YOLOv8 training and returns the path to `best.pt`.

1. **Checks that the dataset exists** (`model/dataset/<model>/dataset.yaml`). If not, prints the command to generate it and exits.
2. **Loads the base checkpoint** (`args.base`), or resumes from `last.pt` if `--resume` is passed.
3. **Calls `model.train(...)`** with augmentations tuned for IGN orthophotos.
4. **Copies `best.pt`** to `model/weights/<model>.pt`.

**Configured augmentations:**

```python
# Aerial imagery has no canonical orientation - full rotation and both flips are valid
fliplr=0.5, flipud=0.5, degrees=180,
# Mild colour jitter to handle IGN sensor variability across acquisition zones
hsv_h=0.015, hsv_s=0.5, hsv_v=0.4,
mosaic=1.0,
```

:::info Why these augmentations?
Orthophotos have **no canonical orientation** - there is no "up" the way a landscape photo has one. Full rotation (`degrees=180`) and flips in both directions are therefore valid: they multiply training examples without introducing inconsistency.

Hue variation (`hsv_*`) compensates for **sensor calibration differences** between IGN acquisition zones, which are not all photographed under the same conditions.
:::

### 3. `export_onnx(model_name, best_checkpoint)`

Exports `best.pt` to `.onnx` and copies it to `frontend/public/models/`.

```python
model.export(
    format="onnx",
    imgsz=640,
    opset=12,      # last version broadly supported by onnxruntime-web
    simplify=True, # simplify the graph (onnxslim)
    nms=False,     # NMS is handled in JS, not embedded in the graph
    dynamic=False, # fixed input shape - required by onnxruntime-web
)
```

:::tip Why `nms=False`?
The **NMS** operation (duplicate box suppression, see [YOLO](./yolo.md)) is poorly supported by ONNX Runtime Web. We **exclude it from the graph** and reimplement it in JavaScript. The `.onnx` then returns only raw boxes in `[1, 5, 8400]` format; the browser filters by score and deduplicates.
:::

:::tip Why `opset=12`?
The **opset** is the version of the ONNX operations vocabulary. A too-recent opset may contain operations the browser runtime does not recognise. `opset=12` is the last version broadly supported by ONNX Runtime Web.
:::

:::tip Why `dynamic=False`?
ONNX Runtime Web requires a **fixed input shape** to initialise its WASM session. We fix it to `640×640`, exactly the same as `IMAGE_SIZE` in the dataset, ensuring consistency between training and inference.
:::

## Output files

At the end of execution, the script writes two families of files: PyTorch weights (for resuming or re-exporting) and the ONNX model (for the frontend).

```
model/
├── runs/<model>/weights/
│   ├── best.pt      ← best checkpoint (saved automatically)
│   └── last.pt      ← last checkpoint (useful for --resume)
└── weights/
    └── <model>.pt   ← copy of best.pt (stable access point)

frontend/public/models/
└── <model>.onnx     ← served with the SPA, loaded by ONNX Runtime Web
```
