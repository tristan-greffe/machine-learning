# Input & Output

Pandas peut lire et écrire des données depuis de nombreuses sources : fichiers CSV, tables HTML, fichiers Excel, bases de données SQL, etc.

::: tip 👉 **Objectif principal**
comprendre la logique générale  
- `pd.read_*()` → lire des données  
- `df.to_*()` → écrire des données  
:::

## Lecture et écriture de fichiers CSV

Avant de lire un fichier CSV, vous devez :
- connaître **l’emplacement exact du fichier**
- connaître **le nom exact du fichier**
- comprendre le **répertoire de travail courant**

::: details Lire un fichier CSV
```python
import pandas as pd

df = pd.read_csv("example.csv")
```
Options courantes :

```python
pd.read_csv("example.csv", header=None)     # pas d'en-tête
pd.read_csv("example.csv", index_col=0)     # définir une colonne comme index
```
:::

::: details Écrire un fichier CSV
```python
df.to_csv("nouveau_fichier.csv")
```

Options importantes :

```python
df.to_csv("nouveau_fichier.csv", index=False)
```
:::

::: tip ⚠️
Par défaut, Pandas **sauvegarde l’index** dans le fichier CSV.
:::

## Lecture et écriture de tables HTML

Pandas peut lire automatiquement les tableaux HTML (`<table>`) présents dans :
- une **URL**
- un **fichier HTML local**

::: tip ⚠️
- tous les tableaux ne sont pas lisibles (JavaScript, images, formats dynamiques)
- certains sites peuvent bloquer l’accès
:::

::: details Lire des tableaux HTML depuis une URL
```python
url = "https://en.wikipedia.org/wiki/World_population"
tables = pd.read_html(url)
```

- Le résultat est **toujours une liste**
- Chaque élément est un DataFrame

```python
len(tables)
tables[0]
```
:::

::: details  Nettoyage d’un tableau HTML
```python
df = tables[0]

# supprimer des lignes
df = df.drop(index=11)

# supprimer une colonne
df = df.drop(columns="#")

# renommer les colonnes
df.columns = ["Pays", "2000", "2015", "Estimation 2030"]
```
:::

::: details  Écrire un DataFrame en HTML
```python
df.to_html("table_population.html", index=False)
```
:::

## Lire un fichier Excel

```python
df = pd.read_excel("my_excel_file.xlsx", sheet_name="First Sheet")
```

::: details  Lister les feuillets d’un fichier Excel
```python
xls = pd.ExcelFile("my_excel_file.xlsx")
xls.sheet_names
```
:::

::: details  Lire tous les feuillets (dictionnaire)
```python
sheets_dict = pd.read_excel(
    "my_excel_file.xlsx",
    sheet_name=None
)
```
- **clé** → nom du feuillet
- **valeur** → DataFrame

```python
sheets_dict["First Sheet"]
```
:::

::: details Écrire un DataFrame dans un fichier Excel
```python
df.to_excel(
    "example.xlsx",
    sheet_name="First Sheet",
    index=False
)
```
⚠️ Si le fichier existe déjà, Pandas **écrase le feuillet**.
:::

## Fichier Python associé

:::details input & output
<<< ../../../../public/learning/libraries/panda_input_output.py
:::
