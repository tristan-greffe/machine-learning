import matplotlib.pyplot as plt
import numpy as np

# ===========================================================
# Données
# ===========================================================

# Données non linéaires
a = np.linspace(0, 10, 11)
b = a ** 4

# Données linéaires
x = np.arange(0, 10)
y = 2 * x


# ===========================================================
# Figure simple avec un seul axe
# ===========================================================

# plt.subplots() retourne directement la Figure et l'objet Axes
fig, ax = plt.subplots()

ax.plot(x, y, color='red')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Relation linéaire')

plt.show()


# ===========================================================
# Création de plusieurs axes (subplots)
# ===========================================================

# 1 ligne, 2 colonnes
fig, axes = plt.subplots(nrows=1, ncols=2)

# axes est un tableau NumPy d'objets Axes
axes[0].plot(a, b)
axes[0].set_title('a⁴')

axes[1].plot(x, y)
axes[1].set_title('2x')

plt.show()


# ===========================================================
# Subplots en grille 2x2
# ===========================================================

fig, axes = plt.subplots(nrows=2, ncols=2)

axes[0, 0].plot(a, b)
axes[0, 0].set_title('a⁴')

axes[0, 1].plot(y, x)
axes[0, 1].set_title('y vs x')

axes[1, 0].plot(b, a)
axes[1, 0].set_title('b vs a')

axes[1, 1].plot(x, y)
axes[1, 1].set_title('2x')

plt.tight_layout()
plt.show()


# ===========================================================
# Paramètres globaux de Figure
# ===========================================================

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

axes[0, 0].plot(a, b)
axes[0, 0].set_title('0,0')

axes[0, 1].plot(y, x)
axes[0, 1].set_title('0,1')

axes[1, 0].plot(b, a)
axes[1, 0].set_title('1,0')

axes[1, 1].plot(x, y)
axes[1, 1].set_title('1,1')
axes[1, 1].set_xlabel('X')
axes[1, 1].set_ylabel('Y')

# Paramètre global de la Figure
fig.suptitle('Niveau Figure', fontsize=16)

plt.tight_layout()
plt.show()


# ===========================================================
# Espacement manuel des subplots
# ===========================================================

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

axes[0, 0].plot(a, b)
axes[0, 1].plot(y, x)
axes[1, 0].plot(b, a)
axes[1, 1].plot(x, y)

fig.subplots_adjust(
    left=0.05,
    right=0.95,
    bottom=0.05,
    top=0.9,
    wspace=0.6,
    hspace=0.3
)

plt.show()


# ===========================================================
# Exportation de la Figure
# ===========================================================

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

axes[0, 0].plot(a, b)
axes[0, 1].plot(y, x)
axes[1, 0].plot(b, a)
axes[1, 1].plot(x, y)

fig.savefig('subplots.png', bbox_inches='tight')
plt.show()
