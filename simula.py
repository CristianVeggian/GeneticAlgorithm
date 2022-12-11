from time import sleep
import Coadjuvante as cd
import random
import matplotlib.pyplot as plt
import numpy as np

coadMax = 100
gerMax = 1000

coadjs = []

img = plt.imread("mapa.png")
fig, ax = plt.subplots(1, 1)


for i in range(coadMax):
    coadjs.append(cd.Coadjuvante(random.randint(-1000, 1000), random.randint(-1000,1000)))
    #coadjs[i].printaPosicao()

for ger in range(gerMax):
    ax.clear()
    plt.title("Geração " + str(ger))
    # fazer o gene afetar o comportamento
    for coad in coadjs:
        coad.executaGene1()        
    # fazer o critério de seleção (matar == tirar da lista)
    # mostra a posicao final
    eixoXfim = []
    eixoYfim = []
    eixoX = []
    eixoY = []
    for coad in coadjs:
        eixoX.append(coad.xi)
        eixoY.append(coad.yi)
        eixoXfim.append(coad.x)
        eixoYfim.append(coad.y)
        coad.calculaFit()
    # critério de avaliação (fitting)
    coadjs.sort(key=lambda x: x.fit)
    goodParents = []
    probs = []
    total = 0
    for coad in coadjs:
        total += coad.fit 
        goodParents.append(coad)
    coadjs.clear()
    for parent in goodParents:
        probs.append(parent.fit/total)
    for k in range(0, coadMax):
        papitos = np.random.choice(goodParents, size=2, p=probs)
        coadjs.append(cd.Coadjuvante(random.randint(-1000, 1000), random.randint(-1000, 1000), papitos[0], papitos[1]))
    ax.imshow(img, extent=[-1000, 1000, -1000, 1000])
    ax.plot(eixoXfim, eixoYfim, 'Dw')
    ax.plot(eixoX, eixoY, '.c')
    plt.pause(0.001)
    

plt.show()
    