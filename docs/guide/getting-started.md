# Getting started

## Prerequisites

- **conda**: for the Python training environment
- **Node.js 20+**: for the frontend and this documentation

## 1. Clone the repo

```bash
git clone https://github.com/tristan-greffe/geo-ml.git
cd geo-ml
```

## 2. Python environment

Only needed if you want to generate a dataset or train a model. The frontend runs without Python.

```bash
conda env create -f model/environment.yml    # first time
conda env update -f model/environment.yml    # whenever the file changes
conda activate geoml
```

## 3. Run the frontend

```bash
cd frontend
npm install
npm run dev
```

:::info
Open <http://localhost:5173/geo-ml/>.

There is no API. clicking **Run detection** loads the relevant `.onnx` file from `public/models/`, runs inference in the browser via ONNX Runtime Web, and renders the results on the map.
:::

## 4. Generate a dataset and train a model

```bash
conda activate geoml

# Build the dataset (downloads IGN tiles + BD TOPO / OSM polygons)
python -m model.dataset.main --buildings
python -m model.dataset.main --pools

# Train and export to ONNX (writes to frontend/public/models/)
python model/train.py --model buildings
python model/train.py --model pools
```

## 5. Run the documentation

```bash
cd docs
npm install
npm run dev
```

:::info
Open <http://localhost:5174/geo-ml/documentation/>.
:::
