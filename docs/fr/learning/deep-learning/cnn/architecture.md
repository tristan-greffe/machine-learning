# L'architecture

Un CNN (*ConvNet*, réseau de neurones convolutif) empile toujours les mêmes briques, dans le même ordre :

<img src="/learning/deep-learning/cnn/19_cnn.png" style="display:block;margin:0 auto;width:100%;height:auto;">

La première moitié **extrait des motifs** de plus en plus abstraits (bords → textures → formes → objets) ; la seconde **décide** à quelle classe ils correspondent.

## Couche de convolution

Une **couche de convolution** est l'empilement de N filtres appris ensemble. Chaque filtre (petite matrice de poids, typiquement 3×3) glisse sur l'entrée et produit une *feature map* ; les N feature maps empilées forment la sortie de la couche.

<img src="/learning/deep-learning/cnn/09_conv2d.png" style="display:block;margin:0 auto;width:100%;height:auto;">

Trois paramètres définissent la couche :

- **Nombre de filtres** (`out_channels`) : combien de motifs différents on cherche. C'est la profondeur de la sortie.
- **Taille du noyau** (`kernel_size`, ex. 3×3) : l'étendue locale que chaque filtre regarde.
- **Padding / stride** : le padding garde la résolution stable ; le stride saute des positions pour réduire la taille.

:::tip Le nombre de filtres ≠ les canaux d'entrée
Sur une image RGB, l'entrée a **3 canaux** (`in_channels`). Une couche peut produire **64 feature maps** (`out_channels`) : chaque filtre voit les 3 canaux à la fois, mais on en empile 64 pour obtenir 64 vues différentes. Les deux dimensions sont indépendantes.
:::

## ReLU

Après chaque convolution, une fonction d'activation **ReLU** (*Rectified Linear Unit*) est appliquée pixel par pixel : `f(x) = max(0, x)`. Elle remet à zéro les valeurs négatives et laisse passer les positives.

<img src="/learning/deep-learning/cnn/relu.svg" style="display:block;margin:0 auto;width:100%;height:auto;">

:::info Pourquoi c'est indispensable
La convolution est une opération **linéaire**. Empiler dix convolutions linéaires les unes après les autres reviendrait mathématiquement à **une seule** transformation linéaire — aucun gain. ReLU introduit une **non-linéarité** entre les couches : c'est ce qui permet au réseau d'apprendre des relations complexes (formes, textures, objets) et pas seulement des combinaisons linéaires de pixels.
:::

ReLU a remplacé les anciennes activations (`tanh`, `sigmoid`) car son gradient ne sature pas pour les grandes valeurs : l'entraînement converge bien plus vite et les couches profondes apprennent réellement.

## Couche de pooling

Une **couche de pooling** réduit la résolution spatiale d'une feature map sans rien apprendre. C'est la deuxième brique fondamentale après la convolution.

:::tip Trois choses qu'elle fait pour le réseau
- **Réduit la taille** des feature maps d'un facteur 2 typiquement, ce qui allège les couches suivantes.
- **Introduit une invariance** à de petits décalages : un motif détecté en position (10, 12) reste détectable s'il glisse en (11, 13).
- **Aucun poids à apprendre** : c'est juste une opération de réduction, gratuite à entraîner.
:::

:::details Pourquoi pooler ?
Une couche de convolution garde la même résolution que son entrée (avec padding `same`). Sans pooling, une image 256×256 reste 256×256 à toutes les profondeurs, et le réseau garde 65 536 positions à traiter par filtre. Très vite :

- Le calcul explose : chaque couche ajoute son cube `H × W × N` à traiter.
- Le récepteur reste local : un neurone profond ne voit toujours qu'un voisinage de quelques pixels.
:::

Le pooling prend une fenêtre (typiquement 2×2) et la réduit à **une valeur**. Deux stratégies coexistent :

<img src="/learning/deep-learning/cnn/20_cnn.svg" style="display:block;margin:0 auto;width:100%;height:auto;">

- **Max pooling** garde la plus grande activation, donc le motif **le plus saillant** de la fenêtre. C'est le défaut dans 90 % des CNN modernes.
- **Average pooling** moyenne les valeurs, lisse la feature map. Utilisé en bout de réseau (*global average pooling*) pour résumer chaque carte en un scalaire avant la classification.

:::details Dropout : l'astuce de régularisation associée
Souvent placé près du pooling dans les blocs profonds, le **Dropout** complète la régularisation :

- Pendant l'entraînement, à chaque batch, on **désactive aléatoirement** une fraction `p` des neurones (typiquement 0.2 à 0.5).
- À l'inférence, tous les neurones sont actifs.
- Effet : le réseau ne peut pas trop dépendre d'un neurone particulier → moins d'overfitting.

Pooling et Dropout travaillent ensemble : le pooling réduit le **nombre de positions**, le Dropout force le réseau à **distribuer l'information** entre neurones.
:::

## Couche fully connected (dense)

À la fin de l'extraction, les feature maps sont **aplaties** (*flatten*) en un grand vecteur, puis passées dans une ou plusieurs couches **denses** où chaque neurone est connecté à tous les précédents. C'est là que le réseau combine les motifs détectés pour décider.

:::warning Le gros des paramètres est ici
Dans les architectures anciennes (AlexNet, VGG), les couches denses concentrent l'écrasante majorité des paramètres (ex. ~123 M des 138 M de VGG). Les architectures modernes (ResNet) les remplacent largement par du *global average pooling*, beaucoup plus léger.
:::

## Softmax (couche de sortie)

Pour la classification, la dernière couche dense produit un score brut par classe (*logits*). **Softmax** les transforme en **probabilités** : toutes positives et de somme égale à 1.0. La classe retenue est celle de plus forte probabilité, qui sert aussi de **score de confiance**.

Pour une classification binaire (arbre / pas arbre) ou une segmentation pixel à pixel, on utilise plutôt **sigmoïde** (une probabilité indépendante par sortie).

## Architectures connues qui empilent ces briques

| Architecture | Année | Particularité |
| ------------ | ----- | ------------- |
| LeNet-5      | 1998  | Le pionnier, 7 couches, classification de chiffres |
| AlexNet      | 2012  | A relancé le deep learning |
| VGG          | 2014  | Filtres 3×3 partout, beaucoup de profondeur |
| GoogLeNet    | 2014  | Modules « Inception », branches parallèles |
| ResNet       | 2015  | Skip connections, jusqu'à 152 couches |
| U-Net        | 2015  | Encodeur-décodeur pour la segmentation |

Trois jalons montrent comment ces briques s'assemblent et évoluent.

### LeNet-5 : le schéma fondateur

<img src="/learning/deep-learning/cnn/arch-lenet5.svg" style="display:block;margin:0 auto;width:100%;height:auto;">

### VGG : la profondeur par des 3×3

<img src="/learning/deep-learning/cnn/arch-vgg.svg" style="display:block;margin:0 auto;width:100%;height:auto;">

### ResNet : la skip connection

<img src="/learning/deep-learning/cnn/arch-resnet.svg" style="display:block;margin:0 auto;width:100%;height:auto;">
