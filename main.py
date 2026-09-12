from turtledemo.chaos import plot

import scipy as sci
import numpy as np
import matplotlib.pyplot as plt
import statistics as st
from matplotlib.pyplot import grid

mesures1 = np.loadtxt('rameau1.txt')
mesures2 = np.loadtxt('rameau2.txt')
print(mesures1.shape)

temps1 = mesures1[:,0]
tension1 = mesures1[:,1]
temps2 = mesures2[:,0]
tension2 = mesures2[:,1]
plt.plot(temps1*(1/60),tension1, "orange")
plt.plot(temps2*(1/60),tension2, "red")
plt.grid(True)
plt.xlabel('Temps (min)')
plt.ylabel('Tension (V)')
plt.title('Tension en fonction du temps sur Rameau 1 & 2')
plt.show()

plt.close()
tri1 = np.sort(tension1)
tri2 = np.sort(tension2)
plt.xlabel('Numéro de la mesure')
plt.ylabel('Tension (V)')
plt.grid(True)
plt.plot(tri1, '.')
plt.plot(tri2, '.')
plt.title('Tension triée sur Rameau 1 & 2')
plt.show()

plt.close()
hist1 = plt.hist(tension1, bins=50, density=True)
hist2 = plt.hist(tension2, bins=50, density=True, alpha=0.5)
plt.grid(True)
plt.xlabel('Tension (V)')
plt.ylabel('Fréquence')
plt.title('Histogramme de la tension sur Rameau 1 & 2')
plt.show()

print(st.mode(tension1))
print(np.max(tension1))
print(st.median(tension1))
print(np.mean(tension1))
print(len(np.unique(tension1)))
print(np.std(tension1))

plt.subplot(2,2,1)