# Personnalisation des graphiques

Matplotlib offre un système de stylisation **très riche et très flexible** permettant de contrôler l’apparence : légendes, couleurs, styles de lignes, marqueurs, épaisseur des traits, etc.

## Legendes

Lorsque plusieurs courbes sont tracées sur un même graphique, il devient indispensable d’indiquer clairement ce que représente chaque ligne. C’est le rôle de la **légende**.

:::info
L’ajout d’une légende se fait en **deux étapes** :

1. Associer un `label` à chaque tracé
2. Appeler la méthode `legend()` sur l’objet `Axes`
:::

:::tip Exemple
```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 10)

fig, ax = plt.subplots()

ax.plot(x, x, label="x vs x")
ax.plot(x, x**2, label="x vs x²")

ax.legend()
plt.show()
```
Chaque couleur est maintenant associée à un intitulé clair.
:::

:::tip Position de la légende
Par défaut, Matplotlib choisit automatiquement la meilleure position (`loc='best'`). Il est cependant possible de la forcer.

Positions prédéfinies:
```python
ax.legend(loc='upper left')
ax.legend(loc='lower right')
ax.legend(loc='upper right')

```
| Code | Position    |
| ---- | ----------- |
| 0    | best        |
| 1    | upper right |
| 2    | upper left  |
| 3    | lower left  |
| 4    | lower right |
:::

## Couleurs et Styles

Une fois la légende en place, nous pouvons améliorer l’aspect visuel du graphique en personnalisant les **couleurs**, les **styles de lignes** et les **marqueurs**.

:::tip Couleurs des lignes
1. Couleurs nommées
```python
ax.plot(x, x, color='blue')
ax.plot(x, x+1, color='purple')
```
Quelques couleurs courantes : `blue`, `red`, `green`, `orange`, `purple`, `black`

2. Couleurs personnalisées (codes hexadécimaux)
```python
ax.plot(x, x, color='#2ecc71')  # vert
ax.plot(x, x+1, color='#f1c40f')  # jaune
```
:::

:::tip Épaisseur des lignes
L’épaisseur se règle avec `linewidth` ou son raccourci `lw` :
```python
ax.plot(x, x, lw=1)     # par défaut
ax.plot(x, x+1, lw=3)
ax.plot(x, x+2, lw=0.5)
```
:::

:::tip Styles de lignes
Les styles les plus courants :
| Code   | Description    |
| ------ | -------------- |
| `'-'`  | ligne continue |
| `'--'` | tirets         |
| `'-.'` | tiret-point    |
| `':'`  | pointillé      |
```python
ax.plot(x, x, ls='--', lw=2)
ax.plot(x, x+1, ls=':', lw=2)
```
:::

:::tip Marqueurs (points de données)
Les marqueurs représentent les points réels des données.
| Code  | Forme    |
| ----- | -------- |
| `'o'` | cercle   |
| `'s'` | carré    |
| `'+'` | plus     |
| `'^'` | triangle |
| `'*'` | étoile   |
```python
ax.plot(x, x, marker='o')
```
:::

## Fichier Python associé

:::details Style
<<< ./scripts/style.py
:::
