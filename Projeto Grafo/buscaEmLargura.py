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
    def __init__(self):
        self.vertices = {}
        tempo = 0

    def add_vertice(self, vertice):
        if isinstance(vertice, Vertice_L) and vertice.nome not in self.vertices:
            self.vertices[vertice.nome] = vertice
            return True
        else:
            return False
        
    def add_aresta(self, u, v):
        if u.nome in self.vertices and v.nome in self.vertices:
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

def busca_de_Largura (grafo, inicio, fim, fila):
    if inicio in fila:
        print("ja na fila")
        return fila

    fila.append(inicio)
    print("Fila atual: " + str(fila))

    if fila[-1] == fim:
        print("chegou no fim")
        return fila

    vizinhos = grafo[inicio]
    print ("vizinhos: " + str(vizinhos))

    c = 0
    for vizinho in vizinhos:
        print ("No vizinho " + vizinho)
        if vizinho not in fila:
            c += 1
        if vizinho == fim: # XXXXXXXXXXX MUDAAA
            fila.append(vizinho)
            return fila # XXXXXXXXXXX MUDAAA

    if c == 0:
        fila.pop()
        return fila

    for vizinho in vizinhos:
        fila = buscaLargura(grafo, vizinho, fim, fila)
        print(fila)
        if fila[-1] == fim:
            return fila
    return fila

    #     if vizinho not in fila:
    #         fila = buscaLargura(grafo, vizinho, fim, fila)
    #         if fila[-1] == fim:
    #             return fila
    #     print("vizinho na fila")
    #     print ("fila " +str(fila))
    #     if vizinho == vizinhos[-1]:
    #         fila.pop()
    #         print("Fila depois do pop " + str(fila))
    #         return fila
    # return fila

def buscaLargura(grafo, inicio):
    fila = [] # fila da busca, afinal ela eh em largura! .append(elemento) -> adiciona elemento na fila ; .pop(0) -> proximo na fila
    # como os graus de entrada e saida de cada vertice sao iguais em uma busca em largura, chamamos ambos os valores de largura do vertice
    largura = {}
    l = 1 # contador de largura dos vertices na busca
    pai = {} # dicionario com os pais de cada vertice na arvore de busca em largura
    nivel = {} # nivel de cada vertice na arvore de busca em largura
    aresta = {} # classificacao das arestas na arvore de busca em largura do grafo

    # primeira insercao na fila eh o vertice do grafo escolhido arbitrariamente (passado como parametro dessa funcao)
    fila.append(inicio)
    largura[inicio] = l # a largura da raiz da arvore de busca em largura comeca por 1
    pai[inicio] = None # o primeiro vertice a entrar na fila (raiz da arvore de busca em largura) tem pai nulo (None object)
    nivel[inicio] = 1 # o nivel do primeiro vertice a entrar na fila a (raiz da arvore de busca em largura) eh 1

    # enquanto tivermos alguem na fila vamos continuar a busca. Grafos nao-conexos nao estao sendo tratados!
    while len(fila):
        vertice = fila.pop(0) # pega o proximo vertice da fila
        # colocando os vizinhos que ainda naum estavam na fila
        for vizinho in grafo.get(vertice):
            # testando se o vizinho jah foi visitado (se o get retornar None, significa que este vertice nunca entrou na fila)
            if not largura.get(vizinho): # se o vizinho ainda naum foi visitado...
                fila.append(vizinho) # ... colocamos na fila para visita-lo no seu devido momento
                l += 1 # atualizando o contador de largura
                largura[vizinho] = l
                pai[vizinho] = vertice
                nivel[vizinho] = nivel[vertice] + 1 # um vizinho estah sempre um nivel abaixo do pai
            # MOMENTO PARA VISITAR A ARESTA vertice -> vizinho
            # (descomente os codigos abaixo para ver a ordem em que as arestas sao visitadas e suas respectivas classificacoes)
            # print('%s -> %s:' % (str(vertice), str(vizinho)))
            if pai[vizinho] == vertice or pai[vertice] == vizinho:
                aresta[(vertice, vizinho)] = 'aresta de arvore'
                # print('aresta de arvore')
            elif nivel[vertice] == nivel[vizinho]:
                if pai[vertice] == pai[vizinho]:
                    aresta[(vertice, vizinho)] = 'aresta irma'
                    # print('aresta irma')
                else:
                    aresta[(vertice, vizinho)] = 'aresta primo'
                    # print('aresta primo')
            else:
                if nivel[vertice] < nivel[vizinho]:
                    aresta[(vertice, vizinho)] = 'aresta tia'
                    # print('aresta tia')
                else:
                    aresta[(vertice, vizinho)] = 'aresta sobrinha'
                    # print('aresta sobrinha')

    return largura, pai, aresta, nivel

def me_mate(grafo, nivel, inicio, fim, fila, a_nivel):
    if fim == inicio:
        fila.append(inicio)
        return fila

    for n in nivel:
        if nivel[n] == a_nivel:
            a_nivel