# Projection

## Intuition géométrique

Considérons deux vecteurs $\vec{r}$ et $\vec{s}$. On peut imaginer qu’une lumière tombe **perpendiculairement à $\vec{r}$**. L’ombre projetée de $\vec{s}$ sur $\vec{r}$ est ce qu’on appelle la **projection de $\vec{s}$ sur $\vec{r}$**.

Le produit scalaire encode exactement cette idée d’ombre ou de projection.

<img src="/learning/mathematics/vectors/vector-projection.png" alt="Projection scalaire et vectorielle" style="display: block; margin: 0 auto;width: 400px; height: auto;">

:::details Développement mathématique
On a vu que :

$$\vec{r} \cdot \vec{s} = \|\vec{r}\| \|\vec{s}\| \cos(\theta)$$

où $\theta$ est l’angle entre les deux vecteurs.

Dans un triangle rectangle formé par $\vec{s}$, l’angle $\theta$, et la perpendiculaire à $\vec{r}$ :
- $\cos(\theta)$ est le rapport entre le **côté adjacent** (l’ombre de $\vec{s}$ sur $\vec{r}$) et l’**hypoténuse** ($\|\vec{s}\|$).

Donc :

$$\|\vec{s}\|\cos(\theta)$$

est la **longueur de la projection** de $\vec{s}$ sur $\vec{r}$.
:::

## Projection scalaire

La **projection scalaire** de $\vec{s}$ sur $\vec{r}$ est donnée par :

$$\text{proj}_{\vec{r}}(\vec{s}) = \frac{\vec{r}\cdot\vec{s}}{\|\vec{r}\|}$$

- C’est un **nombre** (longueur, positive ou négative selon le sens).
- Elle représente **la taille de l’ombre de $\vec{s}$ sur $\vec{r}$**.

Cas particulier :
- Si $\vec{s} \perp \vec{r}$ : $\cos(\theta) = 0$, donc projection = 0.
- Si $\vec{s}$ est aligné avec $\vec{r}$ : projection = $\|\vec{s}\|$.
- Si $\vec{s}$ est opposé à $\vec{r}$ : projection = $-\|\vec{s}\|$.

:::info Exemple
En ML, la projection scalaire mesure combien une feature contribue à une direction principale (e.g., en PCA, les projections sur les composantes principales).
:::

## Projection vectorielle

La **projection vectorielle** de $\vec{s}$ sur $\vec{r}$ est le vecteur dans la direction de $\vec{r}$ qui correspond à cette projection :

$$\vec{\text{proj}}_{\vec{r}}(\vec{s}) = \frac{\vec{r}\cdot\vec{s}}{\|\vec{r}\|^2}\vec{r}$$

- C’est un **vecteur**, aligné avec $\vec{r}$.
- Sa norme est égale à la projection scalaire.

On peut voir cela comme :

$$\vec{\text{proj}}_{\vec{r}}(\vec{s}) = \big(\text{projection scalaire}\big) \times \vec{u}_r$$

où $\vec{u}_r = \frac{\vec{r}}{\|\vec{r}\|}$ est le vecteur unitaire de la direction de $\vec{r}$.

:::info Exemple en ML
En réduction de dimensionnalité comme PCA, les projections vectorielles transforment les données en un espace de plus faible dimension tout en conservant la variance maximale.
:::

## Résumé

| **Aspect**                | **Projection scalaire**                          | **Projection vectorielle**                       |
|---------------------------|--------------------------------------------------|-------------------------------------------------|
| **Nature du résultat**    | Un **nombre** (longueur de l'ombre).             | Un **vecteur** (l'ombre elle-même).             |
| **Formule**               | $\frac{\vec{r} \cdot \vec{s}}{\|\vec{r}\|}$     | $\frac{\vec{r} \cdot \vec{s}}{\|\vec{r}\|^2} \vec{r}$ |
| **Interprétation**        | Mesure la **taille** de la projection.           | Donne le **vecteur** dans la direction de $\vec{r}$. |
| **Utilisation en ML**     | Mesure la contribution d'une feature (e.g., PCA). | Transforme les données dans un espace réduit.   |

## Lien avec le Machine Learning
- **Projection scalaire** : Utilisée pour quantifier l'importance d'une feature dans une direction donnée, comme dans la similarité cosinus pour comparer des embeddings (e.g., dans les systèmes de recommandation ou la recherche sémantique).
- **Projection vectorielle** : Transforme les données dans un espace réduit, comme dans PCA ou dans les mécanismes d'attention des transformers, où les projections vectorielles capturent les relations entre les tokens.

:::tip 👉 Astuce
La projection scalaire est un intermédiaire pour calculer la projection vectorielle : on calcule d'abord la longueur (scalaire), puis on l'applique à la direction de $\vec{r}$ pour obtenir le vecteur.
:::
