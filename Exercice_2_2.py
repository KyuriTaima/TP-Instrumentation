import scipy as sci
import numpy as np
import matplotlib.pyplot as plt
import statistics as st
from matplotlib.pyplot import grid

im = plt.imread('saturne.png')
print("Taille de l'image :", im.shape) 
plt.imshow(im)
plt.show()
r = im[:,:,0]
g = im[:,:,1]
b = im[:,:,2]
plt.imshow(r, cmap='gray')
# Force the range of the color scale to be between 0 and 1
plt.clim(0, 1)
plt.colorbar()
plt.title('Composante rouge')
plt.savefig('ComposanteRouge.png', bbox_inches='tight')
plt.show()

plt.imshow(g, cmap='gray')
plt.colorbar()
plt.clim(0, 1)
plt.title('Composante verte')
plt.savefig('ComposanteVerte.png', bbox_inches='tight')
plt.show()

plt.imshow(b, cmap='gray')
plt.clim(0, 1)
plt.colorbar()
plt.title('Composante bleue')
plt.savefig('ComposanteBleue.png', bbox_inches='tight')
plt.show()

r_1d = np.reshape(r, 617*480)
g_1d = np.reshape(g, 617*480)
b_1d = np.reshape(b, 617*480)

hist1 = plt.hist(r_1d, bins=10, density=True)

plt.title('Histogramme des densité de probabilité d\'obtenir une valeur de rouge')
plt.grid(True)
plt.xlabel('Intensité')
plt.ylabel('Densité de probabilité')
plt.savefig('DensiteR.png', bbox_inches='tight')
plt.show()

hist2 = plt.hist(g_1d, bins=10, density=True)
plt.title('Histogramme des densité de probabilité d\'obtenir une valeur de verte')
plt.grid(True)
plt.xlabel('Intensité')
plt.ylabel('Densité de probabilité')
plt.savefig('DensiteG.png', bbox_inches='tight')
plt.show()

hist3 = plt.hist(b_1d, bins=10, density=True)
plt.title('Histogramme des densité de probabilité d\'obtenir une valeur de bleue')
plt.grid(True)
plt.xlabel('Intensité')
plt.ylabel('Densité de probabilité')
plt.savefig('DensiteB.png', bbox_inches='tight')
plt.show()

# histrogrammes ensemble
hist1 = plt.hist(r_1d, bins=10, density=True, alpha=0.5, label='Rouge', color='red', range=[0,1])
hist2 = plt.hist(g_1d, bins=10, density=True, alpha=0.5, label='Vert', color='green', range=[0,1])
hist3 = plt.hist(b_1d, bins=10, density=True, alpha=0.5, label='Bleu', color='blue', range=[0,1])
plt.title('Histogramme des densité de probabilité d\'obtenir une valeur de couleur')
plt.grid(True)
plt.xlabel('Intensité')
plt.ylabel('Densité de probabilité')
plt.legend()
plt.savefig('DensiteRGB.png', bbox_inches='tight')
plt.show()

plt.plot(r_1d, b_1d, '.')
plt.grid(True)
plt.xlabel('Intensité rouge')
plt.ylabel('Intensité bleue')
plt.title('Corrélation entre les intensités rouge et bleue')
plt.savefig('correlationRB.png', bbox_inches='tight')
plt.axis('equal')
plt.show()

covrb = lambda x,y: np.sum((x - np.mean(x)) * (y - np.mean(y))) / len(x)
corcoefrb = lambda x,y: covrb(x,y) / (np.std(x) * np.std(y))
print(f"Coefficient de corrélation entre les intensités rouge et bleue : {corcoefrb(r_1d, b_1d):.2f}")