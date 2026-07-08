# [ONNX](https://onnx.ai/)

Dans geo-ml, une fois le modèle YOLOv8 fine-tuné sur nos piscines & bâtiments, il faut le faire tourner **dans le navigateur**, sans serveur, sans Python, sans GPU. C'est là qu'intervient ONNX : on exporte les poids entraînés dans un format universel (`.onnx`), que le navigateur charge et exécute directement via **[ONNX Runtime Web](https://onnxruntime.ai/docs/tutorials/web/)**. Le calcul d'inférence se fait entièrement côté client, sur la machine de l'utilisateur.

:::info
**ONNX** (*Open Neural Network Exchange*) est un **format de fichier universel** pour les modèles de machine learning. Il permet d'entraîner un modèle dans une bibliothèque (ici [PyTorch](https://docs.pytorch.org/docs/2.12/onnx.html) / [Ultralytics](https://docs.ultralytics.com/integrations/onnx)) et de l'exécuter **ailleurs**, y compris dans un navigateur web, sans serveur.
:::

## Principe de fonctionnement

Un modèle entraîné est attaché à son framework : un `.pt` PyTorch a besoin de PyTorch pour tourner. Or PyTorch ne tourne pas dans un navigateur.

ONNX découple le **modèle** de la **bibliothèque d'entraînement** en sérialisant le graphe de calcul et les poids dans un fichier portable 

:::tip Graphe de calcul & poids
- **Graphe de calcul** : la *recette* du modèle, la liste ordonnée des opérations (convolutions, normalisations, activations…) et comment elles se chaînent. C'est l'architecture du réseau.
- **Poids** : les *valeurs numériques* apprises pendant l'entraînement, des millions de nombres qui, combinés avec le graphe, produisent les détections. Sans les poids, le graphe est une coquille vide.
:::

<img src="/guide/onnx-export.png" style="display:block;margin:1.5rem auto;width:100%;height:auto;">

:::info
N'importe quel *runtime* ONNX compatible sait charger ce fichier et l'exécuter.
:::

## [ONNX Runtime Web](https://onnxruntime.ai/docs/tutorials/web/)

Le projet est déployé **sans backend** (GitHub Pages). L'inférence doit donc tourner côté client. C'est le rôle d'**ONNX Runtime Web** :

:::tip Inférence
L'**inférence** est l'étape où le modèle *utilise* ce qu'il a appris : on lui donne une image, il renvoie des prédictions (boîtes, classes, scores). C'est l'opposé de l'entraînement, ici on ne modifie plus les poids, on les applique.
:::

- il charge le `.onnx` directement dans la page
- il l'exécute en **[WebAssembly (WASM)](https://webassembly.org/)**, du code quasi-natif dans le navigateur

:::tip WebAssembly (WASM)
Format binaire exécutable par tous les navigateurs modernes, conçu pour tourner à une vitesse proche du natif. Il permet de faire tourner du code C++/Rust (ici le moteur ONNX) dans un onglet, sans plugin ni installation.
:::