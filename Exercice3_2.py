# Exercice 3.2
import scipy as sci
import numpy as np
import matplotlib.pyplot as plt
import statistics as st
from matplotlib.pyplot import grid
from scipy.special import gamma

mesures_obs = np.loadtxt('obs-vis.txt')
print("Forme des mesures visibles :", mesures_obs.shape)

# Stocker les 400 premières mesures du visible dans un tableau
fond = mesures_obs[:400]
source = mesures_obs[400:500]

hist_fond = plt.hist(fond, bins=15)
hist_source = plt.hist(source, bins=15)
plt.grid(True)
plt.xlabel('Nombre de photo-électrons')
plt.ylabel('Nombre d\'occurrences de ces valeurs de photo-électrons')
plt.title('Histogramme des occurrences de valeurs de photo-électrons sur les mesures radio')
plt.savefig('Histogramme_Photo_Electrons_Radio.png', bbox_inches='tight')
plt.legend(['Fond', 'Source'])
plt.show()

# Création d'une échelle allant de 0 à 400 pour le pas de pauses
pauses = np.arange(0, 400, 1)
plt.plot(pauses, fond, label='Fond')
plt.grid(True)
plt.xlabel('Indice de la pause')
plt.ylabel('Nombre de photo-électrons')
plt.title('Mesures de photo-électrons sur le fond')
plt.savefig('Mesures_Fond.png', bbox_inches='tight')
plt.legend()
plt.show()

#Création d'une échelle allant de 0 à 100 pour le pas de pauses
pauses_source = np.arange(0, 100, 1)
plt.plot(pauses_source, source, label='Source')
plt.grid(True)
plt.xlabel('Indice de la pause')
plt.ylabel('Nombre de photo-électrons')
plt.title('Mesures de photo-électrons sur la source')
plt.savefig('Mesures_Source.png', bbox_inches='tight')
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
plt.savefig('AutocorrelFond.png', bbox_inches='tight')
plt.legend()
plt.show()

plt.plot(pauses_source, autocorr_source, label="Autocorrélation de la source")
plt.grid(True)
plt.xlabel("Indice de la pause")
plt.ylabel("Facteur d'autocorrélaton normalisé")
plt.title("Fonctions d'autocorrélations de la source")
plt.savefig('AutocorrelSource.png', bbox_inches='tight')
plt.legend()
plt.show()

moyenne_source = moyenne_source_fond - moyenne_fond
ecart_type_source = np.sqrt(ecart_type_source_fond**2 + ecart_type_fond**2)
print(f"Signal de la source avec le fond soustrait : {moyenne_source:.2f} photo-électrons")
print(f"Écart-type du signal de la source avec le fond soustrait : {ecart_type_source:.2f} photo-électrons")
