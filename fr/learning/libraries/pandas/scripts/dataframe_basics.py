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
df = pd.read_csv('./data/tips.csv')
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

# ======================================================
# 6. Filtrage conditionnel
# ======================================================

print("=== Filtrage conditionnel : une seule condition ===\n")
# Exemple : total_bill > 40
condition1 = df['total_bill'] > 40
print("Série booléenne pour total_bill > 40 :\n", condition1.head(), "\n")

# Appliquer le filtre
df_filtered1 = df[condition1]
print("Lignes où total_bill > 40 :\n", df_filtered1.head(), "\n")

# Filtrage direct sans variable intermédiaire
df_filtered_direct = df[df['total_bill'] > 40]
print("Filtrage direct total_bill > 40 :\n", df_filtered_direct.head(), "\n")

# Exemple : filtrage sur une colonne catégorielle
df_filtered2 = df[df['sex'] == 'Male']
print("Lignes où sex = 'Male' :\n", df_filtered2.head(), "\n")

# ======================================================
print("=== Filtrage conditionnel : conditions multiples ===\n")
# Exemple : total_bill > 30 ET sex = 'Male'
df_filtered_and = df[(df['total_bill'] > 30) & (df['sex'] == 'Male')]
print("total_bill > 30 ET sex = 'Male' :\n", df_filtered_and.head(), "\n")

# Exemple : total_bill > 30 OU sex = 'Female'
df_filtered_or = df[(df['total_bill'] > 30) | (df['sex'] == 'Female')]
print("total_bill > 30 OU sex = 'Female' :\n", df_filtered_or.head(), "\n")

# ======================================================
print("=== Filtrage conditionnel : plusieurs valeurs avec isin ===\n")
# Exemple : filtrer les jours du week-end (Saturday, Sunday)
weekend_days = ['Saturday', 'Sunday']
df_filtered_weekend = df[df['day'].isin(weekend_days)]
print("Lignes correspondant au week-end :\n", df_filtered_weekend.head(), "\n")

# Ajouter un jour supplémentaire (Friday)
days_filter = ['Friday', 'Saturday', 'Sunday']
df_filtered_days = df[df['day'].isin(days_filter)]
print("Lignes correspondant à Friday, Saturday ou Sunday :\n", df_filtered_days.head(), "\n")

# ======================================================
# 7. Méthodes utiles : apply sur une seule colonne
# ======================================================

print("=== Méthode apply : appliquer une fonction custom sur une colonne ===\n")

# Exemple 1 : extraire les 4 derniers chiffres d'une colonne 'cc_number' (numéro de carte)
# On crée une fonction custom
def last_four(num):
    """Retourne les 4 derniers chiffres d'un nombre en tant que chaîne"""
    return str(num)[-4:]

# Vérification rapide de la fonction
print("Test fonction last_four sur un nombre :", last_four(123456789), "\n")

# Application de la fonction à la colonne 'cc_number' via apply
# Attention : cette colonne doit exister dans votre DataFrame df
if 'cc_number' in df.columns:
    df['last_four'] = df['cc_number'].apply(last_four)
    print("Exemple d'application de last_four sur la colonne 'cc_number' :\n", df[['cc_number', 'last_four']].head(), "\n")
else:
    print("Colonne 'cc_number' non présente dans df. Passez à l'exemple suivant.\n")

# Exemple 2 : catégoriser le total_bill en $ (low, medium, high) avec apply
def categorize_price(price):
    """Retourne un label $ en fonction du prix"""
    if price < 10:
        return '$'
    elif 10 <= price < 30:
        return '$$'
    else:
        return '$$$'

# Application de la fonction sur la colonne 'total_bill'
df['price_category'] = df['total_bill'].apply(categorize_price)
print("DataFrame avec nouvelle colonne 'price_category' :\n", df[['total_bill', 'price_category']].head(), "\n")

# Note pédagogique :
print("""
💡 Points clés sur l'utilisation de apply sur une seule colonne :
- La fonction passée à apply doit prendre en entrée **une seule valeur** (une ligne de la série)
- La fonction doit **retourner une seule valeur**, pas une série
- Très utile pour transformer ou créer de nouvelles colonnes à partir d'une colonne existante
""")

# ======================================================
# 8. Méthodes utiles : apply sur des colonnes multiples
# ======================================================

print("=== Méthode apply : appliquer une fonction sur plusieurs colonnes ===\n")

# ------------------------------------------------------
# Rappel : expression lambda
# ------------------------------------------------------
# lambda x: x * 2
# Fonction anonyme à usage unique, très utilisée avec apply


# ------------------------------------------------------
# Exemple : évaluer la qualité du pourboire
# Colonnes utilisées : total_bill et tip
# ------------------------------------------------------

def tip_quality(total_bill, tip):
    """
    Évalue la qualité du pourboire en fonction du ratio tip / total_bill
    """
    if (tip / total_bill) > 0.25:
        return "Généreux"
    else:
        return "Standard"


# Test rapide de la fonction
print("Test tip_quality :", tip_quality(16.99, 1.01), "\n")


# ------------------------------------------------------
# Méthode 1 : apply + lambda (axis=1)
# ------------------------------------------------------
df['tip_quality_apply'] = df[['total_bill', 'tip']].apply(
    lambda row: tip_quality(row['total_bill'], row['tip']),
    axis=1
)

print("Résultat avec apply + lambda :\n",
      df[['total_bill', 'tip', 'tip_quality_apply']].head(), "\n")


# ------------------------------------------------------
# Méthode 2 : np.vectorize (plus lisible et souvent plus rapide)
# ------------------------------------------------------
import numpy as np

df['tip_quality_vectorized'] = np.vectorize(tip_quality)(
    df['total_bill'],
    df['tip']
)

print("Résultat avec np.vectorize :\n",
      df[['total_bill', 'tip', 'tip_quality_vectorized']].head(), "\n")


# ------------------------------------------------------
# Notes pédagogiques importantes
# ------------------------------------------------------
print("""
💡 Points clés à retenir :
- apply sur plusieurs colonnes nécessite axis=1
- La fonction custom doit retourner UNE seule valeur par ligne
- lambda est pratique pour des appels ponctuels
- np.vectorize rend une fonction Python "consciente" de NumPy
- np.vectorize améliore souvent la lisibilité et parfois les performances
""")

# ======================================================
# 9. Méthodes utiles : informations statistiques et tri
# ======================================================

print("=== Informations statistiques et tri de données ===\n")

# ------------------------------------------------------
# Statistiques descriptives
# ------------------------------------------------------
print("Description statistique du DataFrame :\n")
print(df.describe().T, "\n")  # Transposé pour meilleure lisibilité


# ------------------------------------------------------
# Tri des données
# ------------------------------------------------------
print("Tri par pourboire (tip) croissant :\n")
print(df.sort_values('tip').head(), "\n")

print("Tri par pourboire décroissant :\n")
print(df.sort_values('tip', ascending=False).head(), "\n")

print("Tri sur plusieurs colonnes (tip puis size) :\n")
print(df.sort_values(['tip', 'size']).head(), "\n")


# ------------------------------------------------------
# Valeurs min / max et leurs index
# ------------------------------------------------------
max_total = df['total_bill'].max()
idx_max = df['total_bill'].idxmax()

min_total = df['total_bill'].min()
idx_min = df['total_bill'].idxmin()

print(f"Max total_bill = {max_total} à l'index {idx_max}")
print(df.loc[idx_max], "\n")

print(f"Min total_bill = {min_total} à l'index {idx_min}")
print(df.loc[idx_min], "\n")


# ------------------------------------------------------
# Corrélation entre colonnes numériques
# ------------------------------------------------------
print("Matrice de corrélation :\n")
print(df.corr(numeric_only=True), "\n")


# ------------------------------------------------------
# Comptage de valeurs catégorielles
# ------------------------------------------------------
print("Répartition par sexe :\n")
print(df['sex'].value_counts(), "\n")

print("Valeurs uniques pour 'day' :\n")
print(df['day'].unique(), "\n")

print("Nombre de jours uniques :")
print(df['day'].nunique(), "\n")


# ------------------------------------------------------
# Remplacement de valeurs : replace
# ------------------------------------------------------
print("Remplacement des valeurs de 'sex' avec replace :\n")
print(df['sex'].replace(['Female', 'Male'], ['F', 'M']).head(), "\n")


# ------------------------------------------------------
# Remplacement de valeurs : map (recommandé)
# ------------------------------------------------------
sex_mapping = {
    'Female': 'F',
    'Male': 'M'
}

print("Remplacement des valeurs de 'sex' avec map :\n")
print(df['sex'].map(sex_mapping).head(), "\n")


# ------------------------------------------------------
# Détection et suppression de doublons
# ------------------------------------------------------
print("Présence de doublons :")
print(df.duplicated().any(), "\n")

# Exemple pédagogique
simple_df = pd.DataFrame([1, 2, 2, 2], index=['A', 'B', 'C', 'D'])
print("DataFrame avec doublons :\n", simple_df, "\n")

print("Lignes dupliquées :\n")
print(simple_df.duplicated(), "\n")

print("Suppression des doublons :\n")
print(simple_df.drop_duplicates(), "\n")


# ------------------------------------------------------
# Filtrage par intervalle avec between
# ------------------------------------------------------
between_filter = df['total_bill'].between(10, 20, inclusive='both')

print("Notes totales entre 10 et 20 $ :\n")
print(df[between_filter].head(), "\n")


# ------------------------------------------------------
# nlargest et nsmallest
# ------------------------------------------------------
print("Top 5 des pourboires les plus élevés :\n")
print(df.nlargest(5, 'tip'), "\n")

print("Top 5 des pourboires les plus faibles :\n")
print(df.nsmallest(5, 'tip'), "\n")


# ------------------------------------------------------
# Échantillonnage aléatoire (sampling)
# ------------------------------------------------------
print("Échantillon aléatoire de 5 lignes :\n")
print(df.sample(5), "\n")

print("Échantillon aléatoire de 10% du DataFrame :\n")
print(df.sample(frac=0.1), "\n")


print("""
💡 Points clés à retenir :
- describe() donne une vue statistique rapide
- sort_values() permet le tri simple ou multi-colonnes
- idxmax() / idxmin() donnent la position des valeurs extrêmes
- value_counts(), unique(), nunique() sont essentiels pour les catégories
- map() est plus lisible que replace() pour de nombreux remplacements
- duplicated() et drop_duplicates() gèrent les doublons
- between(), nlargest(), nsmallest() simplifient les filtres
- sample() permet l’échantillonnage aléatoire
""")
