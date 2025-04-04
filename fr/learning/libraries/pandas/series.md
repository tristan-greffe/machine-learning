# Les Series Pandas

## Introduction

Une **Series Pandas** est une structure de données fondamentale de la bibliothèque **Pandas**. Elle représente un **tableau unidimensionnel** de données **associé à un index étiqueté**. C’est cet **index nominatif (labels)** qui distingue une Series d’une **liste Python** et d’un **array NumPy**, qui possède uniquement un index numérique.

| Structure | Index |
|---------|------|
| Liste Python | implicite (positions) |
| `numpy.ndarray` | numérique |
| `pandas.Series` | **numérique + étiqueté** |

> 📌 Une Series = **données + index étiqueté**

::: tip 👉 Définition formelle
Une **Series Pandas** est :
- un tableau **1D**
- avec des **étiquettes d’axes (labels)**
- basé sur **NumPy** (performant et vectorisé)
:::

::: info **Series Pandas** VS **array NumPy**
<div style="display: flex; gap: 2rem;">
<div style="flex: 1">
array NumPy :

| Index | Data |
|---------|------|
| 0 | 1776 |
| 1 | 1867 |
| 2 | 1821 |
</div>
<div style="flex: 1">
Series Pandas :

| Labeled Index | Data |
|---------|------|
| USA | 1776 |
| CANADA | 1867 |
| MEXICO | 1821 |
</div>
</div>
:::


## Pourquoi utiliser une Series ?

### 1. Index étiqueté (clé → valeur)

L’index peut être :
- des chaînes de caractères
- des entiers
- tout objet hashable

::: tip Cela permet :
- une lecture plus naturelle
- une extraction plus claire
- un code plus proche des données réelles
:::

### 2. Double accès aux données

Une Series conserve :

- un **index numérique** (position)
- un **index étiqueté** (label)

> 👉 On peut accéder aux valeurs par position ou par label

::: info **Series Pandas** 
| Index | Labeled Index | Data |
|---------|---------|------|
| 0 | USA | 1776 |
| 1 | CANADA | 1867 |
| 2 | MEXICO | 1821 |
:::

### 3. Performances et opérations vectorisées

Les Series reposent sur NumPy :

- opérations rapides
- diffusion automatique (**broadcasting**)
- pas besoin de boucles `for`

## Fichier Python associé

Le fichier suivant contient tous les exemples de création et d’opérations sur les Series Pandas :

:::details principales opérations NumPy
<<< ../../../../public/learning/libraries/series_basics.py
:::

