"""
pandas_pivot_tables.py
=====================
Le pivotement des données peut aider à clarifier les relations et à explorer vos datasets. 

Documentation complète sur le pivot et les méthodes connexes :
https://pandas.pydata.org/docs/user_guide/reshaping.html
"""

import numpy as np
import pandas as pd

# ======================================================
# Lecture du fichier CSV
# ======================================================
df = pd.read_csv('./data/Sales_Funnel_CRM.csv')

# ======================================================
# 1. Méthode pivot()
# ======================================================
"""
La méthode pivot() réorganise les données en fonction des valeurs de colonnes et d'un nouvel index.
⚠️ Note : Il n'est pas toujours nécessaire de pivoter les données. Cette méthode est surtout utile
pour l'analyse, l'exploration et la visualisation.

Checklist avant d'utiliser pivot() :
1. Quelle question essayez-vous de répondre ?
2. À quoi ressemblerait le DataFrame qui répond à cette question ?
3. Le pivot est-il vraiment nécessaire ?
4. Quelles colonnes sont essentielles pour le pivot ?
"""

help(pd.pivot)  # Documentation rapide

# Exemple pratique : combien de licences de chaque produit Google a-t-il acheté ?
licenses = df[['Company', 'Product', 'Licenses']]

# Pivot simple
pivot_simple = pd.pivot(
    data=licenses,
    index='Company',   # valeurs uniques de Company deviennent l'index
    columns='Product', # valeurs uniques de Product deviennent les colonnes
    values='Licenses'  # valeurs numériques à afficher
)
pivot_simple

# ======================================================
# 2. Méthode pivot_table()
# ======================================================
"""
Comme pivot(), pivot_table() réorganise les données mais permet également d'appliquer des fonctions
d'agrégation. Très pratique pour résumer les données numériques.
"""

# Pivot table basique avec somme
pivot_sum = pd.pivot_table(df, index="Company", aggfunc='sum')

# Sélectionner uniquement les colonnes intéressantes
pivot_sum[['Licenses', 'Sale Price']]

# Ou en utilisant le paramètre 'values'
pivot_sum_values = pd.pivot_table(
    df,
    index="Company",
    values=['Licenses', 'Sale Price'],
    aggfunc='sum'
)

# Équivalent avec groupby
df.groupby('Company').sum()[['Licenses', 'Sale Price']]

# ======================================================
# Pivot multi-index
# ======================================================
pivot_multi = pd.pivot_table(
    df,
    index=["Account Manager", "Contact"],
    values=['Sale Price'],
    aggfunc='sum'
)

# Ajouter une dimension de colonne (segmentation par produit)
pivot_multi_columns = pd.pivot_table(
    df,
    index=["Account Manager", "Contact"],
    values=["Sale Price"],
    columns=["Product"],
    aggfunc=np.sum,
    fill_value=0  # remplace NaN par 0
)

# Plusieurs fonctions d'agrégation
pivot_multi_agg = pd.pivot_table(
    df,
    index=["Account Manager", "Contact"],
    values=["Sale Price"],
    columns=["Product"],
    aggfunc=[np.sum, np.mean],
    fill_value=0
)

# Plusieurs colonnes de valeurs
pivot_multi_values = pd.pivot_table(
    df,
    index=["Account Manager", "Contact"],
    values=["Sale Price", "Licenses"],
    columns=["Product"],
    aggfunc=np.sum,
    fill_value=0
)

# Multi-index avec Product dans l'index
pivot_full_index = pd.pivot_table(
    df,
    index=["Account Manager", "Contact", "Product"],
    values=["Sale Price", "Licenses"],
    aggfunc=np.sum,
    fill_value=0
)

# Ajouter les totaux généraux avec margins=True
pivot_with_totals = pd.pivot_table(
    df,
    index=["Account Manager", "Contact", "Product"],
    values=["Sale Price", "Licenses"],
    aggfunc=np.sum,
    fill_value=0,
    margins=True
)

# Exemple avec autre dimension
pivot_status = pd.pivot_table(
    df,
    index=["Account Manager", "Status"],
    values=["Sale Price"],
    aggfunc=np.sum,
    fill_value=0,
    margins=True
)
