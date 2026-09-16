import scipy as sci
import numpy as np
import matplotlib.pyplot as plt
import statistics as st
from matplotlib.pyplot import grid

mesures1 = np.loadtxt('rameau1.txt')
mesures2 = np.loadtxt('rameau2.txt')

temps1 = mesures1[:,0] * 1e-3
tension1 = mesures1[:,1]
temps2 = mesures2[:,0] * 1e-3
tension2 = mesures2[:,1]

moyenne1 = np.sum(tension1)/len(tension1)
moyenne2 = np.sum(tension2)/len(tension2)

s = np.sqrt(np.sum((tension1 - moyenne1)**2)/len(tension1))
s2 = np.sqrt(np.sum((tension2 - moyenne2)**2)/len(tension2))

mediane1 = np.median(tension1)
mediane2 = np.median(tension2)
print(f"Médiane de la distribution des tensions sur Rameau 1 : {mediane1:.2f}")
print(f"Médiane de la distribution des tensions sur Rameau 2 : {mediane2:.2f}")

moyenne1 = np.sum(tension1)/len(tension1)
moyenne2 = np.sum(tension2)/len(tension2)

diff_moyenne_median1 = abs(moyenne1 - mediane1)
diff_moyenne_median2 = abs(moyenne2 - mediane2)
print(f"Différence entre la moyenne et la médiane sur Rameau 1 : {diff_moyenne_median1:.2f}")
print(f"Différence entre la moyenne et la médiane sur Rameau 2 : {diff_moyenne_median2:.2f}")

Q1_1 = sci.stats.scoreatpercentile(tension1, 25)
Q_3_1 = sci.stats.scoreatpercentile(tension1, 75)
Q1_2 = sci.stats.scoreatpercentile(tension2, 25)
Q_3_2 = sci.stats.scoreatpercentile(tension2, 75)

print(f"Premier quartile (Q1) de la distribution des tensions sur Rameau 1 : {Q1_1:.2f}")
print(f"Troisième quartile (Q3) de la distribution des tensions sur Rameau 1 : {Q_3_1:.2f}")
print(f"Premier quartile (Q1) de la distribution des tensions sur Rameau 2 : {Q1_2:.2f}")
print(f"Troisième quartile (Q3) de la distribution des tensions sur Rameau 2 : {Q_3_2:.2f}")

gauss = lambda x,m,s: np.exp(-((x-m)**2)/(2*s**2))/(s*np.sqrt(2*np.pi))
x = np.linspace(tension1.min(), tension1.max(), 100)
y = gauss(x, moyenne1, s)
hist1 = plt.hist(tension1, bins=25, density=True, cumulative=True, color='blue')
plt.plot(x, y, color='red', label='Densité de probabilité cumulée gaussienne')
plt.xlabel('Tension (V)')
plt.ylabel('Densité de probabilité')
plt.title('Distribution des tensions sur Rameau 1')
plt.legend()
plt.grid(True)
plt.savefig('FitGaussienCumulatifR1.png', bbox_inches='tight')
plt.show()
plt.close()

x2 = np.linspace(tension2.min(), tension2.max(), 100)
y2 = gauss(x2, moyenne2, s2)
gauss = lambda x2,m2,s2: np.exp(-((x2-m2)**2)/(2*s2**2))/(s2*np.sqrt(2*np.pi))
hist2 = plt.hist(tension2, bins=25, density=True, cumulative=True, color='orange')
plt.plot(x2, y2, color='red', label='Densité de probabilité cumulée gaussienne')
plt.xlabel('Tension (V)')
plt.ylabel('Densité de probabilité')
plt.title('Distribution des tensions sur Rameau 2')
plt.legend()
plt.grid(True)
plt.savefig('FitGaussienCumulatifR2.png', bbox_inches='tight')
plt.show()