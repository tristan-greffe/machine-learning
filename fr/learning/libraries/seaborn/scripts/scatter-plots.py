"""
===========================================================
Diagrammes de dispersion (Scatter Plots) avec Seaborn
===========================================================

Les diagrammes de dispersion (scatter plots) permettent de visualiser
la relation entre deux variables numériques.

Ils sont utiles pour :
- analyser une corrélation
- observer des tendances
- détecter des valeurs aberrantes (outliers)

Ce script explore la fonction seaborn.scatterplot() ainsi que ses
principaux paramètres : hue, size, style, palette, etc.
"""

# ===========================================================
# Imports
# ===========================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ===========================================================
# Chargement des données
# Source : http://roycekimmons.com/tools/generated_data
# ===========================================================

df = pd.read_csv("./data/dm_office_sales.csv")

print(df.head())
print("\n")
df.info()


# ===========================================================
# Scatterplot simple
# ===========================================================

sns.scatterplot(
    x="salary",
    y="sales",
    data=df
)

plt.show()


# ===========================================================
# Paramètres Seaborn : hue (couleur)
# ===========================================================
# La couleur des points dépend d'une variable catégorielle.

plt.figure(figsize=(12, 8))
sns.scatterplot(
    x="salary",
    y="sales",
    data=df,
    hue="division"
)
plt.show()

plt.figure(figsize=(12, 8))
sns.scatterplot(
    x="salary",
    y="sales",
    data=df,
    hue="work experience"
)
plt.show()


# ===========================================================
# Palette de couleurs
# ===========================================================
# Utilisation d'une palette Matplotlib :
# https://matplotlib.org/stable/tutorials/colors/colormaps.html

plt.figure(figsize=(12, 8))
sns.scatterplot(
    x="salary",
    y="sales",
    data=df,
    hue="work experience",
    palette="viridis"
)
plt.show()


# ===========================================================
# Paramètres Scatterplot : size
# ===========================================================
# Dimensionne la taille des points selon une variable numérique.

plt.figure(figsize=(12, 8))
sns.scatterplot(
    x="salary",
    y="sales",
    data=df,
    size="work experience"
)
plt.show()


# ===========================================================
# Taille fixe des marqueurs (s)
# ===========================================================

plt.figure(figsize=(12, 8))
sns.scatterplot(
    x="salary",
    y="sales",
    data=df,
    s=200
)
plt.show()

plt.figure(figsize=(12, 8))
sns.scatterplot(
    x="salary",
    y="sales",
    data=df,
    s=200,
    linewidth=0,
    alpha=0.2
)
plt.show()


# ===========================================================
# Paramètre style
# ===========================================================
# Applique des styles de marqueurs selon une variable catégorielle.
# Il est possible de définir ses propres marqueurs avec markers=[].

plt.figure(figsize=(12, 8))
sns.scatterplot(
    x="salary",
    y="sales",
    data=df,
    style="level of education"
)
plt.show()

# Combinaison de hue + style sur la même variable
plt.figure(figsize=(12, 8))
sns.scatterplot(
    x="salary",
    y="sales",
    data=df,
    hue="level of education",
    style="level of education",
    s=100
)
plt.show()


# ===========================================================
# Exporter une figure Seaborn
# ===========================================================

plt.figure(figsize=(12, 8))
sns.scatterplot(
    x="salary",
    y="sales",
    data=df,
    hue="level of education",
    style="level of education",
    s=100
)

plt.savefig("example_scatter.jpg")
plt.show()
