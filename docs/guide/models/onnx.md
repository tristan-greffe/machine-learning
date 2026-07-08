# [ONNX](https://onnx.ai/)

In geo-ml, once the YOLOv8 model has been fine-tuned on our pools & buildings, it needs to run **in the browser** - no server, no Python, no GPU. That is where ONNX comes in: we export the trained weights into a universal format (`.onnx`) that the browser loads and executes directly via **[ONNX Runtime Web](https://onnxruntime.ai/docs/tutorials/web/)**. All inference computation runs entirely client-side, on the user's machine.

:::info
**ONNX** (*Open Neural Network Exchange*) is a **universal file format** for machine-learning models. It lets you train a model in one library (here [PyTorch](https://docs.pytorch.org/docs/2.12/onnx.html) / [Ultralytics](https://docs.ultralytics.com/integrations/onnx)) and run it **elsewhere** - including in a web browser, with no server.
:::

## How it works

A trained model is tied to its framework: a PyTorch `.pt` needs PyTorch to run. And PyTorch does not run in a browser.

ONNX decouples the **model** from the **training library** by serialising the compute graph and weights into a portable file.

:::tip Compute graph & weights
- **Compute graph**: the model's *recipe* - the ordered list of operations (convolutions, normalisations, activations…) and how they chain together. This is the network architecture.
- **Weights**: the *numerical values* learned during training - millions of numbers that, combined with the graph, produce the detections. Without the weights, the graph is an empty shell.
:::

<img src="/guide/onnx-export.png" style="display:block;margin:1.5rem auto;width:100%;height:auto;">

:::info
Any compatible ONNX runtime can load this file and execute it.
:::

## [ONNX Runtime Web](https://onnxruntime.ai/docs/tutorials/web/)

The project is deployed **without a backend** (GitHub Pages), so inference must run client-side. That is the role of **ONNX Runtime Web**:

:::tip Inference
**Inference** is the step where the model *uses* what it has learned: we give it an image, it returns predictions (boxes, classes, scores). It is the opposite of training - here we no longer modify the weights, we apply them.
:::

- it loads the `.onnx` directly into the page
- it executes it in **[WebAssembly (WASM)](https://webassembly.org/)** - near-native code in the browser

:::tip WebAssembly (WASM)
A binary format executable by all modern browsers, designed to run at near-native speed. It allows C++/Rust code (here the ONNX engine) to run in a browser tab, with no plugin or installation required.
:::