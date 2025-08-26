# Introduction à [NumPy](https://numpy.org/doc/stable)

`NumPy` est la bibliothèque fondamentale de Python pour le calcul numérique. Elle est utilisée dans toute la data science et le machine learning.`Pandas`, `Scikit-learn` ou `TensorFlow` reposent sur NumPy.

## Qu’est-ce que `NumPy` ?

`NumPy` signifie **Numerical Python**. Son objet central est le **ndarray** (*N-dimensional array*). C’est un tableau à plusieurs dimensions :  

- 1D → vecteur  
- 2D → matrice  
- 3D ou plus → tenseur  

::: tip 👉 Exemple mathématique :  
Un tableau `[1, 2, 3]` représente le vecteur (1, 2, 3) ∈ ℝ³.  
Un tableau `[[1, 2], [3, 4]]` représente la matrice :  
$$
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
$$
:::

## Pourquoi utiliser `NumPy` ?

### 1. Performance

`NumPy` est une bibliothèque écrite en C et optimisée pour le calcul numérique.  
Les opérations sont réalisées en interne par du code compilé, ce qui les rend **beaucoup plus rapides** que les boucles Python classiques.  

::: tip 👉 Exemple :  
Additionner deux tableaux `NumPy` de grande taille est bien plus efficace que parcourir des listes Python avec une boucle `for`.  
C’est cette efficacité qui a fait de `NumPy` le socle de toutes les bibliothèques de data science (Pandas, Scikit-learn, TensorFlow…).
:::


### 2. Le Broadcasting

Le **broadcasting** est l’une des fonctionnalités les plus puissantes de `NumPy`.  
Il permet d’appliquer automatiquement une opération entre deux tableaux de dimensions différentes, sans avoir à écrire de boucles explicites.  

Concrètement, `NumPy` "étend" (ou **diffuse**) le plus petit tableau pour qu’il ait la même forme que le plus grand, et applique ensuite l’opération élément par élément.  

::: tip 👉 Exemple : scalaire & vecteur 
```python
import numpy as np

a = np.array([1, 2, 3, 4])
b = 5

print(a + b)  # [6 7 8 9]
```
Ici, le scalaire `5` est diffusé automatiquement en `[5, 5, 5, 5]`.  
Résultat : chaque élément du vecteur `a` est additionné à `5`.
:::

::: tip 👉 Exemple : matrice et vecteur
```python
A = np.array([[1, 2, 3],
              [4, 5, 6]])
B = np.array([10, 20, 30])

print(A + B)
```
Résultat attendu :

$$
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6
\end{bmatrix}
+
\begin{bmatrix}
10 & 20 & 30
\end{bmatrix}
=
\begin{bmatrix}
11 & 22 & 33 \\
14 & 25 & 36
\end{bmatrix}
$$

Ici, le vecteur `B` est diffusé sur chaque ligne de `A`.
:::

#### Pourquoi c’est utile ?

- Évite d’écrire des boucles manuelles.  
- Code plus clair et plus lisible.  
- Calculs optimisés en C, donc très rapides.  

➡️ Le broadcasting est donc **une des raisons principales d’utiliser NumPy plutôt que les listes Python**.

### 3. Fonctions intégrées

`NumPy` ne se limite pas aux tableaux. Il propose un grand nombre de fonctions mathématiques prêtes à l’emploi :
* **Algèbre linéaire** : produit matriciel, inverse, déterminant, valeurs propres.
* **Statistiques** : moyenne, écart-type, variance, quantiles.
* **Trigonométrie** : sinus, cosinus, tangente, etc.
* **Nombres aléatoires** : tirages pseudo-aléatoires, distributions gaussiennes, binomiales, uniformes…

Ces fonctionnalités couvrent la majorité des besoins en calcul scientifique et évitent de réécrire des algorithmes de base.  