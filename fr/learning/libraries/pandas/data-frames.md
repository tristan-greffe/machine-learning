# Les DataFrames Pandas

Un **DataFrame pandas** est une structure de données tabulaire :

* lignes → observations
* colonnes → variables
* index → identifiant des lignes

::: tip 👉 Définition formelle
Un DataFrame est un ensemble de Series pandas partageant le même index (Chaque colonne est une Series)
:::

::: info **Exemple**
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

## `groupby`

Une opération `groupby` permet de :

* segmenter les données par catégories
* appliquer une fonction d’agrégation (mean, sum, count…)

::: info **Exemple**
<img src="/learning/libraries/pandas-dataframe-groupby.png" style="display: block; margin: 0 auto;width: 100%; height: auto;">
:::

**Colonnes catégorielles vs continues** :

* **Colonnes catégorielles** : Valeurs discrètes mais peuvent être numériques ou textuelles (ex : années)
* **Colonnes continues** : Valeurs numériques continues

## Fichier Python associé

:::details DataFrame
<<< ../../../../public/learning/libraries/dataframe_basics.py
:::

:::details `groupby`
<<< ../../../../public/learning/libraries/dataframe_groupby.py
:::