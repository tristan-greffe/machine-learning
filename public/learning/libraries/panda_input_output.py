"""
panda_input_output.py
=====================
Guide pratique pour l'entrée et la sortie de données avec Pandas
Documentation officielle : https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html
"""

import numpy as np
import pandas as pd
from sqlalchemy import create_engine

# ======================================================
# 1. Lecture et écriture d'un CSV
# ======================================================

# Lecture d'un fichier CSV
df = pd.read_csv('example.csv')                  # lecture simple
df = pd.read_csv('example.csv', index_col=0)    # lecture avec l'index sur la première colonne

# Écriture d'un CSV
# index=False pour ne pas sauvegarder l'index par défaut, sinon une colonne "Unnamed: 0" sera ajoutée
df.to_csv('new_file.csv', index=False)


# ======================================================
# 2. Lecture et écriture HTML
# ======================================================

"""
Pandas peut lire les tables HTML avec read_html.  
Nécessite parfois l'installation de : lxml, html5lib, beautifulsoup4
Exemples d'installation :
    pip install lxml html5lib beautifulsoup4
"""

# Lire toutes les tables d'une page Wikipedia
tables = pd.read_html('https://en.wikipedia.org/wiki/World_population')
print(f"Nombre de tables trouvées : {len(tables)}")

# Exemple de sélection et nettoyage
world_pop = tables[0]
world_pop.columns = ['Countries', '2000', '2015', '2030 Est.']
world_pop = world_pop.drop(11, axis=0)  # suppression d'une ligne inutile

# Affichage du DataFrame final
print(world_pop.head())

# Écriture vers un fichier HTML
world_pop.to_html('simple_table.html', index=False)


# ======================================================
# 3. Lecture et écriture Excel
# ======================================================

"""
Pandas peut lire des fichiers Excel (.xlsx, .xls)
Nécessite les bibliothèques : openpyxl et xlrd
    pip install openpyxl xlrd
Chaque feuille (sheet) peut être importée en DataFrame.
"""

# Lecture d'une feuille spécifique
df_excel = pd.read_excel('my_excel_file.xlsx', sheet_name='First_Sheet')

# Pour connaître les noms des feuilles
sheet_names = pd.ExcelFile('my_excel_file.xlsx').sheet_names
print(sheet_names)

# Écriture d'un DataFrame vers Excel
df_excel.to_excel('example.xlsx', sheet_name='First_Sheet', index=False)


# ======================================================
# 4. Lecture et écriture SQL
# ======================================================

"""
Pandas peut interagir avec SQL via SQLAlchemy.  
Pour d'autres moteurs SQL (MySQL, PostgreSQL, MS SQL Server, Oracle, MongoDB),
il est recommandé d'utiliser le pilote Python correspondant et SQLAlchemy.

Exemple ci-dessous avec SQLite, intégré à Python.
"""

# Création d'une base de données SQLite temporaire en mémoire
temp_db = create_engine('sqlite:///:memory:')

# Exemple : utiliser la table populations du HTML précédent
pop = tables[6]
pop.to_sql(name='populations', con=temp_db, index=False, if_exists='replace')  # écrire dans SQL

# Lecture d'une table entière
df_pop = pd.read_sql(sql='populations', con=temp_db)
print(df_pop.head())

# Lecture avec une requête SQL
df_query = pd.read_sql_query(sql="SELECT Country FROM populations", con=temp_db)
print(df_query.head())

"""
Remarques importantes :
- Pandas + SQL dépend du moteur, des permissions, et de la configuration de la base.
- Pour MySQL, PostgreSQL, MS SQL Server, Oracle, etc., consultez la documentation officielle de SQLAlchemy et du pilote correspondant.
- Google est très utile pour trouver des exemples spécifiques selon votre moteur SQL.
"""
