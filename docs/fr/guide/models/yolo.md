# YOLO

Dans geo-ml, plutôt que d'entraîner un modèle de zéro (ce qui demanderait des millions d'images), on part d'un modèle **YOLOv8 déjà entraîné** sur un grand jeu d'images généralistes : il sait déjà reconnaître des formes, des contours, des textures. Puis, on le **spécialise ensuite sur notre tâche** (*fine-tuning*). C'est à dire qu'on poursuit son entraînement sur nos deux classes, **piscines** & **bâtiments**, avec un petit jeu d'images IGN. Le modèle réutilise ce qu'il sait déjà voir et apprend juste à reconnaître nos objets.

:::info
**[YOLO](https://arxiv.org/abs/2208.00773)** (*You Only Look Once*) est une famille de modèles de **détection d'objets** : à partir d'une image, ils renvoient une liste de **boîtes englobantes**, chacune avec une **classe** et un **score de confiance**. C'est le modèle au cœur de ce projet.
:::

## [Principe de fonctionnement](https://blent.ai/blog/a/detection-images-yolo-tensorflow)

<img src="/guide/yolo_vs_faster.png" style="display:block;margin:1.5rem auto;width:100%;height:auto;">

### 🔹 Avant YOLO : deux étapes, deux réseaux (ex. [Faster R-CNN](https://arxiv.org/abs/1506.01497)) 
Le détecteur/modèle passe l'image dans le réseau **plusieurs fois** :

1. **Proposer** des centaines de régions susceptibles de contenir un objet.
2. **Classer** chaque région *une par une* en la repassant dans un CNN.

=> Beaucoup de calculs répétés : **précis, mais lent**.

### 🔹 [YOLO fait tout en **une seule passe**](https://medium.com/@fatimazahra.belharar/object-detection-using-cnn-an-introduction-to-the-yolo-algorithm-df0f7b173c6) :
L'image traverse le réseau **une seule fois** et tout est prédit d'un coup :

1. L'image est redimensionnée (ici **640×640**) et passée **une seule fois** dans le CNN.
2. Le réseau découpe l'image en grille et prédit directement, pour chaque cellule, des boîtes candidates : position `(cx, cy)`, taille `(w, h)`, score d'objet et classe - **le tout simultanément**.
3. Un simple nettoyage final (**NMS**) supprime les doublons. Ce n'est plus un réseau, juste un filtre.

=> Une seule traversée du réseau : **rapide** (idéal pour le temps réel & le navigateur), au prix d'une précision un peu moindre sur les objets très petits ou très nombreux.

## [NMS (Non-Maximum Suppression)](https://learnopencv.com/non-maximum-suppression-theory-and-implementation-in-pytorch/)

Un même objet déclenche souvent **plusieurs boîtes qui se chevauchent**. Le **Non-Maximum Suppression** (NMS) ne garde que la meilleure :

1. **Trier** les boîtes par score de confiance, de la plus élevée à la plus faible.
2. **Garder** la boîte en tête de liste, puis **supprimer** toutes celles qui la recouvrent trop. c'est-à-dire dont l'**IoU** (*Intersection over Union*, l'aire commune divisée par l'aire totale) dépasse un seuil fixé.
3. **Répéter** sur les boîtes restantes jusqu'à ce qu'il n'en reste plus à traiter.

=> Résultat : **une seule boîte par objet**, celle dont le modèle est le plus sûr.

<img src="/guide/yolo-nms.png" style="display:block;margin:1.5rem auto;width:100%;height:auto;">

:::info Dans ce projet, le NMS est fait en JavaScript
On exporte le modèle ONNX **sans NMS embarqué**, car cette opération passe mal dans ONNX Runtime Web. Le navigateur fait donc le NMS (`frontend/src/inference/postprocess.js`)

=> C'est plus fiable
:::

## [YOLOv8n](https://docs.ultralytics.com/models/yolov8#overview)

### Choix du modèle nano

La gamme YOLOv8 propose cinq tailles. Le choix dépend du contexte de déploiement. ici, le modèle doit **tourner dans le navigateur via ONNX Runtime Web**, ce qui impose une contrainte forte sur la taille du fichier `.onnx`.

| Variante | Paramètres | Taille ONNX | Usage |
| --- | --- | --- | --- |
| **YOLOv8n** | ~3 M | ~6 MB | navigateur, mobile ✅ |
| YOLOv8s | ~11 M | ~22 MB | bon compromis, chargement acceptable |
| YOLOv8m | ~25 M | ~50 MB | serveur GPU |
| YOLOv8l / x | 43–68 M | >80 MB | précision max, GPU requis |

`yolov8n` est le défaut du projet. `yolov8s` reste utilisable en browser si on accepte un chargement plus long.

### Fine-tuning sur piscines & bâtiments

Entraîner un détecteur/modèle de zéro demanderait des millions d'images et des semaines de calcul GPU. Le **fine-tuning** contourne ce coût : au lieu de tout réapprendre, on part d'un modèle YOLOv8 déjà entraîné sur **[COCO](https://cocodataset.org/)** (80 classes d'objets du quotidien, voitures, personnes, animaux…) et on le spécialise sur nos deux classes.

<img src="/guide/yolo_fine-tuning.png" style="display:block;margin:1.5rem auto;width:100%;height:auto;">
L'idée clé : un détecteur se décompose en deux parties.

- Le **backbone** a déjà appris à extraire des caractéristiques visuelles génériques, contours, textures, formes. Ces compétences sont *universelles*, valables pour n'importe quel objet, donc on les **conserve telles quelles** (on dit qu'on « fige » ces couches).
- La **tête de détection** (*detection head*) est la partie qui décide *quel objet* et *où*. C'est elle qu'on **réentraîne** sur nos images IGN annotées (piscines / bâtiments).

:::tip Résultat
le modèle réutilise tout son savoir visuel et n'apprend que ce qui nous est spécifique, en quelques dizaines d'**epochs** (passages sur le jeu de données) au lieu de milliers. Les poids ainsi affinés sont ensuite exportés en `.onnx` pour tourner dans le navigateur.
:::