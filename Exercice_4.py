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

gauss = lambda x,m,s: np.exp(-((x-m)**2)/(2*s**2))/(s*np.sqrt(2*np.pi))
x = np.linspace(tension1.min(), tension1.max(), 100)
y = gauss(x, moyenne1, s)
hist1 = plt.hist(tension1, bins=25, density=True)

plt.plot(x, y, color='red', label='Fit gaussien')
plt.xlabel('Tension (V)')
plt.ylabel('Densité de probabilité')
plt.title('Distribution des tensions sur Rameau 1')
plt.legend()
plt.grid(True)
plt.savefig('FitGaussienR1.png', bbox_inches='tight')
plt.show()
plt.close()

x2 = np.linspace(tension2.min(), tension2.max(), 100)
y2 = gauss(x2, moyenne2, s2)
gauss = lambda x2,m2,s2: np.exp(-((x2-m2)**2)/(2*s2**2))/(s2*np.sqrt(2*np.pi))
hist2 = plt.hist(tension2, bins=25, density=True, color='orange')

plt.plot(x2, y2, color='red', label='Fit gaussien')
plt.xlabel('Tension (V)')
plt.ylabel('Densité de probabilité')
plt.title('Distribution des tensions sur Rameau 2')
plt.legend()
plt.grid(True)
plt.savefig('FitGaussienR2.png', bbox_inches='tight')
plt.show()

skew1 = sci.stats.skew(tension1)
skew2 = sci.stats.skew(tension2)
print(f"Skewness de la distribution des tensions sur Rameau 1 : {skew1:.2f}")
print(f"Skewness de la distribution des tensions sur Rameau 2 : {skew2:.2f}")

kurtosis1 = sci.stats.kurtosis(tension1)
kurtosis2 = sci.stats.kurtosis(tension2)
print(f"Kurtosis de la distribution des tensions sur Rameau 1 : {kurtosis1:.2f}")
print(f"Kurtosis de la distribution des tensions sur Rameau 2 : {kurtosis2:.2f}")