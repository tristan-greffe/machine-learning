import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from mpl_toolkits.mplot3d.axes3d import Axes3D
import numpy as np
from matplotlib import ticker
import matplotlib

"""
# Commandes Avancées Matplotlib

Ce script est une référence complète pour les commandes avancées de Matplotlib. 
Chaque section illustre un concept différent, avec des exemples visuels.
"""

# ----------------------------
# Données de base
# ----------------------------
x = np.linspace(0, 5, 50)  # données pour les tracés de base

# ----------------------------
# Échelle logarithmique
# ----------------------------
fig, axes = plt.subplots(1, 2, figsize=(10,4))
axes[0].plot(x, x**2, x, np.exp(x))
axes[0].set_title("Normal scale")

axes[1].plot(x, x**2, x, np.exp(x))
axes[1].set_yscale("log")
axes[1].set_title("Logarithmic scale (y)")

plt.show()

# ----------------------------
# Placement de ticks et étiquettes personnalisées
# ----------------------------
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(x, x**2, x, x**3, lw=2)

ax.set_xticks([1, 2, 3, 4, 5])
ax.set_xticklabels([r'$\alpha$', r'$\beta$', r'$\gamma$', r'$\delta$', r'$\epsilon$'], fontsize=18)

yticks = [0, 50, 100, 150]
ax.set_yticks(yticks)
ax.set_yticklabels(["$%.1f$" % y for y in yticks], fontsize=18)

plt.show()

# ----------------------------
# Notation scientifique
# ----------------------------
fig, ax = plt.subplots()
ax.plot(x, x**2, x, np.exp(x))
ax.set_title("Scientific notation")
ax.set_yticks([0, 50, 100, 150])

formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
formatter.set_powerlimits((-1,1))
ax.yaxis.set_major_formatter(formatter)

plt.show()

# ----------------------------
# Espacement entre axes et labels
# ----------------------------
matplotlib.rcParams['xtick.major.pad'] = 5
matplotlib.rcParams['ytick.major.pad'] = 5

fig, ax = plt.subplots()
ax.plot(x, x**2, x, np.exp(x))
ax.set_yticks([0, 50, 100, 150])
ax.set_title("Label and axis spacing")
ax.xaxis.labelpad = 5
ax.yaxis.labelpad = 5
ax.set_xlabel("x")
ax.set_ylabel("y")

plt.show()

# Restaurer valeurs par défaut
matplotlib.rcParams['xtick.major.pad'] = 3
matplotlib.rcParams['ytick.major.pad'] = 3

# ----------------------------
# Réglages de position des axes
# ----------------------------
fig, ax = plt.subplots()
ax.plot(x, x**2, x, np.exp(x))
ax.set_yticks([0, 50, 100, 150])
ax.set_title("Title")
ax.set_xlabel("x")
ax.set_ylabel("y")
fig.subplots_adjust(left=0.15, right=.9, bottom=0.1, top=0.9)

plt.show()

# ----------------------------
# Grille d'axe
# ----------------------------
fig, axes = plt.subplots(1, 2, figsize=(10,3))
axes[0].plot(x, x**2, x, x**3, lw=2)
axes[0].grid(True)

axes[1].plot(x, x**2, x, x**3, lw=2)
axes[1].grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)

plt.show()

# ----------------------------
# Axis spines
# ----------------------------
fig, ax = plt.subplots(figsize=(6,2))
ax.spines['bottom'].set_color('blue')
ax.spines['top'].set_color('blue')
ax.spines['left'].set_color('red')
ax.spines['left'].set_linewidth(2)
ax.spines['right'].set_color("none")
ax.yaxis.tick_left()

plt.show()

# ----------------------------
# Axes jumeaux
# ----------------------------
fig, ax1 = plt.subplots()
ax1.plot(x, x**2, lw=2, color="blue")
ax1.set_ylabel(r"area $(m^2)$", fontsize=18, color="blue")
for label in ax1.get_yticklabels():
    label.set_color("blue")

ax2 = ax1.twinx()
ax2.plot(x, x**3, lw=2, color="red")
ax2.set_ylabel(r"volume $(m^3)$", fontsize=18, color="red")
for label in ax2.get_yticklabels():
    label.set_color("red")

plt.show()

# ----------------------------
# Axes x et y à zéro
# ----------------------------
fig, ax = plt.subplots()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

xx = np.linspace(-0.75, 1., 100)
ax.plot(xx, xx**3)

plt.show()

# ----------------------------
# Autres styles de tracés 2D
# ----------------------------
n = np.array([0,1,2,3,4,5])
fig, axes = plt.subplots(1, 4, figsize=(12,3))
axes[0].scatter(xx, xx + 0.25*np.random.randn(len(xx))); axes[0].set_title("scatter")
axes[1].step(n, n**2, lw=2); axes[1].set_title("step")
axes[2].bar(n, n**2, align="center", width=0.5, alpha=0.5); axes[2].set_title("bar")
axes[3].fill_between(x, x**2, x**3, color="green", alpha=0.5); axes[3].set_title("fill_between")

plt.show()

# ----------------------------
# Annotation de texte
# ----------------------------
fig, ax = plt.subplots()
ax.plot(xx, xx**2, xx, xx**3)
ax.text(0.15, 0.2, r"$y=x^2$", fontsize=20, color="blue")
ax.text(0.65, 0.1, r"$y=x^3$", fontsize=20, color="green")

plt.show()

# ----------------------------
# Figures avec plusieurs sous-graphiques et encarts
# ----------------------------
# subplots
fig, ax = plt.subplots(2, 3)
fig.tight_layout()
plt.show()

# subplot2grid
fig = plt.figure()
ax1 = plt.subplot2grid((3,3), (0,0), colspan=3)
ax2 = plt.subplot2grid((3,3), (1,0), colspan=2)
ax3 = plt.subplot2grid((3,3), (1,2), rowspan=2)
ax4 = plt.subplot2grid((3,3), (2,0))
ax5 = plt.subplot2grid((3,3), (2,1))
fig.tight_layout()
plt.show()

# gridspec
fig = plt.figure()
gs = gridspec.GridSpec(2, 3, height_ratios=[2,1], width_ratios=[1,2,1])
for g in gs:
    ax = fig.add_subplot(g)
fig.tight_layout()
plt.show()

# add_axes et inset
fig, ax = plt.subplots()
ax.plot(xx, xx**2, xx, xx**3)
fig.tight_layout()

inset_ax = fig.add_axes([0.2, 0.55, 0.35, 0.35])
inset_ax.plot(xx, xx**2, xx, xx**3)
inset_ax.set_title('zoom near origin')
inset_ax.set_xlim(-.2, .2)
inset_ax.set_ylim(-.005, .01)
inset_ax.set_yticks([0, 0.005, 0.01])
inset_ax.set_xticks([-0.1,0,.1])

plt.show()

# ----------------------------
# Cartes de couleurs et figures de contour
# ----------------------------
alpha = 0.7
phi_ext = 2 * np.pi * 0.5

def flux_qubit_potential(phi_m, phi_p):
    return 2 + alpha - 2 * np.cos(phi_p) * np.cos(phi_m) - alpha * np.cos(phi_ext - 2*phi_p)

phi_m = np.linspace(0, 2*np.pi, 100)
phi_p = np.linspace(0, 2*np.pi, 100)
X,Y = np.meshgrid(phi_p, phi_m)
Z = flux_qubit_potential(X, Y).T

# pcolor
fig, ax = plt.subplots()
p = ax.pcolor(X/(2*np.pi), Y/(2*np.pi), Z, cmap=matplotlib.cm.RdBu,
              vmin=abs(Z).min(), vmax=abs(Z).max())
cb = fig.colorbar(p, ax=ax)
plt.show()

# imshow
fig, ax = plt.subplots()
im = ax.imshow(Z, cmap=matplotlib.cm.RdBu,
               vmin=abs(Z).min(), vmax=abs(Z).max(), extent=[0, 1, 0, 1])
im.set_interpolation('bilinear')
cb = fig.colorbar(im, ax=ax)
plt.show()

# contour
fig, ax = plt.subplots()
cnt = ax.contour(Z, cmap=matplotlib.cm.RdBu,
                 vmin=abs(Z).min(), vmax=abs(Z).max(), extent=[0, 1, 0, 1])
plt.show()

# ----------------------------
# Figures 3D
# ----------------------------
# Surface plot
fig = plt.figure(figsize=(14,6))
ax = fig.add_subplot(1, 2, 1, projection='3d')
p = ax.plot_surface(X, Y, Z, rstride=4, cstride=4, linewidth=0)

ax = fig.add_subplot(1, 2, 2, projection='3d')
p = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=matplotlib.cm.coolwarm,
                    linewidth=0, antialiased=False)
cb = fig.colorbar(p, shrink=0.5)
plt.show()

# Wireframe
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(1, 1, 1, projection='3d')
p = ax.plot_wireframe(X, Y, Z, rstride=4, cstride=4)
plt.show()

# Surface avec projections de contours
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(1,1,1, projection='3d')
ax.plot_surface(X, Y, Z, rstride=4, cstride=4, alpha=0.25)
ax.contour(X, Y, Z, zdir='z', offset=-np.pi, cmap=matplotlib.cm.coolwarm)
ax.contour(X, Y, Z, zdir='x', offset=-np.pi, cmap=matplotlib.cm.coolwarm)
ax.contour(X, Y, Z, zdir='y', offset=3*np.pi, cmap=matplotlib.cm.coolwarm)
ax.set_xlim3d(-np.pi, 2*np.pi)
ax.set_ylim3d(0, 3*np.pi)
ax.set_zlim3d(-np.pi, 2*np.pi)
plt.show()
