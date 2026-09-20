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
tempsAutocorrel2_50 = [a2<0.5][0]
tempsAutocorrel1_25 = [a1<0.25][0]
tempsAutocorrel2_25 = [a2<0.25][0]
tempsAutocorrel1_10 = [a1<0.1][0]
tempsAutocorrel2_10 = [a2<0.1][0]

# for i in range 1 to 3, find the time at which the autocorrelation drops below 50%, 25%, and 10% for both modes
for i in range(1,4):
    if i == 1:
        for j in range(len(tempsAutocorrel1_50)):
            if tempsAutocorrel1_50[j]:
                print(f"Mode 1: Autocorrelation drops below 50% at time {temps1[j]} s, after j = {j}")
                break
        for j in range(len(tempsAutocorrel2_50)):
            if tempsAutocorrel2_50[j]:
                print(f"Mode 2: Autocorrelation drops below 50% at time {temps2[j]} s, after j = {j}")
                break
    elif i == 2:
        for j in range(len(tempsAutocorrel1_25)):
            if tempsAutocorrel1_25[j]:
                print(f"Mode 1: Autocorrelation drops below 25% at time {temps1[j]} s, after j = {j}")
                break
        for j in range(len(tempsAutocorrel2_25)):
            if tempsAutocorrel2_25[j]:
                print(f"Mode 2: Autocorrelation drops below 25% at time {temps2[j]} s, after j = {j}")
                break
    elif i == 3:
        for j in range(len(tempsAutocorrel1_10)):
            if tempsAutocorrel1_10[j]:
                print(f"Mode 1: Autocorrelation drops below 10% at time {temps1[j]:.2f} s, after j = {j}")
                break
        for j in range(len(tempsAutocorrel2_10)):
            if tempsAutocorrel2_10[j]:
                print(f"Mode 2: Autocorrelation drops below 10% at time {temps2[j]:.2f} s, after j = {j}")
                break







