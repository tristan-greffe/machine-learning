# Réseaux de neurones convolutifs (CNN)

Les CNN sont une famille de réseaux de neurones conçus pour traiter des données organisées en **grille** : images (2D), vidéos (3D), signaux audio (1D). Ils sont la brique de base de quasiment toutes les tâches de computer vision.

<img src="/learning/deep-learning/cnn/01_cnn.png" style="display:block;margin:0 auto;width:100%;height:auto;">

## Qu’est-ce qu’un Convolutional Neural Network ?

Un Convolutional Neural Networks est une architecture de réseau de neurones qui comprend généralement plusieurs couches de convolution.

<img src="/learning/deep-learning/cnn/21_cnn.png" style="display:block;margin:0 auto;width:100%;height:auto;">

Les couches de convolution utilisent ce qu'on appelle des "filtres" ou "noyaux" pour balayer l'entrée (comme une image) et en extraire des caractéristiques spécifiques, telles que les bords, les textures, ou les formes. Chaque filtre est capable de détecter un type de caractéristique à différents endroits de l'entrée.

## Pourquoi pas un réseau classique ?

Un réseau de neurones classique (ANN) connecte chaque neurone à tous ceux de la couche suivante. Sur une image 256×256 en RGB, ça donne **196 608 entrées**, et chaque connexion a un poids à apprendre. C'est massif, lent, et surtout inutile : un pixel n'a de sens que dans le contexte de ses voisins immédiats.

:::tip Un CNN résout ce problème avec deux idées simples
- **Localité** : un filtre ne regarde qu'une petite zone à la fois (ex. 3×3 pixels)
- **Partage de poids** : le même filtre est appliqué partout sur l'image
:::

<img src="/learning/deep-learning/cnn/02_cnn.png" style="display:block;margin:0 auto;width:100%;height:auto;">

## Composants Clés d'un CNN

<img src="/learning/deep-learning/cnn/22_cnn.png" style="display:block;margin:0 auto;width:100%;height:auto;">

### Couches de convolution 

Les couches de convolution sont le cœur d'un CNN. Elles utilisent des **filtres** (petites matrices de poids) **qui se déplacent sur l'ensemble de l'entrée** (par exemple, une image) pour effectuer des **opérations matricielles**. 

Chaque filtre détecte des caractéristiques spécifiques comme **les bords, les angles ou d'autres motifs visuels** à partir de l'entrée brute.

Le filtre applique une **opération de convolution** en prenant le produit scalaire entre le filtre et des portions locales de l'entrée, créant ainsi une **carte de caractéristiques pour chaque filtre**. Cela permet de capturer des informations spatiales et de motif.

### Fonction d'activation ReLU

La **Rectified Linear Unit (ReLU)** est une fonction d'activation couramment utilisée qui ajoute de la non-linéarité au réseau. 

Sans non-linéarité, le réseau serait essentiellement un modèle linéaire, **limité dans sa capacité à traiter des formes complexes** de données.

ReLU **transforme toutes les valeurs négatives en zéro** et laisse les valeurs positives inchangées. Cela aide à accélérer la convergence du réseau lors de l'apprentissage et à réduire le problème de disparition des gradients (où les gradients deviennent très petits, entravant l'apprentissage).

### Pooling (sous-échantillonnage) 

La **couche de pooling**, souvent appelée aussi sous-échantillonnage, r**éduit la dimensionnalité de chaque carte de caractéristiques** tout en **conservant les caractéristiques les plus importantes**.

Les méthodes les plus courantes sont le **max pooling et l'average pooling**. Le max pooling renvoie la valeur maximale d'une portion de la carte de caractéristiques, tandis que l'average pooling calcule la moyenne.

Cette **réduction de dimensionnalité** permet de diminuer la quantité de calculs et de poids dans le réseau, ce qui aide à combattre le surajustement (overfitting) et améliore la généralisation du modèle

### Couches entièrement connectées 

Après plusieurs couches de convolution et de pooling, **les cartes de caractéristiques sont aplanies** et passées à des couches entièrement connectées, aussi connues sous le nom de couches denses.

**Ces couches combinent toutes les caractéristiques apprises** par les couches précédentes pour effectuer la classification. Les neurones dans une couche dense ont des connexions complètes à tous les activations de la couche précédente, comme dans les réseaux de neurones traditionnels.

## L'architecture typique

Un CNN enchaîne deux phases : l'**extraction de features** (convolution → activation → pooling, répété N fois) puis la **classification** (couches denses + softmax).

<img src="/learning/deep-learning/cnn/21_cnn.svg" style="display:block;margin:0 auto;width:100%;height:auto;">

**Entrée** : l'image brute, un tenseur `H × W × C` (ex. 256×256×3 en RGB).

**Convolution** : fait glisser N filtres 3×3 sur l'entrée ; chacun produit une *feature map*.

**ReLU** : `max(0, x)` sur chaque valeur. Supprime les négatifs et introduit la non-linéarité, sans laquelle empiler des couches ne servirait à rien.

**Pooling** : réduit la résolution (ex. le max de chaque fenêtre 2×2). Allège le calcul et rend le réseau insensible aux petits décalages.

**Flatten + couches denses (*fully connected*)** : aplatit les feature maps en un vecteur, puis connecte tous les neurones vers la sortie.

**Softmax** : convertit les scores en probabilités par classe (somme = 1.0).

**Sortie** : la classe prédite et son score de confiance.

:::info CNN simple analysant une image pour détecter des visages.
La première couche de convolution pourrait capturer des détails basiques comme les bords, ensuite une couche de pooling pourrait réduire la dimensionnalité, puis une autre couche de convolution pourrait détecter des parties de visage comme les yeux ou la bouche, avant de passer à une couche de classification qui décide si l'image contient un visage ou non.
:::

## Ce que le CNN apprend couche par couche

| Couche      | Ce qu'elle détecte                                       |
| ----------- | -------------------------------------------------------- |
| 1           | Bords, gradients de couleur                              |
| 2           | Textures, motifs simples                                 |
| 3           | Formes géométriques                                      |
| Profondes   | Objets complexes (couronne d'arbre, fenêtre, toit…)       |

Les premières couches sont génériques (détection de bords), les couches profondes sont spécifiques au domaine. C'est pourquoi on peut **réutiliser** un CNN pré-entraîné sur une grande base d'images et l'adapter à une tâche spécifique (*transfer learning*).
