# Base Vectorielle

## Qu’est-ce qu’une base ?

Une **base** est un ensemble de vecteurs qui permet de décrire **tous les vecteurs** d’un espace vectoriel en utilisant des **combinaisons linéaires** de ces vecteurs. En d'autres termes, une base est comme un "système de coordonnées" pour un espace, permettant de représenter n'importe quel point ou vecteur. Une base fournit un ensemble minimal de directions indépendantes pour naviguer dans l'espace.

<img src="/learning/mathematics/vectors-matrices/vector-space-basis.png" alt="Illustration d'une base vectorielle" style="display: block; margin: 0 auto; width: 300px; height: auto;">

:::tip 👉 Intuition
Une base est comme un ensemble minimal de "directions" qui permet de naviguer dans tout l’espace. En ML, changer de base peut simplifier les calculs, comme dans la réduction de dimensionnalité où l'on projette les données sur une base qui capture l'essentiel de l'information.
:::

:::info
En machine learning, les bases sont essentielles pour comprendre les transformations de données, comme dans l'**analyse en composantes principales (PCA)** où une nouvelle base est choisie pour maximiser la variance des données, ou dans les réseaux de neurones où les couches apprennent des bases qui extraient des caractéristiques pertinentes (features) des données d'entrée.
:::

### Définition mathématique
Un ensemble de vecteurs $\{\vec{b_1}, \vec{b_2}, \dots, \vec{b_n}\}$ forme une **base** d’un espace vectoriel si :
1. Les vecteurs sont **linéairement indépendants** :
   $$a_1 \vec{b_1} + a_2 \vec{b_2} + \dots + a_n \vec{b_n} = \vec{0} \quad \Rightarrow \quad a_1 = a_2 = \dots = a_n = 0$$
2. Les vecteurs **engendrent l’espace** (ou le spannent), c’est-à-dire que tout vecteur $\vec{v}$ de l’espace peut s’écrire comme :
   $$\vec{v} = c_1 \vec{b_1} + c_2 \vec{b_2} + \dots + c_n \vec{b_n}$$

Le nombre $n$ de vecteurs dans la base correspond à la **dimension** de l’espace.

:::details Développement : Dimension et bases multiples
Tous les espaces vectoriels de dimension finie ont plusieurs bases possibles, mais toutes les bases ont le même nombre d'éléments (théorème de la dimension). Par exemple, en $\mathbb{R}^2$, la base standard $\{\vec{i}, \vec{j}\}$ et une base rotée sont toutes deux valides, mais la dimension reste 2. En ML, cela permet de choisir une base qui aligne les données pour mieux révéler des patterns, comme dans PCA où les vecteurs propres forment une base qui décorrèle les variables.
:::

:::info Exemples en dimensions basses
- En **1D** (une ligne) : Un seul vecteur non nul $\vec{b_1}$ suffit. Tout vecteur sur la ligne est un multiple de $\vec{b_1}$.
- En **2D** (un plan) : Deux vecteurs indépendants $\vec{b_1}, \vec{b_2}$. Tout vecteur dans le plan s'écrit $a_1 \vec{b_1} + a_2 \vec{b_2}$.
- En **3D** : Trois vecteurs indépendants $\vec{b_1}, \vec{b_2}, \vec{b_3}$. Si on ajoute un $\vec{b_4}$ non dans le plan des trois premiers, on passe à 4D.
En ML, les données en haute dimension (e.g., images avec des milliers de pixels) sont souvent projetées sur une base de plus faible dimension pour réduire le bruit et la complexité.
:::

## Indépendance linéaire

Un ensemble de vecteurs est **linéairement indépendant** si aucun des vecteurs ne peut être exprimé comme une combinaison linéaire des autres. Autrement dit, aucun vecteur n’est "redondant". Si un vecteur est une combinaison des autres, il n'apporte pas de nouvelle direction.

:::info Exemple
- Si $\vec{b_2} = 2 \vec{b_1}$, alors $\vec{b_2}$ est dans la même direction que $\vec{b_1}$ et n’apporte rien de nouveau → **dépendance linéaire**.
- Si $\vec{b_2}$ n’est pas un multiple de $\vec{b_1}$ (par exemple, ils forment un angle non nul), alors ils sont **indépendants** et peuvent engendrer un plan (espace 2D).
En ML, l'indépendance linéaire aide à détecter les features redondantes dans un dataset (e.g., via corrélation ou PCA).
:::

:::details Vérification de l’indépendance linéaire
Pour vérifier si des vecteurs sont linéairement indépendants, on peut :
1. Former une matrice avec ces vecteurs comme colonnes.
2. Calculer son **déterminant** (non nul = indépendance) ou vérifier son **rang** (égal au nombre de vecteurs = indépendance).
   - En 2D, pour $\vec{b_1} = \begin{bmatrix} x_1 \\ y_1 \end{bmatrix}$, $\vec{b_2} = \begin{bmatrix} x_2 \\ y_2 \end{bmatrix}$, le déterminant de la matrice $\begin{bmatrix} x_1 & x_2 \\ y_1 & y_2 \end{bmatrix}$ est $x_1 y_2 - x_2 y_1$. S’il est non nul, les vecteurs sont indépendants.
En data science, un rang inférieur indique des dépendances, utile pour la sélection de features.
:::

:::details Pourquoi le déterminant vérifie-t-il l’indépendance linéaire ?
Le déterminant d’une matrice carrée formée par des vecteurs est un outil puissant pour vérifier leur indépendance linéaire. Voici pourquoi, étape par étape :

### Définition et lien avec l’indépendance linéaire
Un ensemble de $n$ vecteurs $\{\vec{v_1}, \vec{v_2}, \dots, \vec{v_n}\}$ dans $\mathbb{R}^n$ est **linéairement indépendant** si l’équation suivante n’a que la solution triviale (tous les coefficients nuls) :
$$c_1 \vec{v_1} + c_2 \vec{v_2} + \dots + c_n \vec{v_n} = \vec{0} \quad \Rightarrow \quad c_1 = c_2 = \dots = c_n = 0.$$

Formons la matrice $A = [\vec{v_1} \, \vec{v_2} \, \dots \, \vec{v_n}]$, où chaque $\vec{v_i}$ est une colonne. L’équation ci-dessus s’écrit sous forme matricielle :
$$A \vec{c} = \vec{0},$$
où $\vec{c} = \begin{bmatrix} c_1 \\ c_2 \\ \vdots \\ c_n \end{bmatrix}$. Les vecteurs sont indépendants si la seule solution est $\vec{c} = \vec{0}$.

### Rôle du déterminant
Si $A$ est une matrice carrée ($n \times n$), son déterminant $\det(A)$ indique si $A$ est **inversible** :
- **Si $\det(A) \neq 0$** : $A$ est inversible, et le système $A \vec{c} = \vec{0}$ n’a que la solution triviale $\vec{c} = \vec{0}$. Les vecteurs sont donc **indépendants**.
- **Si $\det(A) = 0$** : $A$ n’est pas inversible, et le système a des solutions non triviales (des $\vec{c} \neq \vec{0}$). Cela signifie qu’au moins un vecteur est une combinaison linéaire des autres, donc les vecteurs sont **dépendants**.

### Interprétation géométrique
Le déterminant a une signification géométrique :
- En 2D, pour deux vecteurs, $\det(A)$ représente l’aire du parallélogramme formé par ces vecteurs. Si $\det(A) = 0$, l’aire est nulle, ce qui signifie que les vecteurs sont alignés (colinéaires), donc dépendants.
- En 3D, pour trois vecteurs, $\det(A)$ représente le volume du parallélépipède. Si $\det(A) = 0$, le volume est nul, ce qui indique que les vecteurs sont coplanaires (ou alignés), donc dépendants.
En général, un déterminant nul signifie que les vecteurs ne couvrent pas tout l’espace $\mathbb{R}^n$, mais un sous-espace de dimension inférieure.

### Application à l’exemple du cours
Reprenons les vecteurs $\vec{a} = \begin{bmatrix} 1 \\ 2 \\ -1 \end{bmatrix}$, $\vec{b} = \begin{bmatrix} 3 \\ -4 \\ 5 \end{bmatrix}$, $\vec{c} = \begin{bmatrix} 1 \\ -8 \\ 7 \end{bmatrix}$. Formons la matrice :
$$A = \begin{bmatrix} 1 & 3 & 1 \\ 2 & -4 & -8 \\ -1 & 5 & 7 \end{bmatrix}$$

Calculons le déterminant :
$$\det(A) = 1 \cdot \det\begin{bmatrix} -4 & -8 \\ 5 & 7 \end{bmatrix} - 3 \cdot \det\begin{bmatrix} 2 & -8 \\ -1 & 7 \end{bmatrix} + 1 \cdot \det\begin{bmatrix} 2 & -4 \\ -1 & 5 \end{bmatrix}$$

- Premier mineur : $(-4)(7) - (-8)(5) = -28 + 40 = 12$
- Deuxième mineur : $(2)(7) - (-8)(-1) = 14 - 8 = 6$
- Troisième mineur : $(2)(5) - (-4)(-1) = 10 - 4 = 6$

Ainsi :
$$\det(A) = 1 \cdot 12 - 3 \cdot 6 + 1 \cdot 6 = 12 - 18 + 6 = 0$$

Puisque $\det(A) = 0$, les vecteurs sont **dépendants**. Géométriquement, ils sont coplanaires dans $\mathbb{R}^3$, ne formant pas une base.

### Cas non carré
Si le nombre de vecteurs $n$ diffère de la dimension $m$ (par exemple, 4 vecteurs dans $\mathbb{R}^3$), la matrice n’est pas carrée, et le déterminant n’est pas défini. Dans ce cas, on utilise le **rang** de la matrice (via l’élimination de Gauss) pour vérifier l’indépendance.

### En machine learning
Le déterminant est utilisé pour détecter les redondances dans les features (si $\det = 0$, il y a corrélation). Dans PCA, un déterminant non nul des vecteurs propres garantit une base valide pour la projection des données.

### Résumé
Le déterminant teste l’indépendance linéaire car il mesure si les vecteurs couvrent pleinement l’espace. S’il est nul, les vecteurs sont confinés à un sous-espace, donc dépendants. S’il est non nul, ils forment une base.
:::

:::info Exemple en 2D
Considérons :
- $\vec{b_1} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$, $\vec{b_2} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$ (base canonique 2D).
- Ces vecteurs sont linéairement indépendants, car $a_1 \begin{bmatrix} 1 \\ 0 \end{bmatrix} + a_2 \begin{bmatrix} 0 \\ 1 \end{bmatrix} = \begin{bmatrix} a_1 \\ a_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$ implique $a_1 = a_2 = 0$.
- Tout vecteur $\vec{v} = \begin{bmatrix} x \\ y \end{bmatrix}$ peut s’écrire : $\vec{v} = x \vec{b_1} + y \vec{b_2}$.
:::

:::details Exemple supplémentaire : Vérification d'indépendance linéaire en 3D
Les vecteurs suivants sont-ils linéairement indépendants ? 

$\vec{a} = \begin{bmatrix} 1 \\ 2 \\ -1 \end{bmatrix}$, $\vec{b} = \begin{bmatrix} 3 \\ -4 \\ 5 \end{bmatrix}$ et $\vec{c} = \begin{bmatrix} 1 \\ -8 \\ 7 \end{bmatrix}$.

Pour vérifier, on forme la matrice $M$ avec ces vecteurs comme colonnes :

$$M = \begin{bmatrix} 1 & 3 & 1 \\ 2 & -4 & -8 \\ -1 & 5 & 7 \end{bmatrix}$$

On calcule le déterminant de $M$. Si $\det(M) \neq 0$, les vecteurs sont indépendants ; sinon, ils sont dépendants.

Calcul du déterminant étape par étape (utilisant la formule pour une matrice 3x3) :

$$\det(M) = 1 \cdot \det\begin{bmatrix} -4 & -8 \\ 5 & 7 \end{bmatrix} - 3 \cdot \det\begin{bmatrix} 2 & -8 \\ -1 & 7 \end{bmatrix} + 1 \cdot \det\begin{bmatrix} 2 & -4 \\ -1 & 5 \end{bmatrix}$$

- Premier mineur : $\det\begin{bmatrix} -4 & -8 \\ 5 & 7 \end{bmatrix} = (-4)(7) - (-8)(5) = -28 + 40 = 12$
- Deuxième mineur : $\det\begin{bmatrix} 2 & -8 \\ -1 & 7 \end{bmatrix} = (2)(7) - (-8)(-1) = 14 - 8 = 6$
- Troisième mineur : $\det\begin{bmatrix} 2 & -4 \\ -1 & 5 \end{bmatrix} = (2)(5) - (-4)(-1) = 10 - 4 = 6$

Maintenant, assembler :

$$\det(M) = 1 \cdot 12 - 3 \cdot 6 + 1 \cdot 6 = 12 - 18 + 6 = 0$$

Puisque $\det(M) = 0$, les vecteurs sont linéairement **dépendants**. Cela signifie qu'au moins un vecteur peut s'exprimer comme une combinaison linéaire des autres (par exemple, on peut résoudre pour trouver des coefficients non triviaux tels que $\vec{c} = -2\vec{a} + \vec{b}$, mais la vérification du déterminant suffit pour conclure).
:::

## Engendrement de l'espace (Span)

Un ensemble de vecteurs **engendre** l'espace s'il permet d'atteindre tout vecteur via des combinaisons linéaires. La base est l'ensemble minimal (indépendant) qui engendre l'espace.

:::details Interprétation
Si les vecteurs n'engendrent pas l'espace, ils ne couvrent qu'un sous-espace (e.g., deux vecteurs alignés engendrent une ligne, pas un plan). En ML, le span des données peut révéler des sous-espaces de haute variance, comme dans PCA où l'on identifie les directions principales.
:::

:::info Exemple en ML : Réduction de dimensionnalité
Supposez des points de données alignés approximativement sur une ligne dans $\mathbb{R}^2$. La base optimale serait un vecteur le long de cette ligne (direction de variance maximale) et un perpendiculaire (bruit). Projeter sur la première direction réduit à 1D tout en conservant l'information principale, comme dans PCA.
:::

<img src="/learning/mathematics/vectors-matrices/pca-fish.png" alt="Illustration de PCA : projection sur axes principaux" style="display: block; margin: 0 auto; width: 500px; height: auto;">

## Bases spéciales

### Base orthonormée
Une base est **orthonormée** si :
- Les vecteurs sont **orthogonaux** deux à deux : $\vec{b_i} \cdot \vec{b_j} = 0$ si $i \neq j$.
- Les vecteurs sont **unitaires** : $\|\vec{b_i}\| = 1$.

<img src="/learning/mathematics/vectors-matrices/orthogonal-basis.png" alt="Base orthonormée" style="display: block; margin: 0 auto; width: 500px; height: auto;">

:::tip 👉 Avantage
Les bases orthonormées simplifient les calculs en ML, notamment dans les projections (comme dans PCA) ou les transformations (e.g., matrices de rotation dans les réseaux de neurones). Elles ne doivent pas nécessairement être unitaires ou orthogonales, mais c'est plus facile si elles le sont.
:::

:::info Exemple de base orthonormée
La base canonique en 2D :
- $\vec{b_1} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$, $\vec{b_2} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$.
- Vérification :
  - Orthogonalité : $\vec{b_1} \cdot \vec{b_2} = 1 \cdot 0 + 0 \cdot 1 = 0$.
  - Unitaire : $\|\vec{b_1}\| = \sqrt{1^2 + 0^2} = 1$, $\|\vec{b_2}\| = \sqrt{0^2 + 1^2} = 1$.
:::

### Base quelconque
Une base quelconque n’est pas nécessairement orthonormée. Les vecteurs peuvent avoir des longueurs différentes et ne pas être orthogonaux.

:::tip 👉 Note
Les bases non orthonormées compliquent les calculs, car les projections nécessitent des matrices de changement de base. En ML, on préfère souvent orthonormer les bases (e.g., via la décomposition QR ou SVD) pour simplifier les opérations.
:::

## Changement de base

Le **changement de base** consiste à réécrire un vecteur exprimé dans une base $\{\vec{b_1}, \vec{b_2}, \dots, \vec{b_n}\}$ dans une autre base $\{\vec{c_1}, \vec{c_2}, \dots, \vec{c_n}\}$. Cela revient à transformer les coordonnées du vecteur, en préservant les propriétés linéaires : l'espace reste une grille uniformément espacée, sans courbure.

<img src="/learning/mathematics/vectors-matrices/vector-base-change.gif" alt="changement de base vectorielle" style="display: block; margin: 0 auto; width: 500px; height: auto;">

### Principe
Soit un vecteur $\vec{v}$ exprimé dans une base $B = \{\vec{b_1}, \vec{b_2}\}$ :
$$\vec{v} = x_1 \vec{b_1} + x_2 \vec{b_2}$$
On veut ses coordonnées dans une nouvelle base $C = \{\vec{c_1}, \vec{c_2}\}$ :
$$\vec{v} = y_1 \vec{c_1} + y_2 \vec{c_2}$$

La transformation est effectuée à l’aide d’une **matrice de changement de base** $P$, où les colonnes de $P$ sont les vecteurs de la base $C$ exprimés dans la base $B$. Les nouvelles coordonnées sont :
$$\begin{bmatrix} y_1 \\ y_2 \end{bmatrix} = P^{-1} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}$$

Si les bases ne sont pas orthogonales, on ne peut pas utiliser seulement le produit scalaire ; il faut des matrices.

:::details Développement mathématique
Si $\vec{c_1} = p_{11} \vec{b_1} + p_{21} \vec{b_2}$ et $\vec{c_2} = p_{12} \vec{b_1} + p_{22} \vec{b_2}$, la matrice $P$ est :
$$P = \begin{bmatrix} p_{11} & p_{12} \\ p_{21} & p_{22} \end{bmatrix}$$
Alors, pour passer de la base $B$ à $C$, on utilise $P^{-1}$. En ML, les changements de base sont utilisés dans les transformations linéaires (e.g., rotation des données dans PCA ou embeddings dans les transformers).
:::

:::info Exemple en 2D
Soit une base $B = \left\{ \begin{bmatrix} 1 \\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\ 1 \end{bmatrix} \right\}$ et une base $C = \left\{ \begin{bmatrix} 1 \\ 1 \end{bmatrix}, \begin{bmatrix} -1 \\ 1 \end{bmatrix} \right\}$. Un vecteur $\vec{v} = \begin{bmatrix} 3 \\ 2 \end{bmatrix}$ dans $B$ a pour coordonnées :
- Dans $B$ : $\vec{v} = 3 \vec{b_1} + 2 \vec{b_2}$.
- Pour trouver les coordonnées dans $C$, on résout $\vec{v} = y_1 \vec{c_1} + y_2 \vec{c_2}$ :
  $$3 \begin{bmatrix} 1 \\ 0 \end{bmatrix} + 2 \begin{bmatrix} 0 \\ 1 \end{bmatrix} = y_1 \begin{bmatrix} 1 \\ 1 \end{bmatrix} + y_2 \begin{bmatrix} -1 \\ 1 \end{bmatrix}$$
  Cela donne le système :
  - $y_1 - y_2 = 3$
  - $y_1 + y_2 = 2$
  Solution : $y_1 = 2.5$, $y_2 = -0.5$. Donc, $\vec{v} = 2.5 \vec{c_1} - 0.5 \vec{c_2}$.
:::

:::details Exemple supplémentaire : Changement de base en 3D avec base orthogonale
Étant donné les vecteurs $\vec{v} = \begin{bmatrix} -4 \\ -3 \\ 8 \end{bmatrix}$, $\vec{b_1} = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}$, $\vec{b_2} = \begin{bmatrix} -2 \\ 1 \\ 0 \end{bmatrix}$ et $\vec{b_3} = \begin{bmatrix} -3 \\ -6 \\ 5 \end{bmatrix}$, tous écrits dans la base standard, que représente $\vec{v}$ dans la base définie par $\vec{b_1}$, $\vec{b_2}$ et $\vec{b_3}$ ? On sait que $\vec{b_1}$, $\vec{b_2}$ et $\vec{b_3}$ sont orthogonaux les uns par rapport aux autres.

Puisque la base $\{\vec{b_1}, \vec{b_2}, \vec{b_3}\}$ est orthogonale (mais pas nécessairement orthonormée, car les normes ne sont pas forcément 1), on peut trouver les coordonnées $c_1, c_2, c_3$ telles que $\vec{v} = c_1 \vec{b_1} + c_2 \vec{b_2} + c_3 \vec{b_3}$ en utilisant la formule de projection pour bases orthogonales : $c_i = \frac{\vec{v} \cdot \vec{b_i}}{\vec{b_i} \cdot \vec{b_i}}$.

Détaillons les étapes :

1. Vérifions d'abord l'orthogonalité (bien que donné, pour complétude) :
   - $\vec{b_1} \cdot \vec{b_2} = 1 \cdot (-2) + 2 \cdot 1 + 3 \cdot 0 = -2 + 2 + 0 = 0$
   - $\vec{b_1} \cdot \vec{b_3} = 1 \cdot (-3) + 2 \cdot (-6) + 3 \cdot 5 = -3 -12 + 15 = 0$
   - $\vec{b_2} \cdot \vec{b_3} = (-2) \cdot (-3) + 1 \cdot (-6) + 0 \cdot 5 = 6 -6 + 0 = 0$
   Oui, orthogonaux.

2. Pour trouver $c_1$ : On multiplie l'équation $\vec{v} = c_1 \vec{b_1} + c_2 \vec{b_2} + c_3 \vec{b_3}$ par $\vec{b_1}$ (produit scalaire des deux côtés) :
   $$\vec{v} \cdot \vec{b_1} = c_1 (\vec{b_1} \cdot \vec{b_1}) + c_2 (\vec{b_2} \cdot \vec{b_1}) + c_3 (\vec{b_3} \cdot \vec{b_1})$$
   Puisque orthogonaux, $\vec{b_2} \cdot \vec{b_1} = 0$ et $\vec{b_3} \cdot \vec{b_1} = 0$, donc :
   $$\vec{v} \cdot \vec{b_1} = c_1 (\vec{b_1} \cdot \vec{b_1})$$
   $$c_1 = \frac{\vec{v} \cdot \vec{b_1}}{\vec{b_1} \cdot \vec{b_1}}$$
   Calcul : $\vec{v} \cdot \vec{b_1} = (-4)(1) + (-3)(2) + 8(3) = -4 -6 + 24 = 14$
   $\vec{b_1} \cdot \vec{b_1} = 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14$
   $c_1 = 14 / 14 = 1$

3. De même pour $c_2$ : Multipliez par $\vec{b_2}$ :
   $$\vec{v} \cdot \vec{b_2} = c_2 (\vec{b_2} \cdot \vec{b_2})$$ (termes croisés nuls)
   $c_2 = \frac{\vec{v} \cdot \vec{b_2}}{\vec{b_2} \cdot \vec{b_2}}$
   $\vec{v} \cdot \vec{b_2} = (-4)(-2) + (-3)(1) + 8(0) = 8 -3 + 0 = 5$
   $\vec{b_2} \cdot \vec{b_2} = (-2)^2 + 1^2 + 0^2 = 4 + 1 + 0 = 5$
   $c_2 = 5 / 5 = 1$

4. Pour $c_3$ : Multipliez par $\vec{b_3}$ :
   $$\vec{v} \cdot \vec{b_3} = c_3 (\vec{b_3} \cdot \vec{b_3})$$
   $c_3 = \frac{\vec{v} \cdot \vec{b_3}}{\vec{b_3} \cdot \vec{b_3}}$
   $\vec{v} \cdot \vec{b_3} = (-4)(-3) + (-3)(-6) + 8(5) = 12 + 18 + 40 = 70$
   $\vec{b_3} \cdot \vec{b_3} = (-3)^2 + (-6)^2 + 5^2 = 9 + 36 + 25 = 70$
   $c_3 = 70 / 70 = 1$

Donc, dans la base $\{\vec{b_1}, \vec{b_2}, \vec{b_3}\}$, $\vec{v}$ s'écrit comme $\begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}$, c'est-à-dire $\vec{v} = 1 \cdot \vec{b_1} + 1 \cdot \vec{b_2} + 1 \cdot \vec{b_3}$.
:::

## Pourquoi c’est important en Machine Learning ?

- **Représentation des données** : Les bases permettent de représenter les données dans des espaces de caractéristiques. En PCA, les composantes principales forment une base orthonormée qui maximise la variance des données et minimise le bruit (distance perpendiculaire comme mesure du bruit).
- **Transformations linéaires** : Les changements de base sont utilisés pour simplifier les calculs, comme dans les réseaux de neurones où les poids sont des matrices appliquant des transformations linéaires pour extraire des features (e.g., forme du nez, teinte de peau dans la reconnaissance faciale).
- **Réduction de dimensionnalité** : En ML, on utilise des bases orthonormées (via SVD ou QR) pour réduire la dimensionnalité tout en préservant les informations importantes (e.g., embeddings dans NLP). Si les données sont alignées sur une ligne, projeter sur cette direction réduit le bruit.
- **Mécanisme d’attention** : Dans les transformers, les matrices de changement de base (ou projections linéaires) sont utilisées pour calculer les relations entre les tokens via des produits scalaires.

:::info Exemple concret en ML
Dans **PCA**, les données sont projetées sur une base orthonormée formée par les vecteurs propres de la matrice de covariance. Cela réduit la dimensionnalité tout en conservant la variance maximale, facilitant la visualisation ou la classification. Par exemple, des points alignés sur une ligne ont une variance élevée le long de la ligne et faible perpendiculairement (bruit).
:::

:::tip 👉 Application pratique
En **NLP**, les embeddings de mots (comme dans Word2Vec) sont souvent exprimés dans une base non orthonormée. Les algorithmes comme **t-SNE** ou **UMAP** changent de base pour visualiser ces données en 2D ou 3D. Dans les réseaux de neurones, l'apprentissage dérive une base qui extrait les caractéristiques les plus riches des données.
:::