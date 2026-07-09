# Jeu de données

Dans **geo-ml**, il n'y a **aucune annotation manuelle**. C'est le principe central du projet : les labels existent déjà, sous forme de données vectorielles ouvertes et gratuites couvrant toute la France. Les polygones de bâtiments proviennent de la **BD TOPO IGN**, ceux des piscines d'**OpenStreetMap**.
 
Le rôle du pipeline est donc uniquement mécanique : télécharger des tuiles satellitaires IGN, assembler des mosaïques, convertir les polygones GPS en boîtes exprimées en pixels, puis découper le tout en fenêtres 640×640 au format attendu par YOLO.
 
::: tip Aucune annotation manuelle
Les labels couvrent toute la France. On télécharge, on convertit, on entraîne, sans jamais dessiner une boîte à la main.
:::

## Sources des labels
 
| Objet | Source | Couche / tag |
| --- | --- | --- |
| **Bâtiments** | [BD TOPO IGN](https://geoservices.ign.fr/bdtopo) | `BDTOPO_V3:batiment` |
| **Piscines** | [OpenStreetMap](https://www.openstreetmap.org/) | `leisure=swimming_pool` |
 
Les deux sources renvoient des **polygones GPS** (GeoJSON) que le pipeline convertit ensuite en bounding boxes pixel.
 
## Format YOLO
 
YOLOv8 attend un dataset structuré autour d'un fichier de configuration `dataset.yaml` qui décrit les chemins et les noms de classes. Voir le [format officiel Ultralytics](https://docs.ultralytics.com/datasets/detect#supported-dataset-formats).
 
```
model/dataset/<modèle>/
├── dataset.yaml          ← chemins + noms de classes
├── images/
│   ├── train/  *.jpg     ← fenêtres 640×640 (80 %)
│   └── val/    *.jpg     ← fenêtres 640×640 (20 %)
└── labels/
    ├── train/  *.txt     ← une ligne par objet
    └── val/    *.txt
```
 
::: tip `train/` vs `val/`
Le dataset est découpé **80 % / 20 %** au moment de l'écriture :
 
- **`train/`**: les images que le modèle voit pendant l'entraînement. Il calcule ses erreurs dessus et ajuste ses poids à chaque passe.
- **`val/`**: les images que le modèle ne voit **jamais** pendant l'entraînement. Elles servent uniquement à mesurer sa qualité réelle à la fin de chaque epoch.
Si la performance sur `val` se dégrade alors que celle sur `train` continue de s'améliorer, c'est le signe d'un **sur-apprentissage** (*overfitting*).
:::
 
### Structure d'un fichier de labels
 
Chaque image `images/train/000042.jpg` possède un fichier `labels/train/000042.txt` associé. Chaque ligne du `.txt` décrit **un objet** :
 
```
0  0.666  0.655  0.156  0.181
↑    ↑      ↑      ↑      ↑
class  cx    cy     w      h    (tout normalisé entre 0.0 et 1.0)
```
 
::: tip Détail des champs
- **`class`**: identifiant de la classe (`0` = bâtiment ou piscine selon le modèle). Un seul entier.
- **`cx`, `cy`**: coordonnées du **centre** de la boîte, normalisées entre `0.0` et `1.0` (`0` = bord gauche/haut, `1` = bord droit/bas).
- **`w`, `h`**: **largeur** et **hauteur** de la boîte, normalisées de la même façon.
Tout est relatif à l'image 640×640 : aucun pixel absolu.
:::
 
```yaml
# dataset.yaml (généré automatiquement)
path: /abs/path/to/model/dataset/buildings
train: images/train
val:   images/val
names:
  0: building
```

## Vue d'ensemble du pipeline
 
Le pipeline part de deux sources de données distinctes, l'une vectorielle (les annotations), l'autre raster (l'imagerie), qui finissent par se rejoindre pour produire le dataset final.
 
<img src="/guide/dataset_pipeline_overview.png" style="display:block;margin:1.5rem auto;width:100%;height:auto;">

**1. Récupération des annotations (source vectorielle)**
- Téléchargement des polygones GPS depuis les données ouvertes : **BD TOPO** (via WFS) et **OpenStreetMap** (via Overpass).
- Ces polygones délimitent les objets à détecter (piscines, bâtiments).

**2. Récupération de l'imagerie (source raster)**
- Téléchargement des tuiles **256×256 px** depuis **IGN WMTS** (`data.geopf.fr`), au zoom 19 (~20 cm/px).
- Mise en cache disque dans `model/dataset/_tilecache/` pour éviter de re-télécharger les mêmes tuiles.

**3. Assemblage de la mosaïque**
- Assemblage de **4×4 tuiles** en une **mosaïque 1024×1024 px** (~200 m × 200 m au sol), à résolution native.

**4. Conversion des coordonnées**
- Les polygones GPS sont projetés sur la mosaïque : conversion **GPS → pixel**, ce qui produit des **bounding boxes** exprimées en pixels.

**5. Découpe en fenêtres**
- La mosaïque est découpée en **fenêtres 640×640 px** (la taille d'entrée de YOLO), selon une stratégie de découpe propre à chaque modèle.

**6. Génération du dataset final**
- Chaque fenêtre produit une paire image + annotations, répartie entre entraînement et validation :
  - `images/train/` et `images/val/` → les images `*.jpg`
  - `labels/train/` et `labels/val/` → les annotations `*.txt` (format YOLO)

### Pourquoi assembler une mosaïque ?
 
Une tuile IGN brute fait 256×256 px, trop petite pour une fenêtre YOLO de 640×640. L'upscaler floute l'image et annule l'intérêt de la haute résolution IGN. En assemblant 4×4 tuiles, on obtient une mosaïque 1024×1024 px à résolution native, dans laquelle on peut découper plusieurs fenêtres 640×640. C'est aussi exactement la même échelle qu'à l'inférence, ce qui garantit que le modèle voit la même résolution à l'entraînement et en production.
 
<img src="/guide/mosaique.png" style="display:block;margin:1.5rem auto;width:100%;height:auto;">

## Deux stratégies selon la densité
 
Bâtiments et piscines ont une répartition très différente dans l'espace. Le pipeline adapte donc sa stratégie de découpe à chaque type d'objet.
 
### Bâtiments - fenêtre glissante sur grille
 
Les bâtiments sont **denses et uniformément répartis**. Pour chaque zone, on assemble une grande mosaïque puis on fait **glisser une fenêtre 640×640 avec 25 % de recouvrement** sur toute la surface, afin de garantir une couverture exhaustive sans couper d'objet en bordure.
 
<img src="/guide/dataset_batiments.png" style="display:block;margin:1.5rem auto;width:100%;height:auto;">

**Étapes pour chaque zone :**
 
1. Télécharger les tuiles IGN → assembler la mosaïque.
2. Requêter **BD TOPO WFS** pour les polygones de bâtiments de la zone.
3. Convertir les polygones GPS → bboxes pixel sur la mosaïque.
4. Faire glisser la fenêtre 640×640 → écrire image + labels YOLO.

### Piscines - fenêtre centrée avec jitter
 
Les piscines sont **rares et dispersées** : une grille produirait surtout des images vides. À la place, pour **chaque piscine**, on télécharge une mosaïque centrée dessus, puis on découpe une fenêtre avec un décalage aléatoire (**jitter ±120 px**) afin d'améliorer l'invariance à la position.
 
<img src="/guide/dataset_piscines.png" style="display:block;margin:1.5rem auto;width:100%;height:auto;">

**Étapes pour chaque zone :**
 
1. Requêter **OSM Overpass** → polygones `leisure=swimming_pool`.
2. Filtrer les piscines hors-norme (`< 1,5 m` ou `> 35 m`).
3. Pour chaque piscine : télécharger une mosaïque centrée.
4. Découper une fenêtre 640×640 avec jitter → labelliser **toutes** les piscines visibles → écrire.

::: warning Labelliser toutes les piscines de la fenêtre
Si une fenêtre contient 3 piscines mais qu'on n'en marque qu'une, on apprend au modèle que les 2 autres sont du fond → **faux négatifs**. Le script labellise donc **toutes** les piscines présentes dans la fenêtre, pas seulement celle qui a servi au centrage.
:::

## Télécharger le jeu de données

```bash
conda activate geoml

python -m model.dataset.main              # bâtiments + piscines (défaut)
python -m model.dataset.main --buildings  # bâtiments seulement
python -m model.dataset.main --pools      # piscines seulement
```

| Argument | Description |
| --- | --- |
| *(aucun)* | Génère les deux datasets (bâtiments + piscines) |
| `--buildings` | Génère uniquement le dataset bâtiments (BD TOPO WFS) |
| `--pools` | Génère uniquement le dataset piscines (OSM Overpass) |

:::info imprécision du jeu de données
Les polygones BD TOPO et OSM ne sont pas toujours **parfaitement alignés** avec l'orthophoto IGN, un décalage de 1 à 2 m est courant. Les boîtes sont donc parfois légèrement décalées. YOLO tolère bien ce bruit d'étiquetage, mais c'est la principale source d'imprécision du jeu de données.
:::
