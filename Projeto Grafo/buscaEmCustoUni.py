from collections import deque, namedtuple

# De padrão a distância dos vértices é infinita
inf = float('inf')
Aresta = namedtuple('Aresta', 'comeco, fim, custo')


def cria_aresta(comeco, fim, custo=1):
  return Aresta(comeco, fim, custo)


class Grafo_U:
    def __init__(self, arestas):
        arestas_erradas = [i for i in arestas if len(i) not in [2, 3]]
        if arestas_erradas:
            raise ValueError('Conteúdo de arestas errado: {}'.format(arestas_erradas))

        self.arestas = [cria_aresta(*aresta) for aresta in arestas]

    @property
    def vertices(self):
        return set(
            sum(
                ([aresta.comeco, aresta.fim] for aresta in self.arestas), []
            )
        )

    def get_dupla_vertices(self, n1, n2, ambos_fecham=True):
        if ambos_fecham:
            dupla_vertices = [[n1, n2], [n2, n1]]
        else:
            dupla_vertices = [[n1, n2]]
        return dupla_vertices

    def remove_aresta(self, n1, n2, ambos_fecham=True):
        dupla_vertices = self.get_dupla_vertices(n1, n2, ambos_fecham)
        arestas = self.arestas[:]
        for aresta in arestas:
            if [aresta.comeco, aresta.fim] in dupla_vertices:
                self.arestas.remove(aresta)

    def add_aresta(self, n1, n2, custo=1, ambos_fecham=True):
        dupla_vertices = self.get_dupla_vertices(n1, n2, ambos_fecham)
        for aresta in self.arestas:
            if [aresta.comeco, aresta.fim] in dupla_vertices:
                return ValueError('Aresta {} {} já existe'.format(n1, n2))

        self.arestas.append(Aresta(comeco=n1, fim=n2, custo=custo))
        if ambos_fecham:
            self.arestas.append(Aresta(comeco=n2, fim=n1, custo=custo))

    @property
    def vizinhos(self):
        vizinhos = {vertice: set() for vertice in self.vertices}
        for aresta in self.arestas:
            vizinhos[aresta.comeco].add((aresta.fim, aresta.custo))

        return vizinhos

    def dijkstraCustoUniforme(self, origem, destino):
        assert origem in self.vertices, "Este vértice de origem não existe!"
        distancias = {vertice: inf for vertice in self.vertices}
        vertices_anteriores = {
            vertice: None for vertice in self.vertices
        }
        distancias[origem] = 0
        vertices = self.vertices.copy()

        while vertices:
            vertice_atual = min(
                vertices, key=lambda vertice: distancias[vertice])
            vertices.remove(vertice_atual)
            if distancias[vertice_atual] == inf:
                break
            for vizinho, custo in self.vizinhos[vertice_atual]:
                caminho_alternativo = distancias[vertice_atual] + custo
                if caminho_alternativo < distancias[vizinho]:
                    distancias[vizinho] = caminho_alternativo
                    vertices_anteriores[vizinho] = vertice_atual

        caminho, vertice_atual = deque(), destino
        while vertices_anteriores[vertice_atual] is not None:
            caminho.append_esq(vertice_atual)
            vertice_atual = vertices_anteriores[vertice_atual]
        if caminho:
            caminho.append_esq(vertice_atual)
        return caminho