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

measuredValue = 3.14
S_B = measuredValue/s
print(f"Rapport signal sur bruit (S/B) pour Rameau 1 : {S_B:.2f}")

Q16_1 = sci.stats.scoreatpercentile(tension1, 16)
Q84_1 = sci.stats.scoreatpercentile(tension1, 84)
Q16_2 = sci.stats.scoreatpercentile(tension2, 16)
Q84_2 = sci.stats.scoreatpercentile(tension2, 84)
print(f"Intervalle de confiance à 68% pour Rameau 1 : [{Q16_1:.2f}, {Q84_1:.2f}]")
print(f"Intervalle de confiance à 68% pour Rameau 2 : [{Q16_2:.2f}, {Q84_2:.2f}]")
err_inf_1 = mediane1 - Q16_1
err_sup_1 = Q84_1 - mediane1
err_inf_2 = mediane2 - Q16_2
err_sup_2 = Q84_2 - mediane2
print(f"Erreur inférieure pour Rameau 1 : {err_inf_1:.2f}")
print(f"Erreur supérieure pour Rameau 1 : {err_sup_1:.2f}")
print(f"Erreur inférieure pour Rameau 2 : {err_inf_2:.2f}")
print(f"Erreur supérieure pour Rameau 2 : {err_sup_2:.2f}")
err_inf_1_90 = mediane1 - sci.stats.scoreatpercentile(tension1, 5)
err_sup_1_90 = sci.stats.scoreatpercentile(tension1, 95) - mediane1
err_inf_2_90 = mediane2 - sci.stats.scoreatpercentile(tension2, 5)
err_sup_2_90 = sci.stats.scoreatpercentile(tension2, 95) - mediane2
print(f"Erreur inférieure pour Rameau 1 à 90% : {err_inf_1_90:.2f}")
print(f"Erreur supérieure pour Rameau 1 à 90% : {err_sup_1_90:.2f}")
print(f"Erreur inférieure pour Rameau 2 à 90% : {err_inf_2_90:.2f}")
print(f"Erreur supérieure pour Rameau 2 à 90% : {err_sup_2_90:.2f}")

err_inf_1_95 = mediane1 - sci.stats.scoreatpercentile(tension1, 2.5)
err_sup_1_95 = sci.stats.scoreatpercentile(tension1, 97.5) - mediane1
err_inf_2_95 = mediane2 - sci.stats.scoreatpercentile(tension2, 2.5)
err_sup_2_95 = sci.stats.scoreatpercentile(tension2, 97.5) - mediane2
print(f"Erreur inférieure pour Rameau 1 à 95% : {err_inf_1_95:.2f}")
print(f"Erreur supérieure pour Rameau 1 à 95% : {err_sup_1_95:.2f}")
print(f"Erreur inférieure pour Rameau 2 à 95% : {err_inf_2_95:.2f}")
print(f"Erreur supérieure pour Rameau 2 à 95% : {err_sup_2_95:.2f}")

err_sup_1_99 = sci.stats.scoreatpercentile(tension1, 99.5) - mediane1
err_inf_1_99 = mediane1 - sci.stats.scoreatpercentile(tension1, 0.5)
err_sup_2_99 = sci.stats.scoreatpercentile(tension2, 99.5) - mediane2
err_inf_2_99 = mediane2 - sci.stats.scoreatpercentile(tension2, 0.5)
print(f"Erreur inférieure pour Rameau 1 à 99% : {err_inf_1_99:.2f}")
print(f"Erreur supérieure pour Rameau 1 à 99% : {err_sup_1_99:.2f}")
print(f"Erreur inférieure pour Rameau 2 à 99% : {err_inf_2_99:.2f}")
print(f"Erreur supérieure pour Rameau 2 à 99% : {err_sup_2_99:.2f}")