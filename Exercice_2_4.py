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

# On construit le signal v1 + v2, donc on somme les amplitudes, le pas de temps reste le même.
tension3 = tension1 + tension2
temps3 = temps1

# On compare l'espérance expérimentale de v1 + v2 avec l'espérance théorique de v1 + v2, qui est la somme des espérances de v1 et v2.
esperance1 = st.mean(tension1)
esperance2 = st.mean(tension2)
esperance3 = st.mean(tension3)

print(f"Espérance expérimentale de v1: {esperance1:.2f}")
print(f"Espérance expérimentale de v2: {esperance2:.2f}")
print(f"Espérance expérimentale de v1 + v2: {esperance3:.2f}")
print(f"Espérance théorique de v1 + v2: {esperance1 + esperance2:.2f}")

ecart_type1 = st.stdev(tension1)
ecart_type2 = st.stdev(tension2)
ecart_type3 = st.stdev(tension3)

print(f"Écart-type expérimental de v1: {ecart_type1:.2f}")
print(f"Écart-type expérimental de v2: {ecart_type2:.2f}")
print(f"Écart-type expérimental de v1 + v2: {ecart_type3:.2f}")
print(f"Somme des écarts-types v1 + v2: {ecart_type1 + ecart_type2:.2f}")

print(f"Variance expérimentale de v1: {ecart_type1**2:.2f}")
print(f"Variance expérimentale de v2: {ecart_type2**2:.2f}")
print(f"Variance expérimentale de v1 + v2: {ecart_type3**2:.2f}")
print(f"Variance théorique de v1 + v2: {ecart_type1**2 + ecart_type2**2:.2f}")

variance_théorique = ecart_type1**2 + ecart_type2**2 + 2 * np.cov(tension1, tension2)[0][1]
print(f"Variance théorique de v1 + v2 avec covariance: {variance_théorique:.2f}")

r_1d = np.reshape(r, 617*480)
g_1d = np.reshape(g, 617*480)
b_1d = np.reshape(b, 617*480)

r_b = r_1d + b_1d
esperance_r_b = st.mean(r_b)
ecart_type_r_b = st.stdev(r_b)
esperance_r = st.mean(r_1d)
ecart_type_r = st.stdev(r_1d)
esperance_b = st.mean(b_1d)
ecart_type_b = st.stdev(b_1d)
esperance_r_plus_b = esperance_r + esperance_b
ecart_type_r_plus_b_theorique = np.sqrt(ecart_type_r**2 + ecart_type_b**2 + 2 * np.cov(r_1d, b_1d)[0][1])

print("-----------------------------")
print(f"Espérance de r: {esperance_r:.2f}")
print(f"Espérance de b: {esperance_b:.2f}")
print(f"Écart-type de r: {ecart_type_r:.2f}")
print(f"Écart-type de b: {ecart_type_b:.2f}")
print(f"Variance de r: {ecart_type_r**2:.2f}")
print(f"Variance de b: {ecart_type_b**2:.2f}")
print(f"Espérance de r + b: {esperance_r_b:.2f}")
print(f"Espérance de r + espérance de b: {esperance_r + esperance_b:.2f}")
print(f"Écart-type de r + b: {ecart_type_r_b:.2f}")
print(f"Ecart-type de r + ecart-type de b: {ecart_type_r + ecart_type_b:.2f}")
print(f"Variance de r + b: {ecart_type_r_b**2:.2f}")
print(f"Variance de r + variance de b + covariance: {ecart_type_r_plus_b_theorique**2:.2f}")
print(f"Variance de r + variance de b: {ecart_type_r**2 + ecart_type_b**2:.2f}")