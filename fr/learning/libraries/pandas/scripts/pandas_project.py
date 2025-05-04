import pandas as pd

url = 'https://raw.githubusercontent.com/moncoachdata/MasterClass_DS_ML/main/hotel_booking_data.csv'
hotels = pd.read_csv(url)

#hotels.head()
#hotels.info()

# Combien y-a-t-il de lignes ? 119389

print(len(hotels))

# Y a-t-il des données manquantes ? Si oui, quelle colonne a le plus de données manquantes ?

print(hotels.isnull().sum())
print(f"Oui, il y a des données manquantes, la colonne company a le plus de données manquantes : {hotels['company'].isna().sum()} points de données manquants.")

# Supprimer la colonne "company" de l'ensemble de données

hotels = hotels.drop('company', axis=1)
print(hotels.head())

# Quels sont les 5 codes pays les plus fréquents dans l'ensemble de données ?
print(hotels['country'].value_counts()[:5])

# Quel est le nom de la personne qui a payé le tarif journalier moyen le plus élevé ? Quel était ce montant ?**
# taux/tarif journalier moyen = adr (Average Daily Rate)

