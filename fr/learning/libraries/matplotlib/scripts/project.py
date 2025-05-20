import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from mpl_toolkits.mplot3d.axes3d import Axes3D
import numpy as np
from matplotlib import ticker
import matplotlib

# ----------------------------
# Tracé de l'équation d'Einstein E = mc²
# ----------------------------

# Données
c = 3 * 10**8 # Vitesse de la lumière
m = np.arange(0, 11)
e = m*c**2

# Shema
fig, axe = plt.subplots()
axe.plot(m, e, color="#FF8C00", lw=2)
axe.set_xlabel('Masse (g)')
axe.set_ylabel('Energie (Joules)')
axe.set_title('E = mc²')

# ÉCHELLE LOG
plt.yscale("log")
plt.grid(which='both',axis='y')

plt.show()

# ----------------------------
# Création de tracés à partir de points de données
# ----------------------------

# Données

"""
Les données montrent les intérêts payés pour une obligation du Trésor américain pour une certaine durée de contrat. La liste des étiquettes affiche la longueur de contrat correspondante par position d'index.
https://home.treasury.gov/policy-issues/financing-the-government/interest-rate-statistics?data=yield
"""
labels = ['1 Mo','3 Mo','6 Mo','1 Yr','2 Yr','3 Yr','5 Yr','7 Yr','10 Yr','20 Yr','30 Yr']
july16_2007 =[4.75,4.98,5.08,5.01,4.89,4.89,4.95,4.99,5.05,5.21,5.14]
july16_2020 = [0.12,0.11,0.13,0.14,0.16,0.17,0.28,0.46,0.62,1.09,1.31]

# Shema 1
fig, axe = plt.subplots()
axe.plot(labels, july16_2007, color="#FF8C00", lw=2, label="july16_2007")
axe.plot(labels, july16_2020, color="#8B008B", lw=2, label="july16_2020")
axe.legend(loc=(1.04,0.5))
plt.show()

# Shema 2
fig, axes = plt.subplots(2, 1)

axes[0].plot(labels, july16_2007, color="#FF8C00", lw=2, label="july16_2007")
axes[0].set_title('16 juillet 2007')

axes[1].plot(labels, july16_2020, color="#8B008B", lw=2, label="july16_2020")
axes[1].set_title('16 juillet 2020')

plt.show()

# Shema bonus

fig, ax1 = plt.subplots(figsize=(12,8))

ax1.plot(labels,july16_2007, lw=2, color="blue")
ax1.set_ylabel("2007", fontsize=18, color="blue")

ax1.spines['left'].set_color('blue')
ax1.spines['left'].set_linewidth(4)

for label in ax1.get_yticklabels():
    label.set_color("blue")
plt.yticks(fontsize=15)    
    
ax2 = ax1.twinx()
ax2.plot(labels,july16_2020, lw=2, color="red")
ax2.set_ylabel("2020", fontsize=18, color="red")

ax2.spines['right'].set_color('red')
ax2.spines['right'].set_linewidth(4)

for label in ax2.get_yticklabels():
    label.set_color("red")
    
ax1.set_title("Courbes de rendement du 16 juillet")
plt.yticks(fontsize=15)

plt.show()