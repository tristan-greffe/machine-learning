import matplotlib.pyplot as plt
import numpy as np

# ======================================================
# Exemple de base : Tracé simple d'un tableau
# ======================================================
# Ici, nous allons créer un graphique très simple en utilisant deux tableaux NumPy.
# Vous pouvez aussi utiliser des listes Python ou des colonnes Pandas, qui se comportent comme des tableaux.

# Création des données
x = np.arange(0, 10)  # Tableau de 0 à 9
y = 2 * x             # Relation linéaire : y = 2*x

# ======================================================
# 1. Tracé de base avec plt.plot()
# ======================================================
# Commandes Matplotlib de base pour créer un graphique linéaire

plt.plot(x, y)                       # Tracer X vs Y
plt.xlabel("Axe X")                  # Label de l'axe X
plt.ylabel("Axe Y")                  # Label de l'axe Y
plt.title("Graphique linéaire simple") # Titre du graphique
plt.show()                            # Afficher le graphique
# Note : plt.show() est nécessaire si vous utilisez un script .py. 
# Dans un notebook Jupyter ou Google Colab, le graphique s'affiche automatiquement, mais show() permet de supprimer l'objet Out[].

# ======================================================
# 2. Modification des limites des axes
# ======================================================
# Vous pouvez définir les limites pour zoomer sur une partie spécifique du graphique
plt.plot(x, y)
plt.xlabel("Axe X")
plt.ylabel("Axe Y")
plt.title("Graphique avec limites d'axes")
plt.xlim(0, 6)   # Limite de l'axe X : de 0 à 6
plt.ylim(0, 12)  # Limite de l'axe Y : de 0 à 12
plt.show()

# ======================================================
# 3. Exportation d'un graphique
# ======================================================
# Pour sauvegarder votre graphique dans un fichier image (PNG, JPEG, PDF, etc.)
# La fonction plt.savefig() permet de contrôler le format, le dpi, et le chemin de sauvegarde

plt.plot(x, y)
plt.xlabel("Axe X")
plt.ylabel("Axe Y")
plt.title("Graphique sauvegardé")
plt.savefig("example.png")  # Enregistre le graphique dans le fichier 'example.png'
plt.show()

# Pour plus d'informations sur savefig
help(plt.savefig)
