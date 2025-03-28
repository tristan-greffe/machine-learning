"""
========================
NumPy Basis
========================
"""

import numpy as np

# 1️⃣ Créer un tableau de 10 zéros
zeros = np.zeros(10)
print("Tableau de zéros :")
print(zeros)
print()

# 2️⃣ Créer un tableau de 10 uns
ones = np.ones(10)
print("Tableau de uns :")
print(ones)
print()

# 3️⃣ Créer un tableau avec une valeur donnée
filled = np.full(10, 5)
print("Tableau rempli avec la valeur 5 :")
print(filled)
print()

# 4️⃣ Créer une suite de nombres
sequence = np.arange(0, 10)
print("Suite de nombres de 0 à 9 :")
print(sequence)
print()

# 5️⃣ Créer des valeurs espacées régulièrement
linspace = np.linspace(0, 1, 5)
print("Valeurs espacées entre 0 et 1 :")
print(linspace)
print()

# 6️⃣ Informations sur un tableau
print("Forme du tableau :", sequence.shape)
print("Type des données :", sequence.dtype)