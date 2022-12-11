import random
from Utils import utilTupla

xLim = 1000
yLim = 1000
chanceMutacao = 5
listaGenes1 = ['N', 'L', 'S', 'O']
#[(N,20), (L, 10), (N, 5), (S ,15)]- exemplo

idGlobal = 0

class Coadjuvante:

    fit = 0

    def __init__(self, x, y, genePai1 = None, genePai2 = None):
        global idGlobal
        self.id = idGlobal
        idGlobal = idGlobal + 1
        self.xi = x
        self.x = x
        self.yi = y
        self.y = y
        self.gene1 = self.__geraGene1(genePai1, genePai2)

    def __geraGene1(self, genePai1, genePai2):
        gene = []
        if not genePai1 and not genePai2:
            for i in range(4):
                ge = (random.choice(listaGenes1))
                if ge == 'N' or ge == 'S':
                    gene.append((ge, random.randint(0, 1000-self.y)))
                else:
                    gene.append((ge, random.randint(0, 1000-self.x)))
        elif genePai1 and genePai2:
            gp1 = genePai1.gene1.copy()
            gp2 = genePai2.gene1.copy()
            gene.append(gp1[0])
            gene.append(gp1[1])
            gene.append(gp2[2])
            gene.append(gp2[3])
            #calcula a chance de mutação
            if random.randint(1, 100) <= chanceMutacao:
                idx = random.randint(0,3)
                #escolhe qual característica do genoma pra mutar
                if random.randint(0,1) == 0: #direção
                    gene[idx] = utilTupla(gene[idx], 0, random.choice(listaGenes1))
                else: #amplitude
                    gene[idx] = utilTupla(gene[idx], 1, random.randint(0,300))
        return gene

    def printaGene1(self):
        print(self.gene1)

    def printaPosicao(self):
        print("ID" + str(self.id) + " X:" + str(self.x) + " - Y:" + str(self.y))

    def printaCoad(self):
        print("------------")
        print("ID" + str(self.id) + "\nX:" + str(self.x) + " - Y:" + str(self.y))
        print("------------")

    def executaGene1(self):
        for i in range(0, 4):
            if self.gene1[i][0] == 'N':
                self.y = self.yi + self.gene1[i][1]
                if self.y >= yLim:
                    self.y = yLim - random.randint(100,1000)
            elif self.gene1[i][0] == 'L':
                self.x = self.xi + self.gene1[i][1]
                if self.x >= xLim:
                    self.x = xLim - random.randint(100,1000)
            elif self.gene1[i][0] == 'S':
                self.y = self.yi - self.gene1[i][1]
                if self.y <= -yLim:
                    self.y = -yLim + random.randint(100,1000)
            elif self.gene1[i][0] == 'O':
                self.x = self.xi - self.gene1[i][1]
                if self.x <= -xLim:
                    self.x = -xLim + random.randint(100,1000)

    def calculaFit(self):
        self.fit = self.x + self.y
        self.fit -= 2000
        self.fit = 1/(1+self.fit)