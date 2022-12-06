import random
from Utils import utilTupla

chanceMutacao = 10
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
                gene.append((random.choice(listaGenes1), random.randint(0, 600)))
        elif genePai1 and genePai2:
            gp1 = genePai1.gene1.copy()
            gp2 = genePai2.gene1.copy()
            gene.append(gp1[0])
            gene.append(gp1[1])
            gene.append(gp2[2])
            gene.append(gp2[3])
            #calcula a chance de mutação
            if random.randint(1, 100) <= chanceMutacao:
                #escolhe qual característica do genoma pra mutar
                if random.randint(0,1) == 0: #direção
                    utilTupla(gene[random.randint(0,3)], 0, random.choice(listaGenes1))
                else: #amplitude
                    utilTupla(gene[random.randint(0,3)], 1, random.randint(0,600))
        return gene

    def printaGene1(self):
        print(self.gene1)

    def printaPosicao(self):
        print("ID" + str(self.id) + " X:" + str(self.x) + " - Y:" + str(self.y))

    def printaCoad(self):
        print("------------")
        print("ID" + str(self.id) + "\nX:" + str(self.x) + " - Y:" + str(self.y))
        print("------------")

    def calculaFit(self):
        coord = (self.x - self.xi, self.y - self.yi)
        if coord[0] < 0 and coord[1] < 0:
            self.fit = -coord[0]*coord[1]
        else:
            self.fit = coord[0]*coord[1]
        self.fit = 1/(1+self.fit)
        print(self.fit)