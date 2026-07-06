# Introduction

On peut détecter beaucoup de choses sur une orthophoto, mais toutes ne se valent pas en difficulté. Deux facteurs décident de la faisabilité : la **disponibilité de labels** prêts à l'emploi et la **forme** de l'objet.

* 🟢 `Piscines` : couleur unique, forme simple, peu de faux positifs
* 🟢 `Bâtiments` : labels gratuits [BD TOPO](https://geoservices.ign.fr/bdtopo)
* 🟡 `Forêts` : labels BD Forêt IGN, mais fusion de polygones complexe
* 🟠 `Arbres isolés` : zoom élevé requis, instances difficiles à séparer
* 🔴 `Routes` : fines, longues, occultées par les arbres

:::tip Le choix de ce projet
**piscines** & **bâtiments** : formes simples et labels disponibles gratuitement ([OpenStreetMap](https://www.openstreetmap.org/) pour les piscines, [BD TOPO](https://geoservices.ign.fr/bdtopo) pour les bâtiments).
:::

## Les trois tâches de computer vision

Face à une image, un modèle peut répondre à trois questions de plus en plus précises.

<img src="/guide/vision_tasks.png" style="display:block;margin:0 auto;width:100%;height:auto;">

| Tâche | Question | Sortie | Modèles |
|---|---|---|---|
| **Classification** | Qu'y a-t-il dans l'image ? | Une seule réponse pour toute l'image (« c'est une forêt - 94 % ») | CNN classique |
| **Détection d'objets** | Où sont les objets, et combien ? | Une boîte englobante (*bounding box*) autour de chaque objet, avec un score de confiance | YOLO, Faster R-CNN, SSD |
| **Segmentation** | À quelle classe appartient chaque pixel ? | Une classe attribuée à chaque pixel (« ce pixel = bâtiment, celui-là = eau ») | U-Net, SegFormer |

:::info Choix : détection avec [YOLOv8](https://docs.ultralytics.com/models/yolov8/)
La détection est **plus légère**, **plus rapide à entraîner**, **plus fiable à exporter en ONNX** pour tourner côté client.
:::
