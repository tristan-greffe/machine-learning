# Introduction à [Seaborn](https://seaborn.pydata.org/)

`Seaborn`, une bibliothèque Python construite au-dessus de Matplotlib dédiée à la **visualisation statistique des données**, est conçue pour fonctionner **nativement avec les DataFrames Pandas** et permet de produire rapidement des graphiques statistiques clairs, esthétiques et informatifs.

Elle a pour objectif de :
* simplifier la création de graphiques statistiques
* réduire la quantité de code nécessaire
* fournir des visualisations par défaut esthétiques et cohérentes

> 📌 Seaborn est particulièrement adaptée à l’**exploration de données (EDA)**.

## Seaborn & Pandas

Seaborn est pensée pour interagir directement avec les **DataFrames Pandas**.
* Les données sont passées via l’argument data
* Les variables sont référencées par leurs noms de colonnes
* Les graphiques sont automatiquement adaptés aux types de données

:::info ➡️
Contrairement à Matplotlib, on ne manipule pas directement les tableaux NumPy dans la majorité des cas.
:::

## Philosophie de Seaborn

### Une syntaxe simple et expressive

La majorité des graphiques Seaborn peuvent être créés en ***une seule ligne de code***.

:::tip Exemple : nuage de points (scatter plot)
```py
import seaborn as sns

sns.scatterplot(x="age", y="salary", data=df)
```
* `x` et `y` sont des chaînes de caractères
* Elles correspondent aux colonnes du DataFrame
* `data` contient la source des données

➡️ Le graphique est généré automatiquement, sans configuration supplémentaire.
:::

### Une abstraction au-dessus de Matplotlib

Seaborn utilise exactement les mêmes objets que Matplotlib : `Figure` & `Axes`. Cela signifie que :
* Seaborn crée le graphique
* Matplotlib peut ensuite être utilisé pour le personnaliser

:::tip Exemple
```py
import matplotlib.pyplot as plt

sns.scatterplot(x="age", y="salary", data=df)
plt.title("Salaire en fonction de l'âge")
plt.xlabel("Âge")
plt.ylabel("Salaire")
```
➡️ Seaborn = simplicité
➡️ Matplotlib = personnalisation fine
:::

> Les deux bibliothèques sont **complémentaires**, pas concurrentes.

## Types de graphiques disponibles

* Diagrammes de dispersion
* Diagrammes de distribution
* Diagrammes catégoriels
* Diagrammes de comparaison
* Grilles Seaborn (Grids)
* Diagrammes matriciels

:::info quand et pourquoi utiliser chaque type de graphique ?
La réponse dépend :
* du type de variables (numérique, catégorielle)
* de la relation que vous cherchez à analyser
* de la question que vous vous posez
:::

:::warning Important :
👉 Toutes les questions ne nécessitent pas un graphique. Parfois, une simple statistique descriptive suffit.
:::

