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

Q16_1 = sci.stats.scoreatpercentile(tension1, 16)
Q84_1 = sci.stats.scoreatpercentile(tension1, 84)
Q16_2 = sci.stats.scoreatpercentile(tension2, 16)
Q84_2 = sci.stats.scoreatpercentile(tension2, 84)
err_inf_1 = mediane1 - Q16_1
err_sup_1 = Q84_1 - mediane1
err_inf_2 = mediane2 - Q16_2
err_sup_2 = Q84_2 - mediane2
err_inf_1_90 = mediane1 - sci.stats.scoreatpercentile(tension1, 5)
err_sup_1_90 = sci.stats.scoreatpercentile(tension1, 95) - mediane1
err_inf_2_90 = mediane2 - sci.stats.scoreatpercentile(tension2, 5)
err_sup_2_90 = sci.stats.scoreatpercentile(tension2, 95) - mediane2
err_inf_1_95 = mediane1 - sci.stats.scoreatpercentile(tension1, 2.5)
err_sup_1_95 = sci.stats.scoreatpercentile(tension1, 97.5) - mediane1
err_inf_2_95 = mediane2 - sci.stats.scoreatpercentile(tension2, 2.5)
err_sup_2_95 = sci.stats.scoreatpercentile(tension2, 97.5) - mediane2
err_sup_1_99 = sci.stats.scoreatpercentile(tension1, 99.5) - mediane1
err_inf_1_99 = mediane1 - sci.stats.scoreatpercentile(tension1, 0.5)
err_sup_2_99 = sci.stats.scoreatpercentile(tension2, 99.5) - mediane2
err_inf_2_99 = mediane2 - sci.stats.scoreatpercentile(tension2, 0.5)

plt.plot(tension1, tension2, '.')
plt.axis('equal')
plt.xlabel('Tension rameau 1 (V)')
plt.ylabel('Tension rameau 2 (V)')
plt.grid(True)
plt.title('Corrélation entre les tensions des deux modes Rameaux')
plt.savefig('correlation_rameaux.png', dpi=300)
plt.show()

cov = lambda x,y: np.sum((x - np.mean(x)) * (y - np.mean(y))) / len(x)
corcoef = lambda x,y: cov(x,y) / (np.std(x) * np.std(y))
print(f"Coefficient de corrélation entre les tensions des deux modes Rameaux : {corcoef(tension1, tension2):.2f}")