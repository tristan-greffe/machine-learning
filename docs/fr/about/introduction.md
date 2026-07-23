# GeoML

**GeoML** est un projet appliqué de machine learning géospatial : entraîner des modèles de détection d'objets sur de vraies images aériennes, les exporter en [ONNX](https://onnx.ai/), et livrer un SPA 100 % statique qui exécute l'inférence directement dans le navigateur, sans backend.

<img src="/guide/geoml-archi.png" style="display:block;margin:2rem auto;width:100%;">

- **Un SPA React** pilote la carte ([MapLibre](https://maplibre.org/projects/gl-js/)) et exécute l'[inférence](https://www.oracle.com/fr/artificial-intelligence/ai-inference/) localement via [ONNX Runtime Web](https://onnxruntime.ai/docs/tutorials/web/). Les couches de tuiles ([IGN WMTS](https://cartes.gouv.fr/aide/fr/guides-utilisateur/utiliser-les-services-de-la-geoplateforme/diffusion/wmts/), [OSM](https://wiki.openstreetmap.org/wiki/Main_Page) …) sont appelées directement depuis le navigateur.
- **Un pipeline d'entraînement offline** télécharge des tuiles satellitaires IGN et des polygones BD TOPO/OSM, génère automatiquement un dataset annoté au [format YOLO](https://docs.ultralytics.com/datasets/detect#supported-dataset-formats), affine un modèle [YOLOv8](https://docs.ultralytics.com/models/yolov8#overview), et exporte les poids `.onnx` intégrés au SPA.

:::tip Pourquoi sans backend
Les modèles [YOLOv8n](https://docs.ultralytics.com/models/yolov8#overview) sont suffisamment petits (~12 Mo chacun) pour tourner côté client via [WebAssembly](https://webassembly.org/).
:::
