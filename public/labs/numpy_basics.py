"""
========================
NumPy Basics - Exercices et Solutions
========================
"""

import numpy as np

# -----------------------------
# 1️⃣ Créer des tableaux simples
# -----------------------------

# Tableau de 10 zéros
zeros = np.zeros(10)
print("1️⃣ Tableau de zéros :")
print(zeros)
print()

# Tableau de 10 uns
ones = np.ones(10)
print("2️⃣ Tableau de uns :")
print(ones)
print()

# Tableau rempli de 5
fives = np.ones(10) * 5
print("3️⃣ Tableau rempli de 5 :")
print(fives)
print()

# -----------------------------
# 2️⃣ Suites de nombres
# -----------------------------

# Nombres entiers de 10 à 50
integers_10_50 = np.arange(10, 51)
print("4️⃣ Nombres de 10 à 50 :")
print(integers_10_50)
print()

# Entiers pairs de 10 à 50
even_10_50 = np.arange(10, 51, 2)
print("5️⃣ Entiers pairs de 10 à 50 :")
print(even_10_50)
print()

# Suite de nombres de 0 à 9
sequence = np.arange(0, 10)
print("6️⃣ Suite de 0 à 9 :")
print(sequence)
print()

# Valeurs linéairement espacées entre 0 et 1
linspace = np.linspace(0, 1, 5)
print("7️⃣ Valeurs espacées entre 0 et 1 :")
print(linspace)
print()

# -----------------------------
# 3️⃣ Matrices et identité
# -----------------------------

# Matrice 3x3 avec valeurs 0 à 8
matrix_3x3 = np.arange(9).reshape(3, 3)
print("8️⃣ Matrice 3x3 de 0 à 8 :")
print(matrix_3x3)
print()

# Matrice identité 3x3
identity_3x3 = np.eye(3)
print("9️⃣ Matrice identité 3x3 :")
print(identity_3x3)
print()

# -----------------------------
# 4️⃣ Nombres aléatoires
# -----------------------------

# Nombre aléatoire entre 0 et 1
rand_number = np.random.rand(1)
print("🔟 Nombre aléatoire entre 0 et 1 :")
print(rand_number)
print()

# Tableau de 25 nombres aléatoires (distribution normale)
rand_normal = np.random.randn(25)
print("1️⃣1️⃣ Tableau de 25 nombres aléatoires (normale) :")
print(rand_normal)
print()

# -----------------------------
# 5️⃣ Matrices avancées
# -----------------------------

# Matrice 10x10 avec valeurs 0.01 à 1.00
matrix_10x10 = np.arange(1, 101).reshape(10, 10) / 100
print("1️⃣2️⃣ Matrice 10x10 de 0.01 à 1 :")
print(matrix_10x10)
print()

# 20 points linéaires entre 0 et 1
linspace_20 = np.linspace(0, 1, 20)
print("1️⃣3️⃣ 20 points linéaires entre 0 et 1 :")
print(linspace_20)
print()

# -----------------------------
# 6️⃣ Indexation et sélection
# -----------------------------

mat = np.arange(1, 26).reshape(5, 5)
print("1️⃣4️⃣ Matrice 5x5 de 1 à 25 :")
print(mat)
print()

print("1️⃣5️⃣ Sélection des lignes 3 à 5 et colonnes 2 à 5 :")
print(mat[2:, 1:])
print()

print("1️⃣6️⃣ Valeur de la ligne 4, colonne 5 :")
print(mat[3, 4])
print()

print("1️⃣7️⃣ Colonnes 2 de la ligne 1 à 3 :")
print(mat[:3, 1:2])
print()

print("1️⃣8️⃣ Ligne 5 complète :")
print(mat[4, :])
print()

print("1️⃣9️⃣ Lignes 4 à 5 complètes :")
print(mat[3:5, :])
print()

# -----------------------------
# 7️⃣ Opérations NumPy
# -----------------------------

# Somme de toutes les valeurs
total_sum = mat.sum()
print("2️⃣0️⃣ Somme totale de mat :", total_sum)

# Écart type
std_mat = mat.std()
print("2️⃣1️⃣ Écart type :", std_mat)

# Somme par colonne
col_sum = mat.sum(axis=0)
print("2️⃣2️⃣ Somme par colonne :", col_sum)
print()

# -----------------------------
# 8️⃣ Seed pour nombres aléatoires reproductibles
# -----------------------------
np.random.seed(101)
reproducible_random = np.random.rand(5)
print("2️⃣3️⃣ Exemples de nombres aléatoires reproductibles :")
print(reproducible_random)
