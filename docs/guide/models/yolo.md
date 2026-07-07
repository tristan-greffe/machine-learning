# YOLO

In geo-ml, rather than training a model from scratch (which would require millions of images), we start from a **YOLOv8 model already trained** on a large general-purpose dataset - it already knows how to recognise shapes, edges, and textures. We then **specialise it for our task** (*fine-tuning*): we continue its training on our two classes, **pools** & **buildings**, using a small set of IGN images. The model reuses what it already knows and just learns to recognise our specific objects.

:::info
**[YOLO](https://arxiv.org/abs/2208.00773)** (*You Only Look Once*) is a family of **object-detection** models: given an image, they return a list of **bounding boxes**, each with a **class** and a **confidence score**. It's the model at the heart of this project.
:::

## [How it works](https://blent.ai/blog/a/detection-images-yolo-tensorflow)

<img src="/guide/yolo_vs_faster.png" style="display:block;margin:1.5rem auto;width:100%;height:auto;">

### 🔹 Before YOLO: two stages, two networks (e.g. [Faster R-CNN](https://arxiv.org/abs/1506.01497))
The detector passes the image through the network **multiple times**:

1. **Propose** hundreds of regions that might contain an object.
2. **Classify** each region *one by one* by re-running it through a CNN.

=> Many repeated computations: **accurate, but slow**.

### 🔹 [YOLO does everything in **a single pass**](https://medium.com/@fatimazahra.belharar/object-detection-using-cnn-an-introduction-to-the-yolo-algorithm-df0f7b173c6)
The image traverses the network **once** and everything is predicted at once:

1. The image is resized (here **640×640**) and passed **once** through the CNN.
2. The network splits the image into a grid and predicts directly, for each cell, candidate boxes: position `(cx, cy)`, size `(w, h)`, objectness score and class - **all simultaneously**.
3. A simple final cleanup (**NMS**) removes duplicates. It's not a network, just a filter.

=> A single network pass: **fast** (ideal for real-time & the browser), at the cost of slightly lower precision on very small or very dense objects.

## [NMS (Non-Maximum Suppression)](https://learnopencv.com/non-maximum-suppression-theory-and-implementation-in-pytorch/)

The same object often triggers **several overlapping boxes**. **Non-Maximum Suppression** (NMS) keeps only the best one:

1. **Sort** boxes by confidence score, highest first.
2. **Keep** the top box, then **discard** every box that overlaps it too much - i.e. whose **IoU** (*Intersection over Union*, the shared area divided by the total area) exceeds a set threshold.
3. **Repeat** on the remaining boxes until none are left to process.

=> Result: **one box per object**, the one the model is most confident about.

<img src="/guide/yolo-nms.png" style="display:block;margin:1.5rem auto;width:100%;height:auto;">

:::info In this project, NMS runs in JavaScript
We export the ONNX model **without embedded NMS**, because that operation runs poorly in ONNX Runtime Web. The browser handles NMS itself (`frontend/src/inference/postprocess.js`).

=> It's more reliable.
:::

## [YOLOv8n](https://docs.ultralytics.com/models/yolov8#overview)

### Choosing the nano variant

The YOLOv8 family offers five sizes. The choice depends on the deployment context - here, the model must **run in the browser via ONNX Runtime Web**, which puts a hard constraint on the `.onnx` file size.

| Variant | Parameters | ONNX size | Use |
| --- | --- | --- | --- |
| **YOLOv8n** | ~3 M | ~6 MB | browser, mobile ✅ |
| YOLOv8s | ~11 M | ~22 MB | good trade-off, acceptable load time |
| YOLOv8m | ~25 M | ~50 MB | GPU server |
| YOLOv8l / x | 43–68 M | >80 MB | max accuracy, GPU required |

`yolov8n` is the project default. `yolov8s` is still usable in the browser if a longer load time is acceptable.

### Fine-tuning on pools & buildings

Training a detector from scratch would require millions of images and weeks of GPU compute. **Fine-tuning** avoids that cost: instead of relearning everything, we start from a YOLOv8 model already trained on **[COCO](https://cocodataset.org/)** (80 everyday object classes - cars, people, animals…) and specialise it on our two classes.

<img src="/guide/yolo_fine-tuning.png" style="display:block;margin:1.5rem auto;width:100%;height:auto;">

The key idea: a detector is made up of two parts.

- The **backbone** has already learned to extract generic visual features - edges, textures, shapes. These skills are *universal*, valid for any object, so we **keep them as-is** (we say those layers are "frozen").
- The **detection head** is the part that decides *which object* and *where*. This is what we **retrain** on our annotated IGN images (pools / buildings).

:::tip Result
The model reuses all its visual knowledge and only learns what is specific to our task, in a few dozen **epochs** (passes over the dataset) instead of thousands. The fine-tuned weights are then exported to `.onnx` to run in the browser.
:::
