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

# Densité de probabilité
hist1 = plt.hist(tension1, bins=25, density=True)
plt.grid(True)
plt.xlabel('Tension (V)')
plt.ylabel('Densité de probabilité')
plt.title('Histogramme des densité de probabilité d\'obtenir une valeur de tension sur Rameau 1')
plt.savefig('DensiteR1.png', bbox_inches='tight')
plt.show()