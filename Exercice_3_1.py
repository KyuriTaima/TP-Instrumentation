import scipy as sci
import numpy as np
import matplotlib.pyplot as plt
import statistics as st
from matplotlib.pyplot import grid

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


# Construction de la densité de probabilité à posteriori de la tension v connaissant la précision instrumenetale sigma = 0,2421 pour 1, 10, 100 et 700 mesures
sigma = 0.2421
# Moyenne des carrés des mesures
m2 = np.mean(tension**2)
# Carré des moyennes des mesures
m1 = np.mean(tension)**2
s = np.sqrt(m2-m1)
# Moyenne arithmétique des mesures
m = np.mean(tension)
n = tension.size
# on boucle sur les valeurs de n pour construire les distributions à posteriori
x_radio = np.linspace(tension.min(), tension.max(), 100)
step = 0.01
x_radio = np.arange(tension.min(), tension.max(), step)
gauss = lambda x,m,s,n: ((1/np.sqrt(2*np.pi*sigma))**n)*np.exp(-n*s**2/(2*sigma**2)*((x-m)**2/(sigma/np.sqrt(n))**2))
for n in [1, 10, 100, 700]:
    f_tension_a_posteriori = gauss(x_radio, mvec[n-1], np.sqrt(-mvec[n-1]**2 + np.mean(tension[:n]**2)), n)
    # Etape 1 Construction de la distribution à priori des erreurs
    # f_tension_a_posteriori = []
    # for i in range(x_radio.size):
        # f_tension_a_posteriori.append(((1/np.sqrt(2*np.pi*sigma))**n)*np.exp(-n*s**2/(2*sigma**2)*((x_radio[i]-mvec[n-1])**2/(sigma/np.sqrt(n))**2)))
    # normalisation de la distribution à posteriori
    f_tension_a_posteriori = f_tension_a_posteriori/(np.sum(f_tension_a_posteriori)*step)
    plt.plot(x_radio,f_tension_a_posteriori,label="n = "+str(n))
plt.title("Densité de probabilité à posteriori de la tension v connaissant la précision instrumentale sigma = 0,2421 pour n mesures")
plt.grid(True)
plt.xlabel("Tension (V)")
plt.ylabel("Densité de probabilité")
plt.axvline(x=m, color='r', linestyle='--', label='Moyenne des mesures = {:.2f} V'.format(m))
plt.legend()
plt.savefig('DensiteProbabilitePosterioriRadio_n_'+str(n)+'.png', bbox_inches='tight')
plt.show()