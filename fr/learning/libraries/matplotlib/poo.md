# L'objet `Figure` de Matplotlib

Matplotlib offre une **approche orientée objet** permettant de créer des visualisations complexes et personnalisables grâce à l'objet `Figure`

## Qu'est-ce que l'objet `Figure` ?

L'objet `Figure` représente une **toile blanche** ou un **canevas vierge**, sur lequel des axes (`Axes`) peuvent être ajoutés.  
Il permet de gérer des propriétés globales affectant tous les axes :
* La taille de la figure
* La résolution (DPI)
* Les paramètres de rendu globaux

:::info
Par défaut, une figure a une taille de 432x288 pixels, ne contient aucun axe et n'affiche rien à l'écran.
```py
fig = plt.figure()  # Création d'une figure vide
```
<img src="/learning/libraries/matplotlib-figure-initialize.png" style="display: block; margin: 0 auto;width: 50%; height: auto;">
:::

## Ajouter un ensemble d'axes

Pour tracer des données, il est nécessaire d'ajouter un axe sur la figure.

:::info
```py
ax = fig.add_axes([0, 0, 1, 1])
```
<img src="/learning/libraries/matplotlib-figure-initialize-axes.png" style="display: block; margin: 0 auto;width: 50%; height: auto;">
:::

Les paramètres sont : `[x0, y0, largeur, hauteur]`
* `(x0, y0)` : coordonnées du coin inférieur gauche des axes, en proportion de la figure (0 à 1)
* `largeur` et `hauteur` : largeur et hauteur de l'axe, également en proportion de la figure

:::tip Exemples
* `fig.add_axes([0, 0, 1, 1])` : l'axe occupe toute la figure
* `fig.add_axes([0, 0, 0.5, 0.5])` : l'axe occupe la moitié de la largeur et de la hauteur
* `fig.add_axes([0.5, 0.5, 0.5, 0.5])` : l'axe commence au centre et occupe la moitié de la figure
:::

:::details Visualisation
<img src="/learning/libraries/matplotlib-figure-initialize-axes-1.png" style="display: block; margin: 0 auto;width: 70%; height: auto;">
<img src="/learning/libraries/matplotlib-figure-initialize-axes-2.png" style="display: block; margin: 0 auto;width: 70%; height: auto;">
<img src="/learning/libraries/matplotlib-figure-initialize-axes-3.png" style="display: block; margin: 0 auto;width: 70%; height: auto;">
<img src="/learning/libraries/matplotlib-figure-initialize-axes-4.png" style="display: block; margin: 0 auto;width: 70%; height: auto;">
<img src="/learning/libraries/matplotlib-figure-initialize-axes-5.png" style="display: block; margin: 0 auto;width: 70%; height: auto;">
<img src="/learning/libraries/matplotlib-figure-initialize-axes-6.png" style="display: block; margin: 0 auto;width: 70%; height: auto;">
:::

## Tracer sur un objet `Axes`

L’objet `Axes` constitue la zone de tracé où les données sont affichées. Il permet de :
* contrôler individuellement chaque axe
* créer plusieurs graphiques dans la même figure
* personnaliser chaque graphique séparément

:::tip Exemples
```py
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
x = [0, 1, 2, 3, 4]
y = [0, 2, 4, 6, 8]
ax.plot(x, y) # Tracé sur cet axe
```
<img src="/learning/libraries/matplotlib-figure-initialize-axes-7.png" style="display: block; margin: 0 auto;width: 50%; height: auto;">
:::