import matplotlib.pyplot as plt
import numpy as np

"""
Introduction à l'API orientée objet de Matplotlib

Cette méthode consiste à créer des objets Figure, puis à ajouter des objets Axes sur lesquels tracer des données.
Elle offre un contrôle plus fin et permet des visualisations complexes avec plusieurs tracés.
"""

# -----------------------------------------------------------
# Données
# -----------------------------------------------------------
a = np.linspace(0, 10, 11)  # Tableau de 0 à 10, 11 points
b = a ** 4                  # Puissance 4
x = np.arange(0, 10)        # Tableau de 0 à 9
y = 2 * x                    # Relation linéaire

# -----------------------------------------------------------
# Création d'une Figure simple avec un axe
# -----------------------------------------------------------
fig = plt.figure()  # Canevas vide
axes = fig.add_axes([0, 0, 1, 1])  # Ajouter un axe couvrant toute la figure
axes.plot(x, y)  # Tracé linéaire simple
axes.set_xlabel('X')
axes.set_ylabel('Y')
axes.set_title('Tracé simple sur un axe')
plt.show()

# -----------------------------------------------------------
# Tracé avec des données plus complexes
# -----------------------------------------------------------
fig = plt.figure()
axes = fig.add_axes([0, 0, 1, 1])
axes.plot(a, b)
axes.set_xlabel('X')
axes.set_ylabel('Y')
axes.set_title('Tracé de a^4')
plt.show()

# -----------------------------------------------------------
# Ajout d'un deuxième axe sur la même figure
# -----------------------------------------------------------
fig = plt.figure()
axes1 = fig.add_axes([0, 0, 1, 1])      # Axe principal
axes2 = fig.add_axes([0.2, 0.2, 0.5, 0.5])  # Axe secondaire plus petit

axes1.plot(a, b)
axes1.set_xlabel('X')
axes1.set_ylabel('Y')
axes1.set_title('Grande figure')

axes2.plot(a, b)
axes2.set_title('Petite figure')
plt.show()

# -----------------------------------------------------------
# Déplacement et zoom sur le petit axe
# -----------------------------------------------------------
fig = plt.figure()
axes1 = fig.add_axes([0, 0, 1, 1])        # Axe principal
axes2 = fig.add_axes([0.2, 0.5, 0.25, 0.25])  # Axe secondaire repositionné

axes1.plot(a, b)
axes1.set_xlabel('X')
axes1.set_ylabel('Y')
axes1.set_title('Grande figure')

axes2.plot(a, b)
axes2.set_xlim(8, 10)
axes2.set_ylim(4000, 10000)
axes2.set_xlabel('X')
axes2.set_ylabel('Y')
axes2.set_title('Zoom avant')
plt.show()

# -----------------------------------------------------------
# Ajouter un axe en dehors de la figure principale
# -----------------------------------------------------------
fig = plt.figure()
axes1 = fig.add_axes([0, 0, 1, 1])
axes2 = fig.add_axes([0.2, 0.5, 0.25, 0.25])
axes3 = fig.add_axes([1, 1, 0.25, 0.25])  # Déborde du canevas

axes1.plot(a, b)
axes1.set_xlabel('X')
axes1.set_ylabel('Y')
axes1.set_title('Grande figure')

axes2.plot(a, b)
axes2.set_xlim(8, 10)
axes2.set_ylim(4000, 10000)
axes2.set_xlabel('X')
axes2.set_ylabel('Y')
axes2.set_title('Zoom avant')

axes3.plot(a, b)
axes3.set_title('Hors canevas')
plt.show()

# -----------------------------------------------------------
# Paramètres globaux de la figure
# -----------------------------------------------------------
fig = plt.figure(figsize=(12, 8), dpi=100)
axes = fig.add_axes([0, 0, 1, 1])
axes.plot(a, b)
axes.set_title('Figure personnalisée avec figsize et dpi')
plt.show()

# -----------------------------------------------------------
# Exporter une figure
# -----------------------------------------------------------
fig = plt.figure()
axes = fig.add_axes([0, 0, 1, 1])
axes.plot(a, b)
axes.set_xlabel('X')
axes.set_title('Exportation de figure')
fig.savefig('figure.png', bbox_inches='tight')  # Sauvegarde propre avec marges ajustées

# -----------------------------------------------------------
# Exemple complet avec deux axes et exportation
# -----------------------------------------------------------
fig = plt.figure(figsize=(12, 8))
axes1 = fig.add_axes([0, 0, 1, 1])
axes2 = fig.add_axes([1, 1, 0.25, 0.25])

axes1.plot(x, y)
axes1.set_title('Grand axe')
axes2.plot(x, y)
axes2.set_title('Petit axe hors canevas')

fig.savefig('test.png', bbox_inches='tight')
