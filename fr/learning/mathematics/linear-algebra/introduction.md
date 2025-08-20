# Introduction aux Vecteurs et à l’Algèbre Linéaire

L’algèbre linéaire commence par la maîtrise des `vecteurs`. Ils sont essentiels pour comprendre et résoudre une large variété de problèmes en mathématiques appliquées, en statistiques et en science des données.

## 1. Pourquoi les `vecteurs` ?

Un `vecteur` représente :

- Une direction et une norme dans l’espace physique
- Une liste de paramètres (par exemple, les caractéristiques d’un modèle)
- Un point dans un espace abstrait (statistique, économique, physique)

::: tip 👉 L’idée clé
un vecteur décrit un déplacement ou une collection de valeurs dans un espace donné
:::

## 2. Exemple : la distribution des tailles

Pour les effectifs d'une population, un modèle que nous pouvons utiliser pour prédire les fréquences est la distribution normale (ou gaussienne). Il s'agit d'un modèle pour une courbe en forme de cloche, qui ressemble à ceci,

![variation de la taille de la population](/learning/population-size-variation.svg)

L'équation un peu compliquée est la suivante,
$$
f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{\frac{-(x-\mu)^2}{2\sigma^2}}
$$


Considérons un exemple concret. Nous voulons modéliser la distribution des tailles d’une population. Cette distribution peut être approchée par une **loi normale** (ou gaussienne) donc 

dont la forme exacte est sans importance, si ce n'est qu'elle dépend de deux paramètres, la moyenne, $\mu$,  où la courbe est centrée, et l'écart type, $\sigma$, qui est la largeur caractéristique de la courbe en cloche (mesurée à partir de la moyenne).
Nous pouvons placer ces deux paramètres dans un vecteur :
$$
p =\begin{bmatrix}
\mu \\
\sigma
\end{bmatrix}
$$


- $\mu$ = moyenne (centre de la distribution)
- $\sigma$ = écart-type (largeur de la distribution)


## 3. Ajustement aux données (paramètres $\mu$ et $\sigma$)

Si nos données réelles ne correspondent pas parfaitement à notre estimation initiale de $\mu$ et $\sigma$, alors nous faisons des erreurs d’ajustement.

Une manière de mesurer la **qualité de l’ajustement** est de sommer les **carrés des différences** entre la fonction théorique et les données observées :

$$
Q(\mu, \sigma) = \sum_{i=1}^n \big( y_i - f(x_i; \mu, \sigma) \big)^2
$$

où $(x_i, y_i)$ sont les points de données.

Notre objectif est donc de **minimiser $Q(\mu, \sigma)$**.

---

## 4. Les vecteurs comme déplacements dans l’espace des paramètres

Lorsque nous ajustons $\mu$ et $\sigma$, nous explorons un **espace des paramètres**.  
Un déplacement dans cet espace peut être représenté par un vecteur :

$$
\vec{v} = (\Delta \mu, \Delta \sigma)
$$

Chaque mouvement correspond à un changement de paramètres.  
Ainsi, l’algèbre linéaire nous aide à comprendre :

- Comment se déplacer dans cet espace.  
- Quelle direction réduit le plus rapidement l’erreur $Q(\mu, \sigma)$.  

Ceci correspond à la **descente de gradient**.

---

## 5. Les vecteurs au-delà de la géométrie

Les vecteurs ne servent pas uniquement à représenter des positions dans l’espace physique :  

- En **économie**, un vecteur peut représenter le prix, le coût, et la performance d’un produit.  
- En **chimie**, un vecteur peut représenter les proportions des composants d’un alliage.  
- En **physique**, Einstein a formulé l’espace-temps comme un vecteur à 4 dimensions $(x, y, z, t)$.  
- En **apprentissage automatique**, un vecteur peut représenter les paramètres d’un modèle.

👉 Les vecteurs sont donc des outils universels pour représenter et manipuler l’information.

---

## 6. Optimisation et apprentissage automatique

En ajustant les paramètres d’un modèle (comme $\mu$ et $\sigma$), nous cherchons le point où l’erreur $Q(\mu, \sigma)$ est minimale.  
Cela revient à descendre dans un paysage de contours vers le **point le plus bas**.

- **Vecteurs = déplacements** dans cet espace.  
- **Calcul différentiel = outil** pour trouver la meilleure direction.  
- **Algèbre linéaire = langage** qui permet de représenter ces opérations efficacement.

---

## Conclusion

- Les vecteurs ne sont pas seulement des objets géométriques.  
- Ils représentent des déplacements ou des ensembles de paramètres.  
- Ils sont au cœur de l’optimisation, de l’algèbre linéaire et de l’apprentissage automatique.  

Comprendre les vecteurs est donc **la première étape fondamentale** pour maîtriser l’algèbre linéaire et la data science.