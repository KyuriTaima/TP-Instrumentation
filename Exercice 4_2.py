# Exercice 4.2
import scipy as sci
import numpy as np
import matplotlib.pyplot as plt
import statistics as st
from matplotlib.pyplot import grid
from scipy.special import gamma
from numpy.fft import fft, ifft
from numpy.fft import fft, fftfreq


mesures_obs = np.loadtxt('obs-vis2.txt')
print("Forme des mesures visibles :", mesures_obs.shape)

# Stocker les 500 premières mesures du visible dans un tableau
fond = mesures_obs[:500]
source = mesures_obs[500:700]

hist_fond = plt.hist(fond, bins=15)
hist_source = plt.hist(source, bins=15)
plt.grid(True)
plt.xlabel('Nombre de photo-électrons')
plt.ylabel('Nombre d\'occurrences de ces valeurs de photo-électrons')
plt.title('Histogramme des occurrences de valeurs de photo-électrons sur les mesures du visible')
plt.savefig('Histogramme_Photo_Electrons_Visible_2.png', bbox_inches='tight')
plt.legend(['Fond', 'Source'])
plt.show()

# Création d'une échelle allant de 0 à 500 pour le pas de pauses
pauses = np.arange(0, 500, 1)
plt.plot(pauses, fond, label='Fond')
plt.grid(True)
plt.xlabel('Indice de la pause')
plt.ylabel('Nombre de photo-électrons')
plt.title('Mesures de photo-électrons sur le fond')
plt.savefig('Mesures_Fond_2.png', bbox_inches='tight')
plt.legend()
plt.show()

#Création d'une échelle allant de 0 à 200 pour le pas de pauses
pauses_source = np.arange(0, 200, 1)
plt.plot(pauses_source, source, label='Source')
plt.grid(True)
plt.xlabel('Indice de la pause')
plt.ylabel('Nombre de photo-électrons')
plt.title('Mesures de photo-électrons sur la source')
plt.savefig('Mesures_Source_2.png', bbox_inches='tight')
plt.legend()
plt.show()

moyenne_fond = st.mean(fond)
ecart_type_fond = st.stdev(fond)
moyenne_source_fond = st.mean(source)
ecart_type_source_fond = st.stdev(source)
print(f"Moyenne du fond : {moyenne_fond:.2f} photo-électrons")
print(f"Écart-type du fond : {ecart_type_fond:.2f} photo-électrons")
print(f"Moyenne de la source + fond : {moyenne_source_fond:.2f} photo-électrons")
print(f"Écart-type de la source + fond : {ecart_type_source_fond:.2f} photo-électrons")

def Autocor(x):
    # Autocorrelation normalisee de x
    xc = x.copy() ; xc -= xc.mean()
    a = np.correlate(xc,xc,mode="full")[xc.size-1:]/np.arange(xc.size,0,-1)
    a /= xc.std()**2
    return a

autocorr_fond = Autocor(fond)
autocorr_source = Autocor(source)

plt.plot(pauses, autocorr_fond, label="Autocorrélation du fond")
plt.grid(True)
plt.xlabel("Indice de la pause")
plt.ylabel("Facteur d'autocorrélaton normalisé")
plt.title("Fonctions d'autocorrélations du fond")
plt.savefig('AutocorrelFond_2.png', bbox_inches='tight')
plt.legend()
plt.show()

plt.plot(pauses_source, autocorr_source, label="Autocorrélation de la source")
plt.grid(True)
plt.xlabel("Indice de la pause")
plt.ylabel("Facteur d'autocorrélaton normalisé")
plt.title("Fonctions d'autocorrélations de la source")
plt.savefig('AutocorrelSource_2.png', bbox_inches='tight')
plt.legend()
plt.show()

moyenne_source = moyenne_source_fond - moyenne_fond
ecart_type_source = np.sqrt((ecart_type_source_fond**2)/len(source) + (ecart_type_fond**2)/len(fond))
print(f"Signal de la source avec le fond soustrait : {moyenne_source:.2f} photo-électrons")
print(f"Écart-type du signal de la source avec le fond soustrait : {ecart_type_source:.2f} photo-électrons")

# Fréquence d'échantillonnage (en cycles par pause)
fech = 1.0

# Centrer les mesures et calculer la FFT
mesures_fond = fond - np.mean(fond)
mesures_source = source - np.mean(source)
fft_mesures_fond = fft(mesures_fond)
fft_mesures_source = fft(mesures_source)

# Affichage du spectre complet pour le fond (axe X = indices de 0 à 500)
plt.stem(np.abs(fft_mesures_fond))
plt.xlabel("Indice de fréquence")
plt.ylabel("Amplitude")
plt.title("Transformée de Fourier des mesures du fond")
plt.grid(True)
plt.savefig('FFT_Mesures_Fond.png', bbox_inches='tight')
plt.show()

# Affichage du spectre complet pour la source (axe X = indices de 0 à 200)
plt.stem(np.abs(fft_mesures_source))
plt.xlabel("Indice de fréquence")
plt.ylabel("Amplitude")
plt.title("Transformée de Fourier des mesures de la source")
plt.grid(True)
plt.savefig('FFT_Mesures_Source.png', bbox_inches='tight')
plt.show()

# Recherche des maximums UNIQUEMENT sur la première moitié pour ne pas fausser le résultat avec le reflet
N_fond = len(fond)
N_source = len(source)
indice_max_fond = np.argmax(np.abs(fft_mesures_fond[:N_fond//2]))
indice_max_source = np.argmax(np.abs(fft_mesures_source[:N_source//2]))

# Les fréquences en cycles par pause (indice / nombre total de mesures)
frequence_max_fond = indice_max_fond / N_fond
frequence_max_source = indice_max_source / N_source

print(f"Fréquence maximale pour le fond : {frequence_max_fond:.2f} cycle par pause")
print(f"Fréquence maximale pour la source : {frequence_max_source:.2f} cycle par pause")

# Filtrage de la source aux indices parasites
fft_source_filtree = fft_mesures_source.copy()
fft_source_filtree[20] = 0
fft_source_filtree[180] = 0

# Affichage de la FFT filtrée de la source
plt.stem(np.abs(fft_source_filtree))
plt.xlabel("Indice de fréquence")
plt.ylabel("Amplitude")
plt.title("Transformée de Fourier filtrée des mesures de la source")
plt.grid(True)
plt.savefig('FFT_Mesures_Source_Filtree.png', bbox_inches='tight')
plt.show()

# Affichage du signal filtré de la source après transformation inverse
signal_filtre = ifft(fft_source_filtree)
plt.plot(np.real(signal_filtre))
plt.xlabel("Indice de la pause")
plt.ylabel("Amplitude")
plt.title("Signal filtré de la source")
plt.grid(True)
plt.savefig('Signal_Filtre_Source.png', bbox_inches='tight')
plt.show()

# Histogramme du signal filtré de la source et comparaison du rapport signal sur bruit avec le signal non filtré
signal_filtre = np.real(signal_filtre) + np.mean(source)
plt.hist(signal_filtre, bins=15, alpha=0.5, label='Signal filtré')
plt.hist(source, bins=15, alpha=0.5, label='Signal non filtré')
plt.xlabel('Nombre de photo-électrons')
plt.ylabel('Nombre d\'occurrences de ces valeurs de photo-électrons')
plt.title('Histogramme du signal filtré de la source et comparaison avec le signal non filtré')
plt.grid(True)
plt.legend()
plt.savefig('Histogramme_Signal_Filtre_Source.png', bbox_inches='tight')
plt.show()

rapport_signal_bruit_filtre = (np.mean(signal_filtre)) / np.std(signal_filtre)
rapport_signal_bruit_non_filtre = (np.mean(source) / np.std(source))
print(f"Rapport signal sur bruit du signal filtré : {rapport_signal_bruit_filtre:.2f}")
print(f"Rapport signal sur bruit du signal non filtré : {rapport_signal_bruit_non_filtre:.2f}")
print(f"Amélioration du rapport signal sur bruit après filtrage : {rapport_signal_bruit_filtre / rapport_signal_bruit_non_filtre:.2f} fois")