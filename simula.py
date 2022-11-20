from time import sleep
import Coadjuvante as cd
import random
import matplotlib.pyplot as plt

cmax = 10
nmax = 10

coadjs = []

for i in range(cmax):
    coadjs.append(cd.Coadjuvante(random.randint(-400, 400), random.randint(-400,400)))
    coadjs[i].printaPosicao()

for ger in range(nmax):
    # fazer o gene afetar o comportamento
    for coad in coadjs:
        for i in range(4):
            if coad.gene1[i][0] == 'N':
                coad.y = coad.y + coad.gene1[i][1]
            elif coad.gene1[i][0] == 'L':
                coad.x = coad.x + coad.gene1[i][1]
            elif coad.gene1[i][0] == 'S':
                coad.y = coad.y - coad.gene1[i][1]
            elif coad.gene1[i][0] == 'O':
                coad.x = coad.x - coad.gene1[i][1]
    # fazer o critério de seleção (matar == tirar da lista)
    for coad in coadjs:
        coad.calculaFit()
        if coad.x < 0 or coad.y < 0:
            coadjs.remove(coad)
    # critério de avaliação (fitting)
    coadjs.sort(key=lambda x: x.fit)
    if(len(coadjs)) < 2:
        print("É o fim...")
        break
    goodPais = []
    for coad in coadjs:
        if coad.fit > 0:
            goodPais.append(coad)
            coadjs.remove(coad)
    if len(goodPais) < 2:
        goodPais.append(random.choice(coadjs))
    for k in range(0, cmax):
        papitos = random.sample(goodPais, 2)
        coadjs.append(cd.Coadjuvante(random.randint(-400, 400), random.randint(-400,400) , papitos[0], papitos[1]))
    # mostra a posicao final
    print("Geração " + str(ger))
    eixoX = []
    eixoY = []
    for coad in coadjs:
        eixoX.append(coad.x)
        eixoY.append(coad.y)
    plt.axis([-400, 400, -400, 400])
    plt.plot(eixoX, eixoY, 'r^')
    plt.show()
    