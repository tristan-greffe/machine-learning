# Concepts fondamentaux du Machine Learning

Quand on parle d’intelligence artificielle (IA), on met souvent tout dans le même sac.  
En réalité, il existe **plusieurs grandes familles de modèles**, qui se distinguent par **ce qu’ils font** et **comment ils apprennent**.

:::info
Les modèles de génération (texte, images, audio…) ne représentent **qu’une partie** de l’écosystème.
:::

## Qu’est-ce que le Machine Learning ?

Le **Machine Learning (ML)** est un sous-domaine de l’intelligence artificielle qui permet aux machines **d’apprendre automatiquement à partir de données**, sans être explicitement programmées.

Au lieu d’écrire des règles manuelles, on fournit :
- des données
- un objectif
- un algorithme

:::info
Le modèle apprend alors les règles **par lui-même**
:::

## Les grandes familles de modèles

Chaque famille répond à une **question fondamentale différente**.

### Modèles de classification
👉 *« C’est quoi ? »*

Décider dans quelle **catégorie** appartient une donnée.

:::details **Exemples**
- Email → spam / non spam
- Image → chat / chien
- Transaction → fraude / normale
:::

### Modèles de régression
👉 *« Combien ? »*

Prédire une **valeur numérique continue**.

:::details **Exemples**
- Prix d’un appartement
- Temps de livraison
- Consommation électrique
:::

### Modèles de clustering (non supervisés)
👉 *« Qui ressemble à qui ? »*

Regrouper les données **sans labels**.

:::details **Exemples**
- Segmentation client
- Regroupement d’articles
- Analyse de comportements
:::

### Modèles de détection d’anomalies
👉 *« Qu’est-ce qui est anormal ? »*

Identifier les comportements atypiques.

:::details **Exemples**
- Fraude bancaire
- Pannes industrielles
- Intrusions réseau
:::

### Modèles de recommandation
👉 *« Qu’est-ce qui pourrait t’intéresser ? »*

Proposer du contenu pertinent.

:::details **Exemples**
- Netflix
- Spotify
- Amazon
:::

### Modèles de réduction de dimension
👉 *« Comment simplifier ? »*

Réduire le nombre de variables tout en conservant l’essentiel.

:::details **Objectifs**
- Visualisation
- Accélération des modèles
- Compression
:::

### Modèles de séries temporelles
👉 *« Que va-t-il se passer ? »*

Prédire le futur à partir du passé.

:::details **Exemples**
- Prévisions de ventes
- Charge serveur
- Météo
:::

### Apprentissage par renforcement
👉 *« Quelle action choisir ? »*

Apprendre par **essai-erreur** à l’aide de récompenses.

:::details **Concepts clés**
- Agent
- Environnement
- Récompense
- Politique
:::

### Modèles de génération
👉 *« Que puis-je créer ? »*

Créer du **nouveau contenu**.

:::details **Exemples**
- Texte
- Images
- Audio
- Code
:::

## Les types d’apprentissage

| Type | Données utilisées | Objectif |
|----|----|----|
| Supervisé | Étiquetées | Prédire |
| Non supervisé | Non étiquetées | Découvrir |
| Renforcement | Récompenses | Décider |


## Fonctionnement d’un projet de Machine Learning

1. Collecte des données  
2. Nettoyage et préparation  
3. Choix du modèle  
4. Entraînement  
5. Évaluation  
6. Amélioration  
7. Déploiement  

:::tip L’importance des données

> *Un modèle n’est jamais meilleur que ses données.*

Qualité, volume et représentativité sont essentiels.
:::