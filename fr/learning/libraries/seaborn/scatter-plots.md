# Diagrammes de dispersion

Les **diagrammes de dispersion**, aussi appelés nuages de points (*scatter plots en anglais*), sont l’un des outils les plus fondamentaux en analyse exploratoire des données (EDA). Ils permettent de **visualiser la relation entre deux variables continues**.

## Variables continues vs variables catégorielles

### Variables continues

Une **variable continue** est une variable numérique qui peut prendre une **infinité de valeurs possibles** dans un intervalle (âge, taille, salaire, température, prix, distance etc.)

:::tip Exemple
Un âge de 28 ans peut être affiné :
* 28 ans
* 28 ans et 2 mois
* 28 ans, 2 mois et 1 semaine

➡️ On peut toujours diviser l’unité de mesure.
:::

### Variables catégorielles

Une **variable catégorielle** représente des catégories **distinctes et non continues**.

:::tip Exemple
* niveau d’éducation (lycée, bachelor, master)
* couleur (rouge, vert, bleu)
* forme (carré, triangle, cercle)
* noms (Marc, Claire, Vincent)

➡️ Il n’existe pas de valeur intermédiaire entre deux catégories.
:::

## À quoi sert un diagramme de dispersion ?

Un diagramme de dispersion permet de :
* visualiser la **relation entre deux variables continues**
* détecter des **tendances**
* identifier des **corrélations**
* repérer des **valeurs aberrantes (outliers)**

## Exemple conceptuel

Imaginons une entreprise avec des commerciaux. Variables disponibles :
* **Salaire** (numérique continu)
* **Ventes annuelles** (numérique continu)
* **Expérience professionnelle**
* **Niveau d’éducation**

> ❓ QUESTION : existe-t-il une relation entre le salaire et les ventes ?

:::info VISUALISATION
Chaque point représente un employé.

<img src="/learning/libraries/seaborn-scatter-plots-1.png" style="display: block; margin: 0 auto;width: 70%; height: auto;">

* Axe X → salaire
* Axe Y → ventes
> Si les points montent globalement vers la droite, cela suggère une relation positive : plus les ventes sont élevées, plus le salaire tend à augmenter.

Seaborn peut ensuite ajouter de la couleur et du style
<img src="/learning/libraries/seaborn-scatter-plots-2.png" style="display: block; margin: 0 auto;width: 70%; height: auto;">
:::