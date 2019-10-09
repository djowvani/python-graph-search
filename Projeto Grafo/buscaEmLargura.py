class Vertice_L:
    def __init__(self, n):
        self.nome = n
        self.vizinhos = list()
        
        self.distancia = 9999
        self.cor = "preto"

    def add_vizinho(self, v):
        nset = set(self.vizinhos)
        if v not in nset:
            self.vizinhos.append(v)
            self.vizinhos.sort()

class Grafo_L:
    vertices = {}
    tempo = 0

    def add_vertice(self, vertice):
        if isinstance(vertice, Vertice_L) and vertice.nome not in self.vertices:
            self.vertices[vertice.nome] = Vertice_L(vertice)
            return True
        else:
            return False
        
    def add_aresta(self, u, v):
        if isinstance(v, list):
            for x in range(len(v)):
                v = v[x]
                if u in self.vertices and v in self.vertices:
                    for key, value in self.vertices.items():
                        if key == u:
                            value.add_aresta(v)
                        if key == v:
                            value.add_aresta(u)
                    return True
        else:
            if u in self.vertices and v in self.vertices:
                for key, value in self.vertices.items():
                    if key == u:
                        value.add_aresta(v)
                    if key == v:
                        value.add_aresta(u)
                return True
            else:
                return False

    def print_mapa(self):
        for key in sorted(list(self.vertices.keys())):
            print(key
                  + str(self.vertices[key].vizinhos) + " "
                  + str(self.vertices[key].distancia) + " "
                  + str(self.vertices[key].cor))

    def buscaEmLargura(self, vertice):
        q = list()
        vertice.distancia = 0
        vertice.cor = "vermelho"
        print(len(Vertice_L(vertice).vizinhos))
        for v in Vertice_L(vertice).vizinhos:
            print("============= TESTE 1")
            self.vertices[v].distancia = vertice.distancia + 1
            q.append(v)
            print("============= TESTE 2")

        while len(q) > 0:
            u = q.pop(0)
            node_u = self.vertices[u]
            node_u.cor = "vermelho"

            for v in node_u.vizinhos:
                node_v = self.vertices[v]
                if node_v.cor == "preto":
                    q.append(v)
                    if node_v.distancia > node_u.distancia + 1:
                        node_v.distancia = node_u.distancia +1