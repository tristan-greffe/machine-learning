# Entraînement - `model/train.py`

`model/train.py` est le point d'entrée unique pour entraîner un modèle et exporter les poids en `.onnx`. Il orchestre trois étapes : parsing des arguments, entraînement YOLOv8, export ONNX vers le frontend.

```bash
python model/train.py --model buildings
python model/train.py --model pools
```

<img src="/guide/train_flow.png" style="display:block;margin:1.5rem auto;width:100%;height:auto;">

## Arguments

| Argument | Défaut | Description |
| --- | --- | --- |
| `--model` | *(requis)* | Dataset à utiliser : `buildings` ou `pools` |
| `--epochs` | `80` | Nombre de passes complètes sur le dataset |
| `--batch` | `16` | Nombre d'images par itération |
| `--patience` | `20` | Arrêt anticipé : stoppe si le mAP ne progresse plus pendant N epochs |
| `--base` | `yolov8n.pt` | Checkpoint de départ pour le fine-tuning |
| `--resume` | `False` | Reprend depuis `model/runs/<model>/weights/last.pt` |
| `--no-export` | `False` | Ignore l'export ONNX après l'entraînement |

:::tip Meilleure config qualité
```bash
python model/train.py --model buildings --base yolov8s.pt --epochs 150 --batch 32 --patience 40
```
`yolov8s` est plus précis que `yolov8n` (~22 MB ONNX vs ~6 MB) mais reste chargeable en browser.
:::

## Structure du script
 
Le script se découpe en trois fonctions indépendantes, qui correspondent aux trois étapes du schéma ci-dessus.
 
### 1. `parse_arguments()`
 
Déclare et parse les arguments CLI, puis retourne l'objet `args`.
 
### 2. `run_training(args)`
 
Lance l'entraînement YOLOv8 et retourne le chemin vers `best.pt`.
 
1. **Vérifie que le dataset existe** (`model/dataset/<model>/dataset.yaml`). Sinon, affiche la commande à lancer pour le générer, puis quitte.
2. **Charge le checkpoint de base** (`args.base`), ou reprend depuis `last.pt` si `--resume` est passé.
3. **Lance `model.train(...)`** avec les augmentations adaptées aux orthophotos IGN.
4. **Copie `best.pt`** dans `model/weights/<model>.pt`.
**Augmentations configurées :**
 
```python
# Aerial imagery has no canonical orientation - full rotation and both flips are valid
fliplr=0.5, flipud=0.5, degrees=180,
# Mild colour jitter to handle IGN sensor variability across acquisition zones
hsv_h=0.015, hsv_s=0.5, hsv_v=0.4,
mosaic=1.0,
```
 
::: info Pourquoi ces augmentations ?
Les orthophotos n'ont **pas d'orientation canonique**, il n'existe pas de « haut » au sens où une photo de paysage en aurait un. Rotation complète (`degrees=180`) et flips dans les deux sens sont donc tous valides : ils multiplient les exemples sans introduire d'incohérence.
 
La variation de teinte (`hsv_*`) compense les **différences de calibration capteur** entre les zones d'acquisition IGN, qui ne sont pas toutes photographiées dans les mêmes conditions.
:::
 
### 3. `export_onnx(model_name, best_checkpoint)`
 
Exporte `best.pt` en `.onnx` et le copie dans `frontend/public/models/`.
 
```python
model.export(
    format="onnx",
    imgsz=640,
    opset=12,      # dernière version supportée par onnxruntime-web
    simplify=True, # simplifie le graphe (onnxslim)
    nms=False,     # NMS fait côté navigateur, pas dans le graphe
    dynamic=False, # shape d'entrée fixe, requis par onnxruntime-web
)
```
 
:::tip Pourquoi `nms=False` ?
L'opération **NMS** (suppression des boîtes en doublon, voir [YOLO](./yolo.md)) est mal supportée par ONNX Runtime Web. On l'**exclut du graphe** et on la réimplémente en JavaScript. Le `.onnx` ne renvoie alors que les boîtes brutes au format `[1, 5, 8400]` ; c'est le navigateur qui filtre par score et dédoublonne.
:::

:::tip Pourquoi `opset=12` ?
L'**opset** est la version du « vocabulaire » d'opérations ONNX. Un opset trop récent risque de contenir des opérations que le runtime navigateur ne reconnaît pas. `opset=12` est la dernière version largement supportée par ONNX Runtime Web.
:::

:::tip Pourquoi `dynamic=False` ?
ONNX Runtime Web requiert une **shape d'entrée fixe** pour initialiser sa session WASM. On la fixe donc à `640×640`, exactement la même que `IMAGE_SIZE` dans le dataset, ce qui garantit la cohérence entraînement / inférence.
:::

## Fichiers produits
 
À la fin de l'exécution, le script écrit deux familles de fichiers : les poids PyTorch (pour reprendre ou ré-exporter) et le modèle ONNX (pour le frontend).
 
```
model/
├── runs/<model>/weights/
│   ├── best.pt      ← meilleur checkpoint (sauvegardé automatiquement)
│   └── last.pt      ← dernier checkpoint (utile pour --resume)
└── weights/
    └── <model>.pt   ← copie de best.pt (point d'accès stable)
 
frontend/public/models/
└── <model>.onnx     ← servi avec le SPA, chargé par ONNX Runtime Web
```
 