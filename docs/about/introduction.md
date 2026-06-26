# GeoML

**GeoML** is a hands-on geospatial machine learning project: train object-detection models on real aerial imagery, export them to [ONNX](https://onnx.ai/), and ship a fully static SPA that runs inference directly in the browser, no backend required.

<img src="/guide/architecture.png" style="display:block;margin:2rem auto;width:100%;">

- **A React SPA** drives the map ([MapLibre](https://maplibre.org/projects/gl-js/)) and runs [inference](https://www.oracle.com/artificial-intelligence/ai-inference/) locally via [ONNX Runtime Web](https://onnxruntime.ai/docs/tutorials/web/). Tile layers ([IGN WMTS](https://cartes.gouv.fr/aide/fr/guides-utilisateur/utiliser-les-services-de-la-geoplateforme/diffusion/wmts/), [OSM](https://wiki.openstreetmap.org/wiki/Main_Page)…) are fetched directly from the browser.
- **An offline training pipeline** downloads raw IGN satellite tiles and BD TOPO/OSM polygons, automatically generates an annotated dataset in [YOLO format](https://docs.ultralytics.com/datasets/detect#supported-dataset-formats), fine-tunes a [YOLOv8](https://docs.ultralytics.com/models/yolov8#overview) model, and exports `.onnx` weights bundled with the SPA.

:::tip Why no backend
[YOLOv8n](https://docs.ultralytics.com/models/yolov8#overview) models are small enough (~12 MB each) to run client-side via [WebAssembly](https://webassembly.org/).
:::
