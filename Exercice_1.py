import scipy as sci
import numpy as np
import matplotlib.pyplot as plt
import statistics as st
from matplotlib.pyplot import grid

mesures1 = np.loadtxt('rameau1.txt')
mesures2 = np.loadtxt('rameau2.txt')
print("Forme des mesures 1 :", mesures1.shape)
print("Forme des mesures 2 :", mesures2.shape)

temps1 = mesures1[:,0] * 1e-3
tension1 = mesures1[:,1]
temps2 = mesures2[:,0] * 1e-3
tension2 = mesures2[:,1]

# Affichage pour Rameau 1 en secondes
plt.plot(temps1, tension1, "orange", label='Rameau 1')
plt.grid(True)
plt.xlabel('Temps (s)')
plt.ylabel('Tension (V)')
plt.title('Tension en fonction du temps sur Rameau 1')
plt.legend()
plt.savefig('TensionEnFonctionDuTempsSecondesR1.png', bbox_inches='tight')
plt.show()

# Affichage pour Rameau 1 en minutes
plt.plot(temps1*(1/60), tension1, "orange", label='Rameau 1')
plt.grid(True)
plt.xlabel('Temps (min)')
plt.ylabel('Tension (V)')
plt.title('Tension en fonction du temps sur Rameau 1')
plt.legend()
plt.savefig('TensionEnFonctionDuTempsMinutesR1.png', bbox_inches='tight')
plt.show()

# Affichage pour Rameau 2 en secondes
plt.plot(temps2, tension2, "red", label='Rameau 2')
plt.grid(True)
plt.xlabel('Temps (s)')
plt.ylabel('Tension (V)')
plt.title('Tension en fonction du temps sur Rameau 2')
plt.legend()
plt.savefig('TensionEnFonctionDuTempsSecondesR2.png', bbox_inches='tight')
plt.show()

# Affichage pour Rameau 2 en minutes
plt.plot(temps2*(1/60), tension2, "red", label='Rameau 2')
plt.grid(True)
plt.xlabel('Temps (min)')
plt.ylabel('Tension (V)')
plt.title('Tension en fonction du temps sur Rameau 2')
plt.legend()
plt.savefig('TensionEnFonctionDuTempsMinutesR2.png', bbox_inches='tight')
plt.show()

# Tri des mesures
tri1 = np.sort(tension1)
tri2 = np.sort(tension2)
plt.xlabel('Numéro de la mesure')
plt.ylabel('Tension (V)')
plt.grid(True)
plt.plot(tri1, '.', label='Rameau 1')
plt.plot(tri2, '.', label='Rameau 2')
plt.title('Tension triée sur Rameau 1 & 2')
plt.legend()
plt.savefig('TensionTrieeR1R2.png', bbox_inches='tight')
plt.show()

# Histogramme des mesures
hist1 = plt.hist(tension1, bins=25, density=False)
hist2 = plt.hist(tension2, bins=25, density=False, alpha=0.5)
plt.grid(True)
plt.xlabel('Tension (V)')
plt.ylabel('Fréquence')
plt.title('Histogramme des tensions sur Rameau 1 & 2')
plt.savefig('HistogrammeR1R2.png', bbox_inches='tight')
plt.show()

# Statistiques des mesures
print("Mode de la tension sur Rameau 1 :", st.mode(tension1))
print("Maximum de la tension sur Rameau 1 :", np.max(tension1))
print("Médiane de la tension sur Rameau 1 :", st.median(tension1))
print("Moyenne de la tension sur Rameau 1 :", np.mean(tension1))
print("Nombre de valeurs uniques sur Rameau 1 :", len(np.unique(tension1)))
print("Écart-type de la tension sur Rameau 1 :", np.std(tension1))

print("Mode de la tension sur Rameau 2 :", st.mode(tension2))
print("Maximum de la tension sur Rameau 2 :", np.max(tension2))
print("Médiane de la tension sur Rameau 2 :", st.median(tension2))
print("Moyenne de la tension sur Rameau 2 :", np.mean(tension2))
print("Nombre de valeurs uniques sur Rameau 2 :", len(np.unique(tension2)))
print("Écart-type de la tension sur Rameau 2 :", np.std(tension2))

# Densité de probabilité
hist1 = plt.hist(tension1, bins=25, density=True)
plt.grid(True)
plt.xlabel('Tension (V)')
plt.ylabel('Densité de probabilité')
plt.title('Histogramme des densité de probabilité d\'obtenir une valeur de tension sur Rameau 1')
plt.savefig('DensiteR1.png', bbox_inches='tight')
plt.show()