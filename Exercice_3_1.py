import scipy as sci
import numpy as np
import matplotlib.pyplot as plt
import statistics as st
from matplotlib.pyplot import grid
from scipy.special import gamma

mesures_radio = np.loadtxt('obs-radio.txt')
print("Forme des mesures radio :", mesures_radio.shape)
temps = mesures_radio[:,0] * 1e-3
tension = mesures_radio[:,1]
hist = plt.hist(tension, bins=25)
plt.grid(True)
plt.xlabel('Tension (V)')
plt.ylabel('Nombre d\'occurrences de ces valeurs de tension')
plt.title('Histogramme des occurrences de valeurs de tension sur les mesures radio')
plt.savefig('Histogramme_Tension_Radio.png', bbox_inches='tight')
plt.show()

hist = plt.hist(tension, bins=25, density=True)
plt.grid(True)
plt.xlabel('Tension (V)')
plt.ylabel('Densité de probabilité')
plt.title('Histogramme des densités de probabilité d\'obtenir une valeur de tension sur les mesures radio')
plt.savefig('Histogramme_Densite_Tension_Radio.png', bbox_inches='tight')
plt.show()

def Autocor(x):
    # Autocorrelation normalisee de x
    xc = x.copy() ; xc -= xc.mean()
    a = np.correlate(xc,xc,mode="full")[xc.size-1:]/np.arange(xc.size,0,-1)
    a /= xc.std()**2
    return a
autocorr_radio = Autocor(tension)

plt.plot(temps, autocorr_radio, label="Autocorrélation des mesures radio")
plt.title("Fonctions d'autocorrélations des mesures radio")
plt.xlabel("Temps (s)")
plt.ylabel("Facteur d'autocorrélaton normalisé")
plt.legend()
plt.grid(True)
plt.savefig('AutocorrelRadio.png', bbox_inches='tight')
plt.show()

mvec = np.array(tension[0])
for i in range(2,tension.size+1):
    mvec = np.append(mvec,tension[:i].mean())

#tracer la moyenne glissante des mesures radio en fonction du nombre de mesures prises en compte
plt.plot(np.arange(1,tension.size+1),mvec,label="Moyenne glissante des mesures radio")
plt.title("Moyenne glissante des mesures radio")
plt.grid(True)
plt.xlabel("Nombre de mesures prises en compte")
plt.ylabel("Tension (V)")
plt.legend()
plt.savefig('MoyenneGlissanteRadio.png', bbox_inches='tight')
plt.show()

svec = np.zeros(1)
for i in range(2,tension.size+1):
    svec = np.append(svec,tension[:i].std())

#tracer l'écart-type glissant des mesures radio en fonction du nombre de mesures prises en compte
plt.plot(np.arange(1,tension.size+1),svec,label="Ecart-type glissant des mesures radio")
plt.title("Ecart-type glissant des mesures radio")
plt.grid(True)
plt.xlabel("Nombre de mesures prises en compte")
plt.ylabel("Tension (V)")
plt.legend()
plt.savefig('EcartTypeGlissantRadio.png', bbox_inches='tight')
plt.show()


# Construction de la densité de probabilité à posteriori
sigma = 0.2421
m = np.mean(tension)
n_total = tension.size

# Création d'un axe x suffisamment large pour voir les cloches
x_radio = np.linspace(tension.min(), tension.max(), 1000)

# Définition de la densité de probabilité a posteriori exacte (déjà normalisée)
# L'écart-type a posteriori est sigma / sqrt(n)
gauss_posteriori = lambda x, m_mesure, n_mesure: (1 / (np.sqrt(2 * np.pi) * (sigma / np.sqrt(n_mesure)))) * np.exp(-0.5 * ((x - m_mesure) / (sigma / np.sqrt(n_mesure)))**2)

for n in [1, 10, 100, 700]:
    # On récupère la moyenne glissante pour n mesures
    moyenne_n = mvec[n-1]
    print(f"Moyenne glissante pour n = {n} : {moyenne_n:.2f} V")
    print(f"Écart-type glissant pour n = {n} : {svec[n-1]:.2f} V")
    print(f"Écart-type a posteriori pour n = {n} : {sigma / np.sqrt(n):.4f} V")
    
    # Calcul de la distribution
    f_tension_a_posteriori = gauss_posteriori(x_radio, moyenne_n, n)
    
    plt.plot(x_radio, f_tension_a_posteriori, label=f"n = {n}")

plt.title("Densité de probabilité a posteriori (sigma = 0.2421)")
plt.grid(True)
plt.xlabel("Tension (V)")
plt.ylabel("Densité de probabilité")
plt.axvline(x=m, color='r', linestyle='--', label=f'Moyenne finale = {m:.2f} V')
plt.legend()
plt.savefig('DensiteProbabilitePosterioriRadio.png', bbox_inches='tight')
plt.show()

# Densité de probabilité a posteriori pour n = 4, 10 et 25 en utilisant une loi de Student

student = lambda x, m, s, n: gamma(0.5 * n) / gamma(0.5 * (n - 1)) / gamma(0.5) / s * (1 + ((x - m) / s)**2)**(-0.5 * n)

for n in [4, 10, 25]:
    # On récupère la moyenne glissante pour n mesures
    moyenne_n = mvec[n-1]
    print(f"Moyenne glissante pour n = {n} : {moyenne_n:.2f} V")
    print(f"Écart-type glissant pour n = {n} : {svec[n-1]:.2f} V")
    print(f"Écart-type a posteriori pour n = {n} : {sigma / np.sqrt(n-3):.2f} V")
    
    # Calcul de la distribution
    f_tension_a_posteriori_student = student(x_radio, moyenne_n, svec[n-1], n)
    
    plt.plot(x_radio, f_tension_a_posteriori_student, label=f"n = {n}")

plt.title("Densité de probabilité a posteriori (loi de Student)")
plt.grid(True)
plt.xlabel("Tension (V)")
plt.ylabel("Densité de probabilité")
plt.axvline(x=m, color='r', linestyle='--', label=f'Moyenne finale = {m:.2f} V')
plt.legend() 
plt.savefig('StudentRadioDensiteProbabilitePosteriori.png', bbox_inches='tight')
plt.show()