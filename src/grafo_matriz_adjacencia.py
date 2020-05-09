class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * vertices for i in range(vertices)]
        #print(self.grafo)

    def add_aresta(self, u, v):
        self.grafo[u - 1][v - 1] = 1
        self.grafo[v - 1][u - 1] = 1

    def show(self):
        for i in self.grafo:
            for j in i:
                print(j, end = ' ')
            print('')

    def tem_ligacao(self, u, v):
        if self.grafo[u-1][v-1] == 1:
            return True
        return False

g = Grafo(5)
g.add_aresta(1, 3)
g.add_aresta(3, 4)
g.add_aresta(2, 3)
g.add_aresta(3, 5)
g.add_aresta(4, 5)

g.show()

print(g.tem_ligacao(1, 5))
print(g.tem_ligacao(1, 3))

print('#################### - LISTA DE ADJACENCIA- #######################')

class GrafoDir:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(vertices)]

    def add_aresta(self, u, v):
        self.grafo[u-1].append(v-1)

    def show(self):
        for i in range(self.vertices):
            print('%d: ' % (i+1), end = ' ')
            for j in self.grafo[i]:
                print('%d ->' % (j+1), end = ' ')
            print('')

g2 = GrafoDir(5)

g2.add_aresta(1, 2)
g2.add_aresta(4, 1)
g2.add_aresta(2, 3)
g2.add_aresta(2, 5)
g2.add_aresta(5, 3)

g2.show()
