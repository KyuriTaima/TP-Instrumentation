# Exercice 4.3
import scipy as sci
import numpy as np
import matplotlib.pyplot as plt
import statistics as st
from matplotlib.pyplot import grid
from scipy.special import gamma
from numpy.fft import fft, ifft
from numpy.fft import fft, fftfreq

mesures1 = np.loadtxt('rameau1.txt')
mesures2 = np.loadtxt('rameau2.txt')
print("Forme des mesures 1 :", mesures1.shape)
print("Forme des mesures 2 :", mesures2.shape)

temps1 = mesures1[:,0] * 1e-3
tension1 = mesures1[:,1]
temps2 = mesures2[:,0] * 1e-3
tension2 = mesures2[:,1]

# tension1 = tension1 - np.mean(tension1)
p = np.ones(51, dtype='float') / 51
c = np.correlate(tension1, p, mode='same')
plt.plot(temps1, c)
plt.xlabel("Temps (s)")
plt.ylabel("Tension (V)")
plt.title("Convolution de la tension sur Rameau 1 par la fonction porte")
plt.legend()
plt.savefig('ConvolutionSignalPorteNonCorrige.png', bbox_inches='tight')
plt.show()
print(len(c))

moyenne_tension1 = np.mean(tension1)

tension1 = tension1 - moyenne_tension1
p = np.ones(51, dtype='float') / 51
c = np.correlate(tension1, p, mode='same')
c = c + np.mean(tension1)
plt.plot(temps1, c)
plt.xlabel("Temps (s)")
plt.ylabel("Tension (V)")
plt.title("Convolution de la tension sur Rameau 1 par la fonction porte, avec correction des bords")
plt.legend()
plt.savefig('ConvolutionSignalPortecorrige.png', bbox_inches='tight')
plt.show()

# FFT
tension1 = tension1 + moyenne_tension1
p = 1./51 * np.hstack((np.ones(26) , np.zeros(tension1.size - 51), np.ones(25)))
c = ifft(fft(tension1) * fft(p)).real + moyenne_tension1

plt.plot(temps1, c)
plt.xlabel("Temps (s)")
plt.ylabel("Tension (V)")
plt.title("Lissage dans l'espace de Fourier par multiplication par une porte")
plt.legend()
plt.savefig('LissageParFourier.png', bbox_inches='tight')
#plt.show()

# FFT avec une porte de 501 échantillons
p = 1./501 * np.hstack((np.ones(251) , np.zeros(tension1.size - 501), np.ones(250)))
c = ifft(fft(tension1) * fft(p)).real + moyenne_tension1

plt.plot(temps1, c)
plt.xlabel("Temps (s)")
plt.ylabel("Tension (V)")
plt.title("Lissage dans l'espace de Fourier par multiplication par une porte (501)")
plt.legend()
plt.savefig('LissageParFourier501.png', bbox_inches='tight')
plt.show()

plt.plot(np.real(fft(p)))
p = 1./251 * np.hstack((np.ones(251) , np.zeros(tension1.size - 251)))
plt.plot(np.real(fft(p)))
p = 1./501 * np.hstack((np.ones(501) , np.zeros(tension1.size - 501)))
plt.plot(np.real(fft(p)))
plt.show()

print(f"Partie imaginaire du signal: : {np.mean(np.imag(c))} ")

# FFT sans les corrections de tension
tension1 = tension1 + moyenne_tension1
p = 1./501 * np.hstack((np.ones(251) , np.zeros(tension1.size - 501), np.ones(250)))
c = ifft(fft(tension1) * fft(p)).real

plt.plot(temps1, c)
plt.xlabel("Temps (s)")
plt.ylabel("Tension (V)")
plt.title("Lissage dans l'espace de Fourier par multiplication par une porte (501) sans correction de la moyenne")
plt.legend()
plt.savefig('LissageParFourier501SansCorrectionMoyenne.png', bbox_inches='tight')
plt.show()

dse_rameau1 = np.abs(fft(tension1 - moyenne_tension1) * fft(p))**2
plt.plot(temps1, dse_rameau1)
plt.show()



