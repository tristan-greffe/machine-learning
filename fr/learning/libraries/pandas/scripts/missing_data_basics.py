"""
missing_data_basics.py
=====================
Gestion des données manquantes avec Pandas

Ce script couvre :
- Détection des valeurs manquantes
- Filtrage conditionnel avec isnull / notnull
- Suppression des données manquantes (dropna)
- Remplacement des données manquantes (fillna)
- Interpolation
"""

import pandas as pd
import numpy as np

# ======================================================
# 1. À quoi ressemblent les valeurs manquantes
# ======================================================

"""
Pandas utilise plusieurs représentations pour les données manquantes :

- np.nan  → données numériques (float)
- pd.NA   → valeur manquante générique (nullable)
- pd.NaT  → données temporelles (timestamp)

pd.NA a été introduit pour unifier la gestion des valeurs manquantes
quel que soit le type de données.
"""

print("=== Valeurs manquantes ===")
print("np.nan :", np.nan)
print("pd.NA  :", pd.NA)
print("pd.NaT :", pd.NaT)
print()

# ------------------------------------------------------
# Comparaisons à éviter
# ------------------------------------------------------

print("=== Comparaisons incorrectes ===")
print("np.nan == np.nan :", np.nan == np.nan)
print("np.nan in [np.nan] :", np.nan in [np.nan])
print("np.nan is np.nan :", np.nan is np.nan)
print("pd.NA == pd.NA :", pd.NA == pd.NA)
print()

"""
⚠️ Conclusion :
- Ne JAMAIS utiliser == pour tester une valeur manquante
- Toujours utiliser isna() / notna()
"""

# ======================================================
# 2. Création et exploration d'un DataFrame
# ======================================================

df = pd.read_csv("./data/movie_scores.csv")

print("=== DataFrame initial ===")
print(df)
print()

print("=== Valeurs manquantes (isnull) ===")
print(df.isnull())
print()

print("=== Valeurs présentes (notnull) ===")
print(df.notnull())
print()

# ======================================================
# 3. Filtrage conditionnel avec données manquantes
# ======================================================

print("=== Acteurs avec prénom connu ===")
print(df[df["first_name"].notnull()])
print()

print("=== Score avant film manquant MAIS sexe connu ===")
condition = (
    df["pre_movie_score"].isnull()
    & df["sex"].notnull()
)
print(df[condition])
print()

# ======================================================
# 4. Suppression des données manquantes (dropna)
# ======================================================

print("=== Suppression des lignes avec au moins un NaN ===")
print(df.dropna())
print()

print("=== Suppression des lignes entièrement NaN ===")
print(df.dropna(how="all"))
print()

print("=== Suppression avec seuil (au moins 1 valeur non nulle) ===")
print(df.dropna(thresh=1))
print()

print("=== Suppression des colonnes avec NaN ===")
print(df.dropna(axis=1))
print()

print("=== Suppression des colonnes avec moins de 4 valeurs non nulles ===")
print(df.dropna(thresh=4, axis=1))
print()

# ======================================================
# 5. Remplacement des données manquantes (fillna)
# ======================================================

print("=== Remplacement global (déconseillé) ===")
print(df.fillna("NEW VALUE!"))
print()

print("=== Remplacement ciblé : first_name ===")
df["first_name"] = df["first_name"].fillna("Empty")
print(df["first_name"])
print()

print("=== Remplacement par la moyenne ===")
mean_score = df["pre_movie_score"].mean()
print("Moyenne pre_movie_score :", mean_score)

df["pre_movie_score"] = df["pre_movie_score"].fillna(mean_score)
print(df["pre_movie_score"])
print()

print("=== Remplacement automatique (numérique uniquement) ===")
print(df.fillna(df.mean(numeric_only=True)))
print()

# ======================================================
# 6. Interpolation
# ======================================================

"""
L’interpolation permet d’estimer une valeur manquante
en fonction des valeurs voisines.
⚠️ À utiliser uniquement si l’ordre des données est pertinent.
"""

airline_tix = {
    "economy": 30,
    "economy_plus": 50,
    "business": np.nan,
    "first": 100
}

ser = pd.Series(airline_tix)

print("=== Série originale ===")
print(ser)
print()

print("=== Interpolation linéaire ===")
print(ser.interpolate())
print()

# Interpolation sur DataFrame
df_prices = pd.DataFrame(ser, columns=["Price"]).reset_index()

print("=== Interpolation spline (ordre 2) ===")
print(df_prices.interpolate(method="spline", order=2))
print()