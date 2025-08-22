#  Introduction aux Vecteurs

## Qu’est-ce qu’un vecteur ?

Un **vecteur** est simplement une **liste de nombres** qui peut représenter :
- un déplacement dans l’espace
- des paramètres d’un modèle
- des caractéristiques d’un objet

:::info Exemples
- **En économie** : prix, coût, rendement d’un produit
- **En chimie** : proportions des composants d’un alliage
- **En physique** : \((3, 2)\) → déplacement de 3 pas vers la droite et 2 vers le haut.  
- **En science des données** : une maison peut être représentée par un vecteur :
  $$
  (120, 2, 1, 150000)
  $$
  → 120 m², 2 chambres, 1 salle de bain, prix 150000 €.  
:::

::: tip 👉 L’idée clé
Un vecteur est une **collection de valeurs organisées** qui décrit une position, un déplacement ou un ensemble de paramètres dans un espace. Les vecteurs sont donc des outils universels pour représenter et manipuler l’information.
:::

### Représentation

On peut le représenter de plusieurs façons :

- `géométriquement` : une flèche dans un plan ou un espace
<img src="/learning/mathematics/vector.svg" alt="vecteur" style="display: block; margin: 0 auto;width: 70px; height: auto;">
- `algébriquement` : une liste ordonnée de nombres
$$
v = \begin{bmatrix} v_1 \\ v_2 \\ \dots \\ v_n \end{bmatrix}
$$  

:::info Exemple : la loi normale et ses paramètres
En statistiques, la **loi normale (ou gaussienne)** est utilisée pour décrire des phénomènes naturels comme la **taille des individus dans une population**. 

Il s'agit d'un modèle pour une courbe en forme de cloche, qui ressemble à ceci :
<img src="/learning/mathematics/population-size-variation.png" alt="variation de la taille de la population" style="display: block; margin: 0 auto;width: 300px; height: auto;">

Sa formule est :
$$
f(x) = \frac{1}{\sigma \sqrt{2\pi}} \; e^{ - \frac{(x - \mu)^2}{2\sigma^2}}
$$
où :
- **$\mu$** : moyenne (centre de la distribution)  
- **$\sigma$** : écart-type (largeur de la distribution)  
- L’aire sous la courbe = **1** (100 % de la population)

Ces deux paramètres $(\mu, \sigma)$ peuvent être regroupés dans un vecteur :
$$
p =\begin{bmatrix}
\mu \\
\sigma
\end{bmatrix}
$$
👉 Ici, le vecteur $p$ ne décrit pas un déplacement physique mais un **ensemble de paramètres statistiques** qui définissent complètement une distribution.
:::

## Les vecteurs en machine learning

En apprentissage automatique, un vecteur sert à représenter :
- soit un **ensemble de caractéristiques** (exemple : âge, taille, poids d’un individu),
- soit un **ensemble de paramètres d’un modèle** (comme $\mu$ et $\sigma$ pour la gaussienne)

Chaque combinaison de paramètres correspond à un **point dans un espace abstrait**.  
Modifier ces paramètres revient à **se déplacer dans cet espace**, et ce déplacement est décrit par un **vecteur**.  

:::info Exemple appliqué à la loi normale
Imaginons que nous partions de :  
$$
(\mu, \sigma) = (1,75, 0,1)
$$  

et que nous ajustions légèrement les paramètres :  
$$
(\mu', \sigma') = (1,76, 0,12)
$$  

Le déplacement correspond au vecteur :  
$$
\Delta = (\mu' - \mu, \sigma' - \sigma) = (0,01, 0,02)
$$  
:::

::: tip 👉 L’idée clé
Les vecteurs permettent donc de **formaliser les ajustements** que l’on fait pour améliorer un modèle.
:::

## Ajuster un modèle aux données

En pratique, on veut trouver les paramètres $(\mu, \sigma)$ qui font que la courbe **colle le mieux aux données observées**.  
<img src="/learning/mathematics/normal-distribution.png" alt="Loi Gaussienne" style="display: block; margin: 0 auto;width: 300px; height: auto;">
- Si $\mu$ est trop grand ou trop petit → la courbe est décalée.  
- Si $\sigma$ est trop grand → la courbe est trop aplatie.  
- Si $\sigma$ est trop petit → la courbe est trop étroite.  

Pour évaluer la qualité de l’ajustement, on compare les données réelles $(y_i)$ aux valeurs prédites $(\hat{y}_i)$ :  

$$
\text{Erreur} = \sum_{i=1}^n (y_i - \hat{y}_i)^2
$$  

::: tip 🎯 Objectif
Trouver le vecteur de paramètres $p = (\mu, \sigma)$ qui **minimise l’erreur**.
:::

## Transition vers le calcul différentiel et l’algèbre linéaire

Maintenant que nous savons qu'un vecteur représente les **paramètres d’un modèle** et qu’ajuster ces paramètres, c’est **se déplacer dans un espace**, la prochaine question est :  
👉 **Comment savoir dans quelle direction déplacer notre vecteur de paramètres pour réduire l’erreur le plus vite possible ?**  
C’est ici que le **calcul différentiel (le gradient)** entre en jeu, et que l’**algèbre linéaire** devient indispensable pour manipuler efficacement ces espaces multidimensionnels.