# Les DataFrames Pandas

Un **DataFrame pandas** est une structure de données tabulaire :

* lignes → observations
* colonnes → variables
* index → identifiant des lignes

::: tip 👉 Définition formelle
Un DataFrame est un ensemble de Series pandas partageant le même index (Chaque colonne est une Series)
:::

::: details **Exemple**
Exemples de séries ayant le même index :
<div style="display: flex; gap: 2rem;">
<div style="flex: 1">

| Index | Year |
|---------|------|
| USA | 1776 |
| CANADA | 1867 |
| MEXICO | 1821 |
</div>
<div style="flex: 1">

| Index | Pop |
|---------|------|
| USA | 328 |
| CANADA | 38 |
| MEXICO | 126 |
</div>
<div style="flex: 1">

| Index | GDP |
|---------|------|
| USA | 20.5 |
| CANADA | 1.7 |
| MEXICO | 1.22 |
</div>
</div>
DataFrame :

| Index | Year | Pop | GDP |
|---------|------|---------|------|
| USA | 1776 | 328 | 20.5 |
| CANADA | 1867 | 38 | 1.7 |
| MEXICO | 1821 | 126 | 1.22 |
:::

:::details Fichier Python associé
<<< ../../../../public/learning/libraries/dataframe_basics.py
:::

## `groupby`

`groupby()` sert à regrouper des lignes partageant une même valeur (segmenter les données par catégories), puis à appliquer un calcul (`mean`, `sum`, `count`…) sur chaque groupe.

> 👉 Exactement comme en SQL

::: details **Exemple**
<img src="/learning/libraries/pandas-dataframe-groupby.png" style="display: block; margin: 0 auto;width: 100%; height: auto;">
:::

**Colonnes catégorielles vs continues** :

* **Colonnes catégorielles** : Valeurs discrètes mais peuvent être numériques ou textuelles (ex : années)
* **Colonnes continues** : Valeurs numériques continues

:::info
```py
df.groupby('model_year')
```
À ce stade :
* Aucun calcul n’est effectué
* Pandas crée un objet GroupBy en attente
* Il faut obligatoirement appeler une méthode d’agrégation
:::

### Les fonctions d’agrégation

Une fois les données regroupées, Pandas doit savoir quoi calculer.
🔹 Fonctions les plus courantes

| Méthode | Description |
|---------|------|
| `mean()` | Moyenne |
| `sum()` | Somme |
| `count()` | Nombre de valeurs |
| `size()` | Taille du groupe |
| `min()` / `max()` | Valeurs extrêmes |
| `std()` | Écart-type |
| `var()` | Variance |
| `describe()` | Statistiques complètes |

### Comprendre le MultiIndex

Lorsque tu groupes sur plusieurs colonnes, Pandas crée un index hiérarchique (MultiIndex).


:::details Fichier Python associé
<<< ../../../../public/learning/libraries/dataframe_groupby.py
:::

## Combinaison

Dans la pratique, les données viennent rarement d’une seule source :
* plusieurs fichiers CSV
* différentes tables d’une base de données
* résultats intermédiaires de calculs
* données mensuelles / annuelles séparées

👉 Pandas propose **deux grandes familles d’outils** pour assembler ces données :

| Méthode | Quand l’utiliser |
|---------|------|
| `pd.concat()` | Empiler ou coller des DataFrames |
| `pd.merge()` | Faire des jointures logiques (comme en SQL) |

### Concaténation

`concat()` ne regarde pas le sens des données, il se contente de :
* coller des lignes ou des colonnes
* aligner automatiquement les index et colonnes
* remplir avec NaN si nécessaire

> 📌 Aucune logique métier, juste de l’assemblage

::: tip 👉 Définition informelle
La concaténation consiste à "coller" deux DataFrames ensemble
:::

::: details **Exemple : concaténation par colonnes**
<div style="display: flex; gap: 2rem;">
<div style="flex: 1">

| Index | Year | Pop |
|---------|------|------|
| USA | 1776 | 328 |
| CANADA | 1867 | 38 |
| MEXICO | 1821 | 126 |
</div>
<div style="flex: 1">

| Index | GDP | Perct |
|---------|------|------|
| USA | 20.5 | 75% |
| CANADA | 1.7 | NAN |
| MEXICO | 1.22 | 25% |
</div>
</div>
DataFrame concaténé:

| Index | Year | Pop | GDP | Perct |
|---------|------|---------|------|------|
| USA | 1776 | 328 | 20.5 | 75% |
| CANADA | 1867 | 38 | 1.7 | NAN |
| MEXICO | 1821 | 126 | 1.22 | 25% |
:::

::: details **Exemple : concaténation par lignes**
<div style="display: flex; gap: 2rem;">
<div style="flex: 1">

| Index | Year | Pop | GDP |
|---------|------|------|------|
| USA | 1776 | 328 | 20.5 |
| CANADA | 1867 | 38 | 1.7 |
</div>
<div style="flex: 1">

| Index | Year | Pop | GDP |
|---------|------|------|------|
| MEXICO | 1821 | 126 | 1.22 |
| BRAZIL | 1822 | 209 | 1.86 |
</div>
</div>
DataFrame concaténé:

| Index | Year | Pop | GDP |
|---------|------|------|------|
| USA | 1776 | 328 | 20.5 |
| CANADA | 1867 | 38 | 1.7 |
| BRAZIL | 1822 | 209 | 1.86 |
| MEXICO | 1821 | 126 | 1.22 |
:::

### Fusion

`merge()` fonctionne comme une jointure de base de données :
* il utilise une clé,à savoir **how**
* il compare les valeurs
* il décide quelles lignes garder

:::tip Les types de jointures
* **INNER JOIN (intersection)** : Garde uniquement les valeurs présentes dans les deux tables
* **LEFT JOIN** : Garde toutes les lignes de gauche et complète avec `NaN` si nécessaire
* **RIGHT JOIN** : Symétrique du LEFT JOIN
*  **OUTER JOIN (union complète)** : Garde tout ce qui existe au moins une fois
:::

:::details Fichier Python associé
<<< ../../../../public/learning/libraries/dataframe_combination.py
:::