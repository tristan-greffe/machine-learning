# Produit scalaire (`dot product`)

Le **produit scalaire** est une opération entre deux vecteurs qui associe un **nombre** à leur relation. C’est une façon de mesurer **dans quelle mesure deux vecteurs pointent dans la même direction**.

- Si les vecteurs pointent **dans la même direction**, le produit scalaire est **grand et positif**.  
- S’ils sont **orthogonaux (90°)**, le produit scalaire vaut **0**.  
- S’ils pointent **dans des directions opposées**, il est **négatif**.

<img src="/learning/mathematics/vectors/dot-product.png" alt="vecteur" style="display: block; margin: 0 auto;width: 400px; height: auto;">

:::tip 👉 Intuition
Le produit scalaire mesure **l’alignement** entre deux vecteurs, clé en ML pour la similarité cosinus dans les systèmes de recommandation ou la recherche sémantique.
:::

## Définition mathématique

Le **produit scalaire** de deux vecteurs en dimension $n$ $\vec{r} = (r_1, r_2, \dots, r_n)$ et $\vec{s} = (s_1, s_2, \dots, s_n)$ est :

$$\vec{r} \cdot \vec{s} = r_1 s_1 + r_2 s_2 + \dots + r_n s_n$$

<img src="/learning/mathematics/vectors/dot-product-2d.png" alt="vecteur" style="display: block; margin: 0 auto;width: 400px; height: auto;">

:::tip 📌
Ce résultat est **un nombre réel** (un *scalaire*), contrairement à l’addition de vecteurs qui donne un vecteur.
:::

:::info Exemple en 2D
$$\vec{r} = \begin{bmatrix} 3 \\ -1 \end{bmatrix}, \quad \vec{s} = \begin{bmatrix} 2 \\ 2 \end{bmatrix}$$

$$\vec{r} \cdot \vec{s} = 3 \times 2 + (-1) \times 2 = 6 - 2 = 4$$
:::

:::details Développement de la formule géométrique
Une autre définition relie le produit scalaire à l’angle entre deux vecteurs :

$$\vec{r} \cdot \vec{s} = \|\vec{r}\| \, \|\vec{s}\| \cos(\theta)$$

- $\|\vec{r}\|$ = longueur du vecteur $\vec{r}$.
- $\|\vec{s}\|$ = longueur du vecteur $\vec{s}$.
- $\theta$ = angle entre $\vec{r}$ et $\vec{s}$.

Le produit scalaire est grand si les vecteurs sont proches en direction, nul s’ils sont perpendiculaires, et négatif s’ils pointent en sens opposés.
:::

## Dérivation à partir de la règle du cosinus

En géométrie, pour un triangle avec côtés $a$, $b$, $c$ et angle $\theta$ entre $a$ et $b$ :

$$c^2 = a^2 + b^2 - 2ab \cos(\theta)$$

C’est la **règle du cosinus**, que l’on peut traduire en langage vectoriel.

Soit deux vecteurs $\vec{r}$ et $\vec{s}$. Le troisième côté du triangle est donné par :

$$\vec{r} - \vec{s}$$

La norme au carré de ce vecteur est donc :

$$\|\vec{r} - \vec{s}\|^2$$

D’après la règle du cosinus :

$$\|\vec{r}\|^2 + \|\vec{s}\|^2 - 2 \|\vec{r}\| \|\vec{s}\| \cos(\theta)$$

On peut aussi développer directement avec le **produit scalaire** :

$$\|\vec{r} - \vec{s}\|^2 = (\vec{r} - \vec{s}) \cdot (\vec{r} - \vec{s})$$

Développons :

$$= \vec{r}\cdot\vec{r} - 2 \vec{r}\cdot\vec{s} + \vec{s}\cdot\vec{s}$$

Or :

- $\vec{r}\cdot\vec{r} = \|\vec{r}\|^2$.  
- $\vec{s}\cdot\vec{s} = \|\vec{s}\|^2$.

Donc :

$$\|\vec{r} - \vec{s}\|^2 = \|\vec{r}\|^2 + \|\vec{s}\|^2 - 2 (\vec{r}\cdot\vec{s})$$

En comparant avec la **règle du cosinus** :

$$\|\vec{r} - \vec{s}\|^2 = \|\vec{r}\|^2 + \|\vec{s}\|^2 - 2 \|\vec{r}\| \|\vec{s}\| \cos(\theta)$$

On en déduit la relation fondamentale :

$$\vec{r} \cdot \vec{s} = \|\vec{r}\| \|\vec{s}\| \cos(\theta)$$

:::details Interprétation géométrique
Le produit scalaire mesure **l’alignement** entre deux vecteurs.

- Si $\theta = 0^\circ$ (même direction) :  
  $$\cos(0) = 1 \quad \Rightarrow \quad \vec{r}\cdot\vec{s} = \|\vec{r}\|\|\vec{s}\|$$  
  Produit scalaire **positif et maximal**.

- Si $\theta = 90^\circ$ (vecteurs orthogonaux) :  
  $$\cos(90) = 0 \quad \Rightarrow \quad \vec{r}\cdot\vec{s} = 0$$  
  Vecteurs indépendants.

- Si $\theta = 180^\circ$ (directions opposées) :  
  $$\cos(180) = -1 \quad \Rightarrow \quad \vec{r}\cdot\vec{s} = -\|\vec{r}\|\|\vec{s}\|$$  
  Produit scalaire **négatif**.
:::

:::info Résumé visuel
- Produit scalaire > 0 : vecteurs dans la **même direction**.  
- Produit scalaire = 0 : vecteurs **orthogonaux** (indépendants).  
- Produit scalaire < 0 : vecteurs dans des **directions opposées**.
:::

## Propriétés fondamentales

Voici les principales propriétés du produit scalaire :

| Propriété | Formulation | Interprétation |
|-----------|-------------|----------------|
| **Commutativité** | $\vec{r} \cdot \vec{s} = \vec{s} \cdot \vec{r}$ | L’ordre ne change rien. |
| **Linéarité (distributivité)** | $\vec{r} \cdot (\vec{s} + \vec{t}) = \vec{r} \cdot \vec{s} + \vec{r} \cdot \vec{t}$ | On peut “distribuer” le produit scalaire sur une somme. |
| **Homogénéité (associativité scalaire)** | $(a \vec{r}) \cdot \vec{s} = a (\vec{r} \cdot \vec{s})$ | Un facteur scalaire sort du produit. |
| **Norme** | $\vec{r} \cdot \vec{r} = \|\vec{r}\|^2$ | Le produit scalaire d’un vecteur par lui-même donne le **carré de sa longueur**. |

:::info
En ML, ces propriétés sont essentielles pour les calculs efficaces dans les réseaux de neurones, où le produit scalaire apparaît dans les couches fully-connected.
:::


## Pourquoi c’est important en Machine Learning ?

- La **norme** d’un vecteur mesure la taille (ou importance) d’un paramètre, d’un poids ou d’une donnée, comme dans la régularisation L2 pour éviter le surapprentissage.  
- Le **produit scalaire** permet de mesurer la **similarité** entre deux vecteurs, base de la similarité cosinus :

$$\cos(\theta) = \frac{\vec{r} \cdot \vec{s}}{\|\vec{r}\| \|\vec{s}\|}$$

En IA, c’est central pour :

- Les systèmes de recommandation (e.g., Netflix utilise la similarité cosinus sur les embeddings d'utilisateurs et de films).  
- La recherche sémantique (e.g., dans les moteurs comme Elasticsearch avec embeddings BERT).  
- Le clustering (e.g., k-means utilise des distances basées sur normes).  
- Les transformers (attention mechanism utilise des produits scalaires pour peser les relations entre tokens).

:::info Exemple concret en ML
En NLP, deux embeddings de mots (e.g., "roi" et "reine") ont un produit scalaire élevé si similaires, permettant des analogies comme "roi - homme + femme ≈ reine".  
En data science, la similarité cosinus compare des documents ou des images pour la détection de similarités.
:::