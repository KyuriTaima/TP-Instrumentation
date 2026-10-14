# Exercice 4.1
import scipy as sci
import numpy as np
import matplotlib.pyplot as plt
import statistics as st
from matplotlib.pyplot import grid
from scipy.special import gamma
from numpy.fft import fft, ifft

mesures_golf = np.loadtxt('golf.txt')
vitesses = mesures_golf[:,1]
temps = mesures_golf[:,0]
temps_heures = temps / 3600
duree_obs = temps_heures[-1] - temps_heures[0]
T_e = temps[1] - temps[0]

print("Duréee d'observation :", duree_obs, "heures")

print("Formes des mesures de la vitesse radiale du soleil par GOLF:", mesures_golf.shape)

plt.plot(temps_heures, vitesses, label="Mesures de vitesses radiales du soleil par GOLF")
plt.xlabel("Temps (heures)")
plt.ylabel("Vitesse radiale (m/s)")
plt.title("Vitesse radiale du soleil par GOLF")
plt.legend()
plt.grid(True)
plt.savefig('VitesseRadialeGOLF.png', bbox_inches='tight')
plt.show()

vitesses_centree = vitesses - np.mean(vitesses)
fft_vitesses = fft(vitesses_centree)
print(f"Résultat FFT : {fft_vitesses.shape[0]} points")

frequence_echantillonage = 1 / T_e
pas_frequence = frequence_echantillonage / fft_vitesses.shape[0]

print("Fréquence d'échantillonnage :", frequence_echantillonage, "Hz")
print("Pas de fréquence :", pas_frequence, "Hz")

plt.plot(np.abs(fft_vitesses), "r,")
plt.xlabel("Fréquence (Hz)")
plt.ylabel("Amplitude")
plt.title("Transformée de Fourier des vitesses radiales du soleil par GOLF")
plt.grid(True)
plt.savefig('FFT_VitesseRadialeGOLF.png', bbox_inches='tight')
plt.show()

plt.stem(np.abs(fft_vitesses))
plt.xlabel("Fréquence (Hz)")
plt.ylabel("Amplitude")
plt.title("Transformée de Fourier des vitesses radiales du soleil par GOLF")
plt.grid(True)
plt.savefig('FFT_VitesseRadialeGOLF_stem.png', bbox_inches='tight')
plt.show()

# Représentation de la densité spectrale en énéergie (DSE) de la vitesse radiale en graduant l'axe des abscisses en mHz
dse = (np.abs(fft_vitesses)**2)
abs_frequences = np.arange(0, fft_vitesses.shape[0]) * pas_frequence
plt.plot(abs_frequences * 1000, dse, "r.-")
plt.xlabel("Fréquence (mHz)")
plt.ylabel("Densité spectrale en énergie (m/s)^2/Hz")
plt.title("Densité spectrale en énergie des vitesses radiales du soleil par GOLF")
plt.grid(True)
plt.savefig('DSE_VitesseRadialeGOLF.png', bbox_inches='tight')
plt.show()

plt.plot(abs_frequences * 1000, dse, "r.-")
plt.xlabel("Fréquence (mHz)")
plt.ylabel("Densité spectrale en énergie (m/s)^2/Hz")
plt.title("Densité spectrale en énergie des vitesses radiales du soleil par GOLF - Zoom sur les modes P du Soleil")
plt.grid(True)
plt.xlim(2, 5)
plt.savefig('DSE_VitesseRadialeGOLF_zoom.png', bbox_inches='tight')
plt.show()

# Calcul de la DSE en utilisant uniquement les 1000 premières mesures
fft_vitesses_1000 = fft(vitesses_centree[:1000])
dse_1000 = (np.abs(fft_vitesses_1000)**2)
abs_frequences_1000 = np.arange(0, fft_vitesses_1000.shape[0]) * pas_frequence
#plt.plot(abs_frequences_1000 * 1000, dse_1000, "r.-")
plt.stem(np.abs(fft_vitesses_1000))
plt.xlabel("Fréquence (mHz)")
plt.ylabel("Densité spectrale en énergie (m/s)^2/Hz")
plt.title("Densité spectrale en énergie des vitesses radiales du soleil par GOLF - Zoom sur les 1000 premières mesures")
plt.grid(True)
plt.savefig('DSE_VitesseRadialeGOLF_1000.png', bbox_inches='tight')
plt.show()