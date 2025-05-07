"""
Analyse exploratoire d'un dataset de réservations hôtelières avec Pandas

Objectifs :
- Manipulation de DataFrames
- Nettoyage des données
- Filtrage conditionnel
- Statistiques descriptives
- Feature engineering simple
"""

import pandas as pd
import numpy as np

# ======================================================
# 1. Chargement des données
# ======================================================

URL = "https://raw.githubusercontent.com/moncoachdata/MasterClass_DS_ML/main/hotel_booking_data.csv"
hotels = pd.read_csv(URL)

print("Dataset chargé avec succès")
print(f"Nombre total de lignes : {len(hotels)}\n")

# ======================================================
# 2. Données manquantes
# ======================================================

missing_values = hotels.isna().sum()
print("Valeurs manquantes par colonne :")
print(missing_values.sort_values(ascending=False), "\n")

most_missing_col = missing_values.idxmax()
print(
    f"La colonne avec le plus de valeurs manquantes est '{most_missing_col}' "
    f"avec {missing_values.max()} valeurs manquantes.\n"
)

# Suppression de la colonne trop incomplète
hotels.drop(columns="company", inplace=True)

# ======================================================
# 3. Analyse descriptive simple
# ======================================================

# 5 pays les plus représentés
print("Top 5 des pays les plus fréquents :")
print(hotels["country"].value_counts().head(), "\n")

# ======================================================
# 4. Tarif journalier moyen (ADR)
# ======================================================

# Personne ayant payé l'ADR le plus élevé
max_adr_row = hotels.loc[hotels["adr"].idxmax()]
print(
    f"ADR maximum payé par : {max_adr_row['name']} "
    f"({max_adr_row['adr']} €)\n"
)

# ADR moyen sur l'ensemble des séjours
mean_adr = round(hotels["adr"].mean(), 2)
print(f"ADR moyen sur l'ensemble des séjours : {mean_adr} €\n")

# ======================================================
# 5. Durée et coût des séjours
# ======================================================

# Durée totale du séjour
hotels["total_stay_days"] = (
    hotels["stays_in_week_nights"] + hotels["stays_in_weekend_nights"]
)

mean_stay = round(hotels["total_stay_days"].mean(), 2)
print(f"Durée moyenne d’un séjour : {mean_stay} nuits\n")

# Coût total du séjour
hotels["total_paid"] = hotels["adr"] * hotels["total_stay_days"]
mean_total_paid = round(hotels["total_paid"].mean(), 2)
print(f"Coût total moyen d’un séjour : {mean_total_paid} €\n")

# ======================================================
# 6. Filtrage conditionnel
# ======================================================

# Clients avec 5 demandes spéciales
special_requests = hotels.loc[
    hotels["total_of_special_requests"] == 5, ["name", "email"]
]

print("Clients ayant effectué 5 demandes spéciales :")
print(special_requests.head(), "\n")

# Pourcentage de clients réguliers
repeat_guest_percentage = round(
    100 * (hotels["is_repeated_guest"] == 1).sum() / len(hotels), 2
)
print(f"Pourcentage de clients réguliers : {repeat_guest_percentage} %\n")

# ======================================================
# 7. Analyse des noms
# ======================================================

# Extraction du nom de famille
last_names = hotels["name"].apply(lambda x: x.split()[-1])

print("Top 5 des noms de famille les plus fréquents :")
print(last_names.value_counts().head(), "\n")

# ======================================================
# 8. Enfants et bébés
# ======================================================

hotels["total_kids"] = hotels["children"] + hotels["babies"]

print("Personnes ayant réservé pour le plus grand nombre d’enfants/bébés :")
print(
    hotels.sort_values("total_kids", ascending=False)[
        ["name", "adults", "children", "babies", "total_kids"]
    ].head(3),
    "\n"
)

# ======================================================
# 9. Analyse des numéros de téléphone
# ======================================================

print("Top 3 des indicatifs téléphoniques :")
print(
    hotels["phone-number"]
    .astype(str)
    .str[:3]
    .value_counts()
    .head(3),
    "\n"
)

# ======================================================
# 10. Analyse des dates d’arrivée
# ======================================================

# Arrivées entre le 1er et le 15 inclus
arrivals_1_15 = hotels["arrival_date_day_of_month"].between(1, 15).sum()
print(f"Nombre d’arrivées entre le 1er et le 15 du mois : {arrivals_1_15}\n")

# ======================================================
# 11. Jour de la semaine des arrivées
# ======================================================

# Création d'une vraie date
hotels["arrival_date"] = pd.to_datetime(
    hotels["arrival_date_day_of_month"].astype(str)
    + "-"
    + hotels["arrival_date_month"]
    + "-"
    + hotels["arrival_date_year"].astype(str),
    dayfirst=True,
)

print("Nombre d’arrivées par jour de la semaine :")
print(hotels["arrival_date"].dt.day_name().value_counts())
