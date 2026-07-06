# Introduction

You can detect many things on an orthophoto, but not all are equally hard. Two factors decide feasibility: the **availability of ready-made labels** and the **shape** of the object.

* 🟢 `Pools`: single colour, simple shape, few false positives
* 🟢 `Buildings`: free [BD TOPO](https://geoservices.ign.fr/bdtopo) labels
* 🟡 `Forests`: IGN BD Forêt labels, but complex polygon merging
* 🟠 `Isolated trees`: high zoom required, instances hard to separate
* 🔴 `Roads`: thin, long, occluded by trees

:::tip This project's choice
**Pools** & **buildings**: simple shapes and freely available labels ([OpenStreetMap](https://www.openstreetmap.org/) for pools, [BD TOPO](https://geoservices.ign.fr/bdtopo) for buildings).
:::

## The three computer-vision tasks

Given an image, a model can answer three increasingly precise questions.

<img src="/guide/vision_tasks.png" style="display:block;margin:0 auto;width:100%;height:auto;">

| Task | Question | Output | Models |
|---|---|---|---|
| **Classification** | What is in the image? | One answer for the whole image ("it's a forest - 94%") | Classic CNN |
| **Object detection** | Where are the objects, and how many? | A bounding box around each object with a confidence score | YOLO, Faster R-CNN, SSD |
| **Segmentation** | Which class does each pixel belong to? | A class assigned to every pixel ("this pixel = building, that one = water") | U-Net, SegFormer |

:::info Choice: detection with [YOLOv8](https://docs.ultralytics.com/models/yolov8/)
Detection is **lighter**, **faster to train**, and **more reliable to export to ONNX** for client-side inference.
:::
