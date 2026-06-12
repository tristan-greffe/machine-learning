

<div align="center">

  ![Project Banner](./docs/public/banner_readme.svg)

  <h1>Geospatial ML <br> From model training to interactive map</h1>
  <h3>Building & pool detection on aerial imagery - YOLO models running in your browser</h3>  
  <p>
    <a href="https://github.com/tristan-greffe/machine-learning/stargazers">
      <img src="https://img.shields.io/github/stars/tristan-greffe/machine-learning" alt="stars" />
    </a>
    <a href="https://github.com/tristan-greffe/machine-learning/blob/master/LICENSE">
      <img src="https://img.shields.io/github/license/tristan-greffe/machine-learning.svg" alt="license" />
    </a>
    <a href="https://tristan-greffe.github.io/geo-ml/">
      <img src="https://img.shields.io/badge/deployed-GitHub%20Pages-059669" alt="deployed" />
    </a>
    <a href="https://tristan-greffe.github.io/geo-ml/documentation/">
      <img src="https://img.shields.io/badge/documentation-available-brightgreen.svg" alt="documentation" />
    </a>
  </p> 
  <h4>
    <a href="https://tristan-greffe.github.io/geo-ml/">View Online</a>
    <span> · </span>
    <a href="https://tristan-greffe.github.io/geo-ml/documentation/">View Documentation</a>
    <span> · </span>
    <a href="https://github.com/tristan-greffe/geo-ml/issues/">Report Bug</a>
  </h4>
</div>

<div align="center">
  <img src="./docs/public/geoml-project.png" height="auto" width="90%"/>
</div>

## Tech Stack

**Frontend**  
[![React](https://img.shields.io/badge/React-19-61DAFB?logo=react&logoColor=white)](https://react.dev)
[![Vite](https://img.shields.io/badge/Vite-646CFF?logo=vite&logoColor=white)](https://vite.dev)
[![MapLibre](https://img.shields.io/badge/MapLibre_GL-396CB2?logo=maplibre&logoColor=white)](https://maplibre.org)
[![ONNX Runtime Web](https://img.shields.io/badge/ONNX_Runtime_Web-005CED?logo=onnx&logoColor=white)](https://onnxruntime.ai/docs/tutorials/web/)

**Model**  
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch&logoColor=white)](https://pytorch.org)
[![Ultralytics YOLOv8](https://img.shields.io/badge/Ultralytics_YOLOv8-111F68?logo=yolo&logoColor=white)](https://docs.ultralytics.com)
[![ONNX](https://img.shields.io/badge/ONNX-005CED?logo=onnx&logoColor=white)](https://onnx.ai)

**Docs**  
[![VitePress](https://img.shields.io/badge/VitePress-5C73E7?logo=vitepress&logoColor=white)](https://vitepress.dev)

## Getting Started

Run the web app locally:
```bash
cd frontend
npm install
npm run dev
```

> [!NOTE]
> the ONNX models in `frontend/public/models/` load straight in the browser. Training the models (Python / Ultralytics) is optional and covered in the [documentation](https://tristan-greffe.github.io/geo-ml/documentation/).

## Contributing

Contributions are welcome. See the [contributing guide](https://tristan-greffe.github.io/geo-ml/documentation/about/contributing.html) in the documentation.

## License

This project is licensed under the MIT License - see the [license file](./LICENSE) for details
