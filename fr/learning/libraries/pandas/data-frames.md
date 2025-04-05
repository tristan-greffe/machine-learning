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

## Fichier Python associé

:::details DataFrame
<<< ../../../../public/learning/libraries/dataframe_basics.py
:::
