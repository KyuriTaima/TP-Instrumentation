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

# Statistiques des mesures
print("Mode de la tension sur Rameau 1 :", st.mode(tension1))
print("Maximum de la tension sur Rameau 1 :", np.max(tension1))
print("Médiane de la tension sur Rameau 1 :", st.median(tension1))
print("Moyenne de la tension sur Rameau 1 :", np.mean(tension1))
print("Nombre de valeurs uniques sur Rameau 1 :", len(np.unique(tension1)))
print(f"Écart-type de la tension sur Rameau 1 : {np.std(tension1):.2f}")
print(f"Variance de la tension sur Rameau 1 : {np.var(tension1):.2f}")

print("Mode de la tension sur Rameau 2 :", st.mode(tension2))
print("Maximum de la tension sur Rameau 2 :", np.max(tension2))
print("Médiane de la tension sur Rameau 2 :", st.median(tension2))
print("Moyenne de la tension sur Rameau 2 :", np.mean(tension2))
print("Nombre de valeurs uniques sur Rameau 2 :", len(np.unique(tension2)))
print(f"Écart-type de la tension sur Rameau 2 : {np.std(tension2):.2f}")
print(f"Variance de la tension sur Rameau 2 : {np.var(tension2):.2f}")

moyenne1 = np.sum(tension1)/len(tension1)
moyenne2 = np.sum(tension2)/len(tension2)
print(f"Moyenne calculée de la tension sur Rameau 1 : {moyenne1:.2f}")
print(f"Moyenne calculée de la tension sur Rameau 2 : {moyenne2:.2f}")

s = np.sqrt(np.sum((tension1 - moyenne1)**2)/len(tension1))
print(f"Écart-type calculé de la tension sur Rameau 1 : {s:.2f}")

s2 = np.sqrt(np.sum((tension2 - moyenne2)**2)/len(tension2))
print(f"Écart-type calculé de la tension sur Rameau 2 : {s2:.2f}")