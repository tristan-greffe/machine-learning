import matplotlib.pyplot as plt
import numpy as np

# ===========================================================
# Données
# ===========================================================
x = np.arange(0, 10)
y = 2 * x

# ===========================================================
# LÉGENDES
# ===========================================================
"""
On ajoute une légende en deux étapes :
1) fournir un argument label à chaque tracé
2) appeler la méthode legend() sur l'objet Axes

Attention : la légende peut parfois chevaucher le graphique.
"""

fig, ax = plt.subplots()

ax.plot(x, x**2, label="x²")
ax.plot(x, x**3, label="x³")

# Laisser matplotlib choisir la meilleure position
ax.legend(loc=0)

ax.set_title("Exemple de légende (placement automatique)")
plt.show()


# -----------------------------------------------------------
# Positions possibles de la légende
# -----------------------------------------------------------

positions = {
    1: "coin supérieur droit",
    2: "coin supérieur gauche",
    3: "coin inférieur gauche",
    4: "coin inférieur droit",
}

for loc, description in positions.items():
    fig, ax = plt.subplots()
    ax.plot(x, x**2, label="x²")
    ax.plot(x, x**3, label="x³")
    ax.legend(loc=loc)
    ax.set_title(f"Légende : {description}")
    plt.show()


# ===========================================================
# COULEURS ET STYLES DE LIGNES
# ===========================================================

"""
Matplotlib propose deux syntaxes :
- syntaxe type MATLAB (à éviter si possible)
- arguments par mots-clés (recommandé)
"""

# -----------------------------------------------------------
# Syntaxe type MATLAB (non recommandée)
# -----------------------------------------------------------

fig, ax = plt.subplots()
ax.plot(x, x**2, 'b.-', label="bleu + points")
ax.plot(x, x**3, 'g--', label="vert + tirets")
ax.legend()
ax.set_title("Syntaxe type MATLAB")
plt.show()


# -----------------------------------------------------------
# Approche recommandée : mots-clés
# -----------------------------------------------------------

fig, ax = plt.subplots()

ax.plot(x, x+1, color="blue", alpha=0.5, label="Bleu transparent")
ax.plot(x, x+2, color="#8B008B", label="Violet (hex)")
ax.plot(x, x+3, color="#FF8C00", label="Orange (hex)")

ax.legend()
ax.set_title("Couleurs avec mots-clés")
plt.show()


# ===========================================================
# LARGEUR DES LIGNES
# ===========================================================

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(x, x-1, lw=0.25, label="lw = 0.25")
ax.plot(x, x-2, lw=0.5, label="lw = 0.5")
ax.plot(x, x-3, lw=1, label="lw = 1")
ax.plot(x, x-4, lw=5, label="lw = 5")

ax.legend()
ax.set_title("Largeur des lignes")
plt.show()


# ===========================================================
# STYLES DE LIGNES
# ===========================================================

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(x, x-1, ls='-', lw=3, label="trait plein")
ax.plot(x, x-2, ls='-.', lw=3, label="tiret-point")
ax.plot(x, x-3, ls=':', lw=3, label="points")
ax.plot(x, x-4, ls='--', lw=3, label="tirets")

ax.legend()
ax.set_title("Styles de lignes")
plt.show()


# ===========================================================
# TIRETS PERSONNALISÉS
# ===========================================================

fig, ax = plt.subplots(figsize=(10, 5))

line = ax.plot(x, x, lw=4)[0]
line.set_dashes([10, 5])  # 10 points pleins, 5 points vides

ax.set_title("Tirets personnalisés")
plt.show()


fig, ax = plt.subplots(figsize=(10, 5))

line = ax.plot(x, x, lw=4)[0]
line.set_dashes([2, 2, 10, 2])

ax.set_title("Motif de tirets complexe")
plt.show()


# ===========================================================
# MARQUEURS
# ===========================================================

"""
Les marqueurs représentent les points de données.
Documentation :
https://matplotlib.org/stable/api/markers_api.html
"""

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(x, x-1, marker='+', ms=15, label="+")
ax.plot(x, x-2, marker='o', ms=15, label="o")
ax.plot(x, x-3, marker='s', ms=15, lw=0, label="s (sans ligne)")
ax.plot(x, x-4, marker='1', ms=15, label="1")

ax.legend()
ax.set_title("Types de marqueurs")
plt.show()


# ===========================================================
# MARQUEURS : STYLE AVANCÉ
# ===========================================================

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(
    x, x,
    marker='s',
    ms=15,
    lw=1,
    color="black",
    markerfacecolor="red",
    markeredgecolor="blue",
    markeredgewidth=4,
    label="Marqueur stylisé"
)

ax.legend()
ax.set_title("Personnalisation avancée des marqueurs")
plt.show()
