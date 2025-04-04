"""
series_basics.py
Bases des Series Pandas
"""

import pandas as pd
import numpy as np

# ======================================================
# 1. Création d'une Series à partir d'une liste
# ======================================================

data = [1776, 1867, 1821]
series_numeric_index = pd.Series(data)

print("Series avec index numérique par défaut:")
print(series_numeric_index)
print()


# ======================================================
# 2. Création d'une Series avec un index étiqueté
# ======================================================

countries = ["USA", "Canada", "Mexico"]
independence_years = [1776, 1867, 1821]

series_labeled = pd.Series(independence_years, index=countries)

print("Series avec index étiqueté:")
print(series_labeled)
print()


# ======================================================
# 3. Accès aux éléments
# ======================================================

print("Accès par position (index numérique):")
print(series_labeled[0])  # USA
print()

print("Accès par label:")
print(series_labeled["USA"])
print()


# ======================================================
# 4. Création d'une Series à partir d'un dictionnaire
# ======================================================

ages = {
    "Sam": 5,
    "Frank": 10,
    "Spike": 7
}

series_from_dict = pd.Series(ages)

print("Series créée à partir d'un dictionnaire:")
print(series_from_dict)
print()


# ======================================================
# 5. Vérification des index
# ======================================================

print("Index de la series_from_dict:")
print(series_from_dict.index)
print()


# ======================================================
# 6. Series de ventes (exemple Q1 / Q2)
# ======================================================

sales_q1_dict = {
    "Japan": 80,
    "China": 150,
    "India": 200,
    "USA": 130
}

sales_q2_dict = {
    "Brazil": 100,
    "China": 165,
    "India": 210,
    "USA": 140
}

sales_q1 = pd.Series(sales_q1_dict)
sales_q2 = pd.Series(sales_q2_dict)

print("Ventes Q1:")
print(sales_q1)
print()

print("Ventes Q2:")
print(sales_q2)
print()


# ======================================================
# 7. Opérations scalaires (broadcasting)
# ======================================================

print("Ventes Q1 multipliées par 2:")
print(sales_q1 * 2)
print()

print("Ventes Q1 en centaines:")
print(sales_q1 / 100)
print()


# ======================================================
# 8. Opérations entre Series (alignement sur l'index)
# ======================================================

print("Addition directe Q1 + Q2 (avec NaN):")
total_sales_na = sales_q1 + sales_q2
print(total_sales_na)
print()


# ======================================================
# 9. Addition avec gestion des valeurs manquantes
# ======================================================

print("Addition avec fill_value=0:")
total_sales = sales_q1.add(sales_q2, fill_value=0)
print(total_sales)
print()


# ======================================================
# 10. Types de données (dtype)
# ======================================================

print("Type des données Q1:")
print(sales_q1.dtype)
print()

print("Type des données après addition:")
print(total_sales.dtype)
print()


# ======================================================
# 11. Conversion de type
# ======================================================

total_sales_int = total_sales.astype("int64")

print("Total des ventes converti en int64:")
print(total_sales_int)
print()


# ======================================================
# 12. Attributs importants d'une Series
# ======================================================

print("Valeurs (NumPy array):")
print(total_sales.values)
print()

print("Index:")
print(total_sales.index)
print()

print("Shape:")
print(total_sales.shape)
print()
