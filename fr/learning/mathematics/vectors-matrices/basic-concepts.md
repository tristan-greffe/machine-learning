# Notions de base

## Qu’est-ce qu’un vecteur ?

Un **vecteur** est un objet mathématique qui possède deux propriétés fondamentales :

- Une **direction** (l’orientation dans l’espace).  
- Une **norme** (sa longueur, ou taille).

:::info
En machine learning, les vecteurs représentent souvent des données comme des embeddings, où la direction encode des similarités sémantiques (par exemple, dans les modèles de langage comme Word2Vec ou BERT), et la norme peut refléter l'importance ou la fréquence d'une caractéristique.
:::

## Représentation dans un système de coordonnées

En 2D, on choisit souvent deux vecteurs unitaires orthogonaux $\vec{i}$, $\vec{j}$ :

<img src="/learning/mathematics/vectors-matrices/coordinate-system.jpg" alt="vecteur" style="display: block; margin: 0 auto;width: 400px; height: auto;">

$$\vec{r} = a \cdot \vec{i} + b \cdot \vec{j}$$

- $a$ : composante sur l’axe $x$.  
- $b$ : composante sur l’axe $y$.  

En pratique, on écrit souvent le vecteur sous forme de **colonne** :  

$$\vec{r} = \begin{bmatrix} a \\ b \end{bmatrix}$$

:::tip 👉 Extension en dimensions supérieures
En $n$ dimensions, un vecteur est $\vec{r} = (r_1, r_2, \dots, r_n)$, courant en ML pour les embeddings de haute dimension (e.g., 768 pour BERT).
:::

:::info
En data science, cette représentation est utilisée pour les features dans les datasets, comme dans les algorithmes de clustering (e.g., k-means) où les points sont des vecteurs dans un espace multidimensionnel.
:::

## Norme (longueur) d’un vecteur

La **longueur** (ou norme) d’un vecteur se calcule avec le théorème de Pythagore :

$$\|\vec{r}\| = \sqrt{a^2 + b^2}$$

<img src="/learning/mathematics/vectors-matrices/vector-norm.png" alt="Norme d'un vecteur avec théorème de Pythagore" style="display: block; margin: 0 auto; width: 500px; height: auto;">

:::tip 👉 En dimensions supérieures
$$\|\vec{r}\| = \sqrt{r_1^2 + r_2^2 + \dots + r_n^2}$$
En ML, la norme L2 (euclidienne) mesure la "taille" d'un vecteur, utile pour la régularisation (e.g., Ridge regression) ou la normalisation des embeddings.
:::

:::info Exemple en 2D
$$\vec{r} = \begin{bmatrix} 3 \\ 4 \end{bmatrix}$$

$$\|\vec{r}\| = \sqrt{3^2 + 4^2} = 5$$
:::