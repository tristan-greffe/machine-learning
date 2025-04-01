# [Pandas](https://pandas.pydata.org/docs/#)

Pandas est la bibliothèque **open source** de référence pour la manipulation et l’analyse de données en Python.

Elle est utilisée principalement dans les étapes de nettoyage et organisation des données (`3`) et d'analyse exploratoire (`4`)

![Data Science & Machine Learning](/learning/general-route.svg)

Elle fournit des structures de données puissantes et flexibles, en particulier :

* **Series** → données 1D (vecteurs avec index)
* **DataFrame** → données 2D (tableaux de type tableur)

## Pourquoi utiliser Pandas ?

### 1. Manipulation efficace des données tabulaires

La majorité des données réelles sont tabulaires :

* fichiers CSV
* fichiers Excel
* tables SQL
* données issues d’API ou de pages web

::: info
Pandas est conçu spécifiquement pour ce type de données :

* sélection de colonnes et de lignes
* filtrage conditionnel
* tri, regroupement et agrégation
* transformation et restructuration des tables
:::

### 2. Gestion des données manquantes

Les données réelles sont presque toujours incomplètes. Pandas fournit des outils simples et robustes pour :

* détecter les valeurs manquantes
* les supprimer ou les remplacer
* adapter les analyses à ces absences de données

### 3. Analyse exploratoire des données (EDA)

Pandas permet de :

* calculer rapidement des statistiques descriptives
* explorer les distributions des variables
* comprendre les relations entre colonnes
* préparer les données pour la visualisation

::: info
Il constitue souvent la première étape concrète d’une analyse de données.
:::

### 4. Lecture et écriture de nombreux formats

Pandas peut lire et écrire des données dans une grande variété de formats :

* CSV
* Excel
* JSON
* HTML (tables)
* bases de données SQL
* fichiers Parquet, Feather, etc.

::: info
Si un autre outil peut exporter des données,
il y a de fortes chances que Pandas puisse les importer.
:::

### 5. Alternative robuste aux tableurs classiques

Pandas est parfois décrit comme un “*Excel pour Python*”, mais il va bien au-delà :

* pas de limite stricte sur la taille des données (hors RAM)
* reproductibilité totale des analyses
* automatisation facile
* intégration directe avec le code et le machine learning

::: info
Dans de nombreux contextes professionnels, les fichiers sont trop volumineux pour être ouverts dans un tableur classique, mais parfaitement exploitables avec Pandas.
:::

## Pandas & Machine Learning

Avant d’entraîner un modèle, les données doivent être :

* nettoyées
* structurées
* filtrées
* transformées

Pandas est l’outil principal pour :

* créer les matrices de features
* préparer les variables cibles
* effectuer les transformations nécessaires
* transmettre les données à NumPy ou Scikit-learn

::: info
Un bon Data Scientist passe souvent plus de temps dans Pandas que dans les algorithmes de Machine Learning eux-mêmes.
:::