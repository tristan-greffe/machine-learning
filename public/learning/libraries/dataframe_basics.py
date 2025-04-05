"""
dataframe_basics.py
==================
Bases des DataFrames Pandas
Ce script couvre :
- La création de DataFrames à partir de tableaux ou de fichiers CSV
- L'accès aux colonnes et aux lignes
- La manipulation des données : création, suppression, modification
"""

import pandas as pd
import numpy as np

# ======================================================
# 1. Création d'un DataFrame à partir d'objets Python
# ======================================================

# Fixer la seed pour reproduire les mêmes nombres aléatoires
np.random.seed(101)

# Création d'un tableau 4x3 avec des entiers aléatoires entre 0 et 100
mydata = np.random.randint(0, 101, (4, 3))
print("Tableau de données aléatoires :\n", mydata, "\n")

# Définir un index pour les lignes (exemple : abréviations des états)
myindex = ['CA', 'NY', 'AZ', 'TX']

# Définir les noms des colonnes
mycolumns = ['Jan', 'Feb', 'Mar']

# Création du DataFrame à partir des données uniquement
df = pd.DataFrame(data=mydata)
print("DataFrame avec index et colonnes par défaut :\n", df, "\n")

# Création du DataFrame avec un index personnalisé
df = pd.DataFrame(data=mydata, index=myindex)
print("DataFrame avec index personnalisé :\n", df, "\n")

# Création du DataFrame avec index et colonnes personnalisés
df = pd.DataFrame(data=mydata, index=myindex, columns=mycolumns)
print("DataFrame complet avec index et colonnes :\n", df, "\n")

# Obtenir des informations sur le DataFrame
print("Informations générales sur le DataFrame :")
df.info()
print("\n")

# ======================================================
# 2. Lecture d'un fichier CSV dans un DataFrame
# ======================================================

# Lecture du fichier 'tips.csv' (assurez-vous qu'il est dans le même dossier)
df = pd.read_csv('tips.csv')
print("Lecture du fichier CSV 'tips.csv' :\n", df.head(), "\n")

# Obtenir des informations de base sur le DataFrame
print("Colonnes :", df.columns)
print("Index :", df.index)
print("Premières lignes :", df.head(3))
print("Dernières lignes :", df.tail(3))
print("Résumé info :")
df.info()
print("Nombre de lignes :", len(df))
print("Statistiques descriptives :")
print(df.describe().transpose())
print("\n")

# ======================================================
# 3. Sélection et manipulation des colonnes
# ======================================================

# Saisir une seule colonne
print("Exemple d'accès à une colonne :")
print(df['total_bill'])
print("Type :", type(df['total_bill']), "\n")

# Saisir plusieurs colonnes
print("Accès à plusieurs colonnes :")
print(df[['total_bill', 'tip']], "\n")

# Créer de nouvelles colonnes
df['tip_percentage'] = 100 * df['tip'] / df['total_bill']
df['price_per_person'] = df['total_bill'] / df['size']

# Arrondir les valeurs à 2 décimales
df['price_per_person'] = np.round(df['price_per_person'], 2)

print("DataFrame avec nouvelles colonnes :\n", df.head(), "\n")

# Supprimer une colonne
df = df.drop('tip_percentage', axis=1)
print("DataFrame après suppression de la colonne 'tip_percentage' :\n", df.head(), "\n")

# ======================================================
# 4. Bases de l'index
# ======================================================

# Vérifier l'index actuel
print("Index actuel :", df.index, "\n")

# Définir une colonne comme index
df = df.set_index('Payment ID')
print("DataFrame après avoir défini 'Payment ID' comme index :\n", df.head(), "\n")

# Réinitialiser l'index (transforme l'index en colonne)
df = df.reset_index()
print("DataFrame après réinitialisation de l'index :\n", df.head(), "\n")

# ======================================================
# 5. Manipulation des lignes (rows)
# ======================================================

# Définir à nouveau 'Payment ID' comme index pour manipuler les lignes
df = df.set_index('Payment ID')

# Accès à une seule ligne
print("Accès à la première ligne par position (iloc) :\n", df.iloc[0], "\n")
print("Accès à une ligne par label (loc) :\n", df.loc['Sun2959'], "\n")

# Accès à plusieurs lignes
print("Accès à plusieurs lignes par position :\n", df.iloc[0:4], "\n")
print("Accès à plusieurs lignes par label :\n", df.loc[['Sun2959','Sun5260']], "\n")

# Supprimer une ligne par label
df_temp = df.drop('Sun2959', axis=0)
print("DataFrame après suppression de la ligne 'Sun2959' (temporaire) :\n", df_temp.head(), "\n")

# Insérer une nouvelle ligne (rarement utilisé en pratique)
# Copier une ligne existante
one_row = df.iloc[0]

# Attention : .append() est déprécié depuis Pandas 2.0, utiliser pd.concat() à la place
df = pd.concat([df, one_row.to_frame().T])
print("DataFrame après ajout d'une nouvelle ligne :\n", df.tail(), "\n")
