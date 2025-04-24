"""
dataframe_combination.py
========================
Combinaison de DataFrames avec Pandas

Ce script couvre :
- La concaténation avec pd.concat()
- Les fusions avec pd.merge()
- Les jointures SQL-like : inner, left, right, outer
- Les fusions sur index ou colonnes différentes
- La gestion des colonnes dupliquées
"""

import pandas as pd
import numpy as np

# ======================================================
# 1. CONCATÉNATION (pd.concat)
# ======================================================

"""
La concaténation permet de "coller" des DataFrames
ayant une structure similaire.
"""

data_one = {
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']
}

data_two = {
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']
}

one = pd.DataFrame(data_one)
two = pd.DataFrame(data_two)

print("=== DataFrame ONE ===")
print(one, "\n")

print("=== DataFrame TWO ===")
print(two, "\n")

# ------------------------------------------------------
# Concaténation par lignes (axis=0) — par défaut
# ------------------------------------------------------

print("=== Concaténation par lignes (axis=0) ===")
concat_rows = pd.concat([one, two], axis=0)
print(concat_rows, "\n")

"""
⚠️ Les colonnes ne correspondent pas :
Pandas remplit automatiquement avec NaN
"""

# ------------------------------------------------------
# Concaténation par colonnes (axis=1)
# ------------------------------------------------------

print("=== Concaténation par colonnes (axis=1) ===")
concat_cols = pd.concat([one, two], axis=1)
print(concat_cols, "\n")

# ------------------------------------------------------
# Concaténation par lignes AVEC colonnes identiques
# ------------------------------------------------------

print("=== Concaténation par lignes avec colonnes alignées ===")
two.columns = one.columns  # renommage C,D → A,B
concat_aligned = pd.concat([one, two], axis=0)
print(concat_aligned, "\n")

# Réinitialisation de l'index
concat_aligned = concat_aligned.reset_index(drop=True)
print("=== Index réinitialisé ===")
print(concat_aligned, "\n")

# ======================================================
# 2. FUSION (pd.merge)
# ======================================================

"""
pd.merge() fonctionne comme une jointure SQL
"""

registrations = pd.DataFrame({
    'reg_id': [1, 2, 3, 4],
    'name': ['Andrew', 'Bobo', 'Claire', 'David']
})

logins = pd.DataFrame({
    'log_id': [1, 2, 3, 4],
    'name': ['Xavier', 'Andrew', 'Yolanda', 'Bobo']
})

print("=== Registrations ===")
print(registrations, "\n")

print("=== Logins ===")
print(logins, "\n")

# ------------------------------------------------------
# INNER JOIN
# ------------------------------------------------------

print("=== INNER JOIN ===")
inner_merge = pd.merge(
    registrations,
    logins,
    how='inner',
    on='name'
)
print(inner_merge, "\n")

"""
INNER :
→ uniquement les clés présentes dans LES DEUX tables
"""

# ------------------------------------------------------
# LEFT JOIN
# ------------------------------------------------------

print("=== LEFT JOIN ===")
left_merge = pd.merge(
    registrations,
    logins,
    how='left',
    on='name'
)
print(left_merge, "\n")

"""
LEFT :
→ toutes les lignes de la table de gauche
"""

# ------------------------------------------------------
# RIGHT JOIN
# ------------------------------------------------------

print("=== RIGHT JOIN ===")
right_merge = pd.merge(
    registrations,
    logins,
    how='right',
    on='name'
)
print(right_merge, "\n")

"""
RIGHT :
→ toutes les lignes de la table de droite
"""

# ------------------------------------------------------
# OUTER JOIN
# ------------------------------------------------------

print("=== OUTER JOIN ===")
outer_merge = pd.merge(
    registrations,
    logins,
    how='outer',
    on='name'
)
print(outer_merge, "\n")

"""
OUTER :
→ union complète des deux tables
"""

# ======================================================
# 3. FUSION SUR INDEX
# ======================================================

registrations_idx = registrations.set_index("name")

print("=== Fusion index (left_index=True) ===")
merge_index = pd.merge(
    registrations_idx,
    logins,
    left_index=True,
    right_on='name',
    how='inner'
)
print(merge_index, "\n")

# ======================================================
# 4. COLONNES CLÉS DIFFÉRENTES
# ======================================================

registrations_renamed = registrations.rename(columns={'name': 'reg_name'})

print("=== Colonnes différentes ===")
print(registrations_renamed, "\n")

merge_diff_cols = pd.merge(
    registrations_renamed,
    logins,
    left_on='reg_name',
    right_on='name',
    how='inner'
)

print(merge_diff_cols, "\n")

# Nettoyage
merge_diff_cols = merge_diff_cols.drop('reg_name', axis=1)
print("=== Après nettoyage ===")
print(merge_diff_cols, "\n")

# ======================================================
# 5. COLONNES DUPLIQUÉES & SUFFIXES
# ======================================================

registrations_dup = registrations.rename(columns={'reg_id': 'id'})
logins_dup = logins.rename(columns={'log_id': 'id'})

print("=== Colonnes dupliquées ===")
print(pd.merge(registrations_dup, logins_dup, on='name'), "\n")

print("=== Suffixes personnalisés ===")
print(
    pd.merge(
        registrations_dup,
        logins_dup,
        on='name',
        suffixes=('_reg', '_log')
    )
)
