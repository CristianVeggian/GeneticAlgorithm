from time import sleep
import Coadjuvante as cd
import random
import matplotlib.pyplot as plt

cmax = 100
nmax = 100

coadjs = []

for i in range(cmax):
    coadjs.append(cd.Coadjuvante(random.randint(-400, 400), random.randint(-400,400)))
    #coadjs[i].printaPosicao()

for ger in range(nmax):
    plt.clf()
    plt.title("Geração " + str(ger))
    # fazer o gene afetar o comportamento
    for _ in range(4):
        for coad in coadjs:
            for i in range(0, 4):
                if coad.gene1[i][0] == 'N':
                    coad.y = coad.yi + coad.gene1[i][1]
                elif coad.gene1[i][0] == 'L':
                    coad.x = coad.xi + coad.gene1[i][1]
                elif coad.gene1[i][0] == 'S':
                    coad.y = coad.yi - coad.gene1[i][1]
                elif coad.gene1[i][0] == 'O':
                    coad.x = coad.xi - coad.gene1[i][1]
    # fazer o critério de seleção (matar == tirar da lista)
    # mostra a posicao final
    eixoXfim = []
    eixoYfim = []
    eixoX = []
    eixoY = []
    for coad in coadjs:
        eixoX.append(coad.xi)
        eixoY.append(coad.yi)
    for coad in coadjs:
        coad.calculaFit()
        if coad.fit < 0:
            coadjs.remove(coad)
        eixoXfim.append(coad.x)
        eixoYfim.append(coad.y)
    # critério de avaliação (fitting)
    coadjs.sort(key=lambda x: x.fit)
    goodPais = []
    for coad in coadjs:
        coad.printaGene1()
        if coad.fit > 0:
            goodPais.append(coad)
    coadjs.clear()
    for k in range(0, cmax):
        papitos = random.sample(goodPais, 2)
        coadjs.append(cd.Coadjuvante(random.randint(-400, 400), random.randint(-400, 400), papitos[0], papitos[1]))
    plt.axis([-1000, 1000, -1000, 1000])
    plt.plot(eixoXfim, eixoYfim, 'r^')
    plt.plot(eixoX, eixoY, 'gs')
    plt.pause(3)
    

plt.show()
    