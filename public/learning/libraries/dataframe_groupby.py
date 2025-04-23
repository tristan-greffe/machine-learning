"""
dataframe_groupby.py
====================
Opérations groupby et index multi-niveaux (MultiIndex)

Ce script couvre :
- Le fonctionnement de groupby()
- Les agrégations classiques
- Le groupby sur plusieurs colonnes
- Les index hiérarchiques (MultiIndex)
- La sélection avec loc et xs
- Le tri et la manipulation des niveaux
- Les agrégations avancées avec agg()
"""

import pandas as pd
import numpy as np

# ======================================================
# 0. Chargement des données
# ======================================================

df = pd.read_csv("mpg.csv")

print("=== Aperçu du DataFrame ===")
print(df.head())
print()

# ======================================================
# 1. Méthode groupby()
# ======================================================

"""
groupby() crée un objet intermédiaire.
Aucune opération n’est effectuée tant qu’une méthode
d’agrégation n’est pas appliquée.
"""

grouped = df.groupby("model_year")

print("Type de l'objet groupby :", type(grouped))
print()

# ------------------------------------------------------
# Agrégations classiques
# ------------------------------------------------------

print("=== Moyennes par année ===")
avg_year = grouped.mean(numeric_only=True)
print(avg_year)
print()

print("Index :", avg_year.index)
print("Colonnes :", avg_year.columns)
print()

print("=== Colonne mpg uniquement ===")
print(avg_year["mpg"])
print()

# Accès direct en une ligne
print("=== mpg moyen par année (one-liner) ===")
print(df.groupby("model_year").mean(numeric_only=True)["mpg"])
print()

# Statistiques descriptives
print("=== describe() par année ===")
print(df.groupby("model_year").describe())
print()

print("=== describe() transposé ===")
print(df.groupby("model_year").describe().transpose())
print()

# ======================================================
# 2. Groupby sur plusieurs colonnes
# ======================================================

print("=== Moyennes par année ET par cylindres ===")
year_cyl = df.groupby(["model_year", "cylinders"]).mean(numeric_only=True)
print(year_cyl.head())
print()

print("Index du DataFrame multi-niveaux :")
print(year_cyl.index)
print()

# ======================================================
# 3. MultiIndex (index hiérarchique)
# ======================================================

print("=== Informations sur le MultiIndex ===")
print("Niveaux :", year_cyl.index.levels)
print("Noms des niveaux :", year_cyl.index.names)
print()

# ------------------------------------------------------
# Sélection avec loc
# ------------------------------------------------------

print("=== Toutes les cylindrées pour l'année 70 ===")
print(year_cyl.loc[70])
print()

print("=== Années 70 et 72 ===")
print(year_cyl.loc[[70, 72]])
print()

print("=== Ligne unique : année 70, 8 cylindres ===")
print(year_cyl.loc[(70, 8)])
print()

# ------------------------------------------------------
# Sélection transversale avec xs()
# ------------------------------------------------------

"""
xs() (cross-section) permet de sélectionner des données
à partir d’un niveau interne du MultiIndex.
"""

print("=== Toutes les données pour l'année 70 (xs) ===")
print(year_cyl.xs(key=70, level="model_year"))
print()

print("=== Moyennes pour les moteurs 4 cylindres (toutes années) ===")
four_cyl = year_cyl.xs(key=4, level="cylinders")
print(four_cyl)
print()

"""
⚠️ Bon réflexe :
Il est souvent plus simple de FILTRER les données
avant le groupby plutôt que d’essayer de manipuler
le MultiIndex après coup.
"""

print("=== Filtrage AVANT groupby (6 et 8 cylindres) ===")
filtered = df[df["cylinders"].isin([6, 8])]
print(
    filtered
    .groupby(["model_year", "cylinders"])
    .mean(numeric_only=True)
)
print()

# ======================================================
# 4. Manipulation des niveaux du MultiIndex
# ======================================================

# Échange des niveaux
print("=== Swap des niveaux ===")
print(year_cyl.swaplevel().head())
print()

# Tri du MultiIndex
print("=== Tri par année (descendant) ===")
print(year_cyl.sort_index(level="model_year", ascending=False).head())
print()

print("=== Tri par cylindres (descendant) ===")
print(year_cyl.sort_index(level="cylinders", ascending=False).head())
print()

# ======================================================
# 5. Agrégations avancées avec agg()
# ======================================================

"""
agg() permet d’appliquer plusieurs fonctions
d’agrégation simultanément, éventuellement différentes
selon les colonnes.
"""

# Sélection des colonnes numériques
num_df = df.select_dtypes(include="number")

print("=== Agrégations globales ===")
print(num_df.agg(["median", "mean"]))
print()

print("=== Agrégations ciblées (mpg, weight) ===")
print(num_df.agg(["sum", "mean"])[["mpg", "weight"]])
print()

print("=== Agrégations spécifiques par colonne ===")
print(
    df.agg({
        "mpg": ["median", "mean"],
        "weight": ["mean", "std"]
    })
)
print()

# ======================================================
# 6. groupby() + agg()
# ======================================================

print("=== groupby + agg() ===")
print(
    df.groupby("model_year").agg({
        "mpg": ["median", "mean"],
        "weight": ["mean", "std"]
    })
)
print()
