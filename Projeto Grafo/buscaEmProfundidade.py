class Vertice_P:
    def __init__(self, n):
        self.nome = n
        self.vizinhos = list()
        
        self.tempo_descoberta = 0
        self.tempo_fim = 0
        self.cor = "preto"

    def add_vizinho(self, v):
        nset = set(self.vizinhos)
        if v not in nset:
            self.vizinhos.append(v)
            self.vizinhos.sort()

class Grafo_P:
    vertices = {}
    tempo = 0

    def add_vertice(self, vertice):
        if isinstance(vertice, Vertice_P) and vertice.nome not in self.vertices:
            self.vertices[vertice.nome] = vertice
            return True
        else:
            print("Erro ao registrar novo vértice.")
            return False
        
    def add_aresta(self, u, v):
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
                  + str(self.vertices[key].tempo_descoberta) + " "
                  + str(self.vertices[key].tempo_fim) + " "
                  + str(self.vertices[key].cor))

    # Cor Vermelho = vértice atual
    # Cor Preto = vértice ainda não visitado
    # Cor Azul = vértice já visitado

    def _buscaEmProfundidade(self, vertice):
        global tempo
        vertice.cor = "vermelho"
        vertice.tempo_descoberta = tempo
        tempo += 1
        for v in vertice.vizinhos:
            if self.vertices[v].cor == "preto":
                self._buscaEmProfundidade(self.vertices[v])        
        vertice.cor = "azul"
        vertice.tempo_fim = tempo
        tempo += 1

    def buscaEmProfundidade(self, vertice):
        global tempo
        tempo = 1
        self._buscaEmProfundidade(vertice)