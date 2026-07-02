# Démarrage rapide

## Prérequis

- **conda**: pour l'environnement Python d'entraînement
- **Node.js 20+**: pour le frontend et la documentation

:::tip Structure du dépôt
```
geo-ml/
├── frontend/          SPA React + MapLibre GL + ONNX Runtime Web
│   └── public/models/ poids .onnx servis avec le SPA
├── model/             Pipeline dataset (Python) + entraînement YOLOv8
│   └── dataset/       génération automatique du dataset annoté
└── docs/              Documentation VitePress
```
:::

## 1. Cloner le dépôt

```bash
git clone https://github.com/tristan-greffe/geo-ml.git
cd geo-ml
```

## 2. Environnement Python

Uniquement nécessaire pour générer un dataset ou entraîner un modèle. Le frontend tourne sans Python.

```bash
conda env create -f model/environment.yml    # première fois
conda env update -f model/environment.yml    # si le fichier change
conda activate geoml
```

## 3. Lancer le frontend

```bash
cd frontend
npm install
npm run dev
```

:::info
Ouvrir <http://localhost:5173/geo-ml/>.

Il n'y a pas d'API. cliquer sur **Run detection** charge le fichier `.onnx` depuis `public/models/`, exécute l'inférence dans le navigateur via ONNX Runtime Web, et affiche les résultats sur la carte.
:::

## 4. Générer un dataset et entraîner un modèle

```bash
conda activate geoml

# Générer le dataset (télécharge tuiles IGN + polygones BD TOPO / OSM)
python -m model.dataset.main --buildings
python -m model.dataset.main --pools

# Entraîner et exporter en ONNX (écrit dans frontend/public/models/)
python model/train.py --model buildings
python model/train.py --model pools
```

## 5. Lancer la documentation

```bash
cd docs
npm install
npm run dev
```

:::info
Ouvrir <http://localhost:5174/geo-ml/documentation/>.
:::
