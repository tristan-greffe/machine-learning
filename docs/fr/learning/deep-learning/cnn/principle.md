# Principe de convolution d'images

Un filtre (ou *kernel*, ou *noyau*) est une petite matrice de poids. On le fait glisser sur l'image : à chaque position, on multiplie les valeurs du filtre par les pixels sous-jacents et on additionne. Le résultat est un pixel dans la **carte d'activation** (*feature map*).

<img src="/learning/deep-learning/cnn/04_convolution.png" style="display:block;margin:0 auto;width:100%;height:auto;">

:::tip Terminologie
- **filtre / noyau / kernel** = la matrice de poids (3×3 ici).
- **convolution** = l'opération de glissement + multiplication + somme.
- **Couche de convolution** = un **ensemble de N filtres** appliqués en parallèle à la même entrée. Sortie : N feature maps empilées.
- **feature map** = l'image de sortie produite par un filtre donné.
:::

:::details Glissement de la fenêtre
L'animation ci-dessous montre concrètement comment le noyau parcourt l'image, pixel par pixel.
<div style="display: flex; gap: 2rem;">
<div style="flex: 1">
<img src="/learning/deep-learning/cnn/05_cnn.png" style="display:block;margin:0 auto;width:100%;height:auto;">
</div>
<div style="flex: 1">
<img src="/learning/deep-learning/cnn/06_cnn.png" style="display:block;margin:0 auto;width:100%;height:auto;">
</div>
</div>
:::

## 2D convolution : image en niveaux de gris

### Appliquer le filtre sur l'image 

<img src="/learning/deep-learning/cnn/07_cnn.png" style="display:block;margin:0 auto;width:100%;height:auto;">

<img src="/learning/deep-learning/cnn/08_cnn.png" style="display:block;margin:0 auto;width:100%;height:auto;">

### Couches de convolutions `Conv2d`

<img src="/learning/deep-learning/cnn/10_cnn.png" style="display:block;margin:0 auto;width:100%;height:auto;">

## 3D convolution : image en couleur

### Appliquer le filtre sur l'image 

<img src="/learning/deep-learning/cnn/11_cnn.png" style="display:block;margin:0 auto;width:100%;height:auto;">

:::details RGB
Une image en couleur a trois canaux R, G, B.
<img src="/learning/deep-learning/cnn/13_cnn.png" style="display:block;margin:0 auto;width:50%;height:auto;">
Pour la convolution, le filtre doit pouvoir voir les trois canaux à la fois, il devient donc lui aussi un volume 3D.
<img src="/learning/deep-learning/cnn/14_cnn.png" style="display:block;margin:0 auto;width:50%;height:auto;">
Concrètement, un noyau 3×3 sur une image RGB n'est pas une matrice 3×3, c'est un volume 3×3×3 : un sous-noyau 3×3 par canal, dont les sorties sont **sommées** pour produire un seul pixel de feature map.
<img src="/learning/deep-learning/cnn/15_cnn.png" style="display:block;margin:0 auto;width:50%;height:auto;">
:::

### Couches de convolutions `Conv2d`
<img src="/learning/deep-learning/cnn/12_cnn.png" style="display:block;margin:0 auto;width:100%;height:auto;">

## Paramètres

### Padding

Quand le noyau arrive au bord de l'image, une partie de la fenêtre **tombe dans le vide**. On a deux conséquences :

1. La feature map est **plus petite** que l'image d'entrée.
2. Les pixels du bord sont **sous-représentés**, chaque pixel intérieur participe à 9 calculs (pour un 3×3), un pixel de coin n'en voit qu'**un seul**.

<div style="display: flex; gap: 2rem;">
<div style="flex: 1">
<img src="/learning/deep-learning/cnn/16_cnn.png" style="display:block;margin:0 auto;width:100%;height:auto;">
</div>
<div style="flex: 1">
<img src="/learning/deep-learning/cnn/17_cnn.png" style="display:block;margin:0 auto;width:100%;height:auto;">
</div>
</div>


**Solution : le padding** : On ajoute des **pixels fictifs** autour de l'image avant la convolution. Le plus simple est le *zero-padding* (on remplit avec des 0) ; on trouve aussi le *reflect* (miroir) ou le *replicate* (copie du bord).
<img src="/learning/deep-learning/cnn/18_cnn.png" style="display:block;margin:0 auto;width:50%;height:auto;">

### Strides (Le pas)

Au lieu de glisser le noyau d'**un pixel**, on peut le faire glisser de 2, 3, n. C'est le **stride**. Effet : la feature map est sous-échantillonnée, la sortie devient plus petite que l'entrée d'un facteur égal au stride.
