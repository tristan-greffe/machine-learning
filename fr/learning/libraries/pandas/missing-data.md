# Les données manquantes avec Pandas

Les **données manquantes** sont omniprésentes dans les jeux de données réels.
Elles peuvent provenir de nombreuses causes :
* erreurs de saisie
* données non collectées
* capteurs défaillants
* valeurs non applicables (ex : prix = 0 mais enregistré comme manquant)

:::info
Beaucoup de méthodes statistiques et de modèles de machine learning ne fonctionnent pas avec des valeurs manquantes, ce qui rend leur gestion indispensable.
:::

## Comment Pandas représente les données manquantes

Dans Pandas, les valeurs manquantes sont représentées par :

* `NaN` *(Not a Number)* → données numériques
* `pd.NA` → valeur manquante générique (versions récentes)
* `NaT` *(Not a Time)* → données temporelles (timestamps)

:::info
Pour la majorité des cas pratiques, NaN, NA et NaT sont traités de la même manière.
:::

::: tip ⚠️ Comparaison et valeurs manquantes
Il est **incorrect** de tester une valeur manquante avec `==`
```py
np.nan == np.nan   # False
```
👉 Logique : deux valeurs inconnues ne peuvent pas être comparées.
| Méthode | Rôle |
|---------|------|
| `isna()` / `isnull()` | détecter les valeurs manquantes |
| `notna()` / `notnull()` | détecter les valeurs présentes |
:::

## Les 3 stratégies possibles face aux données manquantes

Il n’existe **pas de solution universelle**. Le choix dépend toujours du **contexte métier et des objectifs**.

### 1️⃣ Conserver les données manquantes

👉 Ne rien faire

| Avantages | Inconvénients |
|---------|------|
| aucune modification des données | incompatible avec beaucoup d’algorithmes |
| méthode la plus simple | peut bloquer un pipeline ML |
| respecte la réalité du dataset |  |

::: tip 📌 À utiliser si :
* les méthodes suivantes acceptent les NaN
* la valeur manquante a un sens en soi
:::

### 2️⃣ Supprimer les données manquantes

On peut supprimer :
* des **lignes** (observations) : Utile si une observation contient trop peu d’informations exploitables
* des **colonnes** (features) : Pertinent si la majorité des valeurs de cette feature sont manquantes.

::: tip ⚠️ Risque majeur
perte d’information et limitation des modèles futurs.
:::

::: info **Exemple** 
<div style="display: flex; gap: 2rem;">
<div style="flex: 1">
supprimer la ligne USA : 

| Index | Year | Pop | GDP |
|---------|------|---------|------|
| USA | 1776 | NAN | NAN |
| CANADA | 1867 | 38 | 1.7 |
| MEXICO | 1821 | 126 | 1.22 |
</div>
<div style="flex: 1">
supprimer la colonne GDP : 

| Index | Year | Pop | GDP |
|---------|------|---------|------|
| USA | 1776 | 328 | NAN |
| CANADA | 1867 | 38 | NAN |
| MEXICO | 1821 | 126 | 1.22 |
</div>
</div>
:::

### 3️⃣ Remplacer / compéter (imputer) les données manquantes

Méthode la plus **complexe**, mais souvent la plus **utile**.

| Remplacement simple | Remplacement statistique | Interpolation |
|---------|------|------|
| 0 (valeur logique : ex. aucun porte-avions) | moyenne | linéaire |
| catégorie par défaut | médiane | temporelle |
| valeur fixe | mode | ordonnée |

::: tip ⚠️ Attention
Remplir = inventer une valeur
Cela doit être justifié par le contexte métier.
:::

::: info **Exemple** 
Remplacement par 0 :
<div style="display: flex; gap: 2rem;">
<div style="flex: 1">

| Index | Year | Pop | GDP |
|---------|------|---------|------|
| USA | 1776 | 328 | 20.5 |
| CANADA | 1867 | 38 | NAN |
| MEXICO | 1821 | 126 | NAN |
</div>
<div style="flex: 1">

| Index | Year | Pop | GDP |
|---------|------|---------|------|
| USA | 1776 | 328 | 20.5 |
| CANADA | 1867 | 38 | 0 |
| MEXICO | 1821 | 126 | 0 |
</div>
</div>

Remplacement avec une valeur interpolée ou estimée :
<div style="display: flex; gap: 2rem;">
<div style="flex: 1">

| Index | Year | Pop | GDP | Perct
|---------|------|---------|------|------|
| USA | 1776 | 328 | 20.5 | 75% |
| CANADA | 1867 | 38 | 1.7 | NAN |
| MEXICO | 1821 | 126 | 1.22 | 25% |
</div>
<div style="flex: 1">

| Index | Year | Pop | GDP | Perct
|---------|------|---------|------|------|
| USA | 1776 | 328 | 20.5 | 75% |
| CANADA | 1867 | 38 | 1.7 | 50% |
| MEXICO | 1821 | 126 | 1.22 | 25% |
</div>
</div>
:::

## Fichier Python associé

:::details missing data
<<< ../../../../public/learning/libraries/missing_data_basics.py
:::
