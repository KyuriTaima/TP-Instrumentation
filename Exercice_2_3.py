import scipy as sci
import numpy as np
import matplotlib.pyplot as plt
import statistics as st
from matplotlib.pyplot import grid

im = plt.imread('saturne.png')
r = im[:,:,0]
g = im[:,:,1]
b = im[:,:,2]

mesures1 = np.loadtxt('rameau1.txt')
mesures2 = np.loadtxt('rameau2.txt')

temps1 = mesures1[:,0] * 1e-3
tension1 = mesures1[:,1]
temps2 = mesures2[:,0] * 1e-3
tension2 = mesures2[:,1]

def Autocor(x):
    # Autocorrelation normalisee de x
    xc = x.copy() ; xc -= xc.mean()
    a = np.correlate(xc,xc,mode="full")[xc.size-1:]/np.arange(xc.size,0,-1)
    a /= xc.std()**2
    return a
a1 = Autocor(tension1)
a2 = Autocor(tension2)

plt.plot(temps1,a1,label="Mode 1")
plt.plot(temps2,a2,label="Mode 2")
plt.title("Fonctions d'autocorrélations des modes 1 et 2")
plt.xlabel("Temps (s)")
plt.ylabel("Facteur d'autocorrélaton normalisé")
plt.legend()
plt.grid(True)
plt.savefig('Autocorrel12.png', bbox_inches='tight')
plt.show()

tempsAutocorrel1_50 = [a1<0.5][0]
tempsAutocorrel2_50 = [a1<0.5][0]
tempsAutocorrel1_25 = [a1<0.25][0]
tempsAutocorrel2_25 = [a1<0.25][0]
tempsAutocorrel1_10 = [a1<0.1][0]
tempsAutocorrel2_10 = [a1<0.1][0]

for i = 

print(f"temps pour atteinre 50% d'autocorrélation pour Rameau 1:  {tempsAutocorrel1_50}")






