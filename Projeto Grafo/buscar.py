from buscaEmProfundidade import *
from buscaEmLargura import *
from buscaEmCustoUni import *
from leitorArquivo import *

def escolhaBusca(question):
    reply = str(input(question+"\nDigite: ")).lower().strip()
    if reply[0] == '1':
        return 1
    if reply[0] == '2':
        return 2
    if reply[0] == '3':
        return 3
    if reply == 'sair':
        return 'sair'
    else:
        return escolhaBusca("\nPor favor insira apenas 1, 2 ou 3.\n'Sair' para sair")

if __name__== "__main__" :
    print("=== INICIALIZANDO PROJETO ===")

    grafo, inicio, fim = lerArquivo("mapa_oficial.txt")

    menu = ''
    while menu is not 'sair':
        # Escolha do usuário
        escolha = escolhaBusca("Escolha o tipo de busca que deseja realizar:"+ "\n" +
                    "1 - Busca em Largura"+ "\n" +
                    "2 - Busca em Profundidade"+ "\n" +
                    "3 - Busca em Custo Uniforme")
        menu = escolha

        # ======================== BUSCA EM LARGURA ========================
        if escolha == 1:
            # Instanciando um Grafo ideal para se realizar buscas em largura
            grafo_largura = Grafo_L()

            # Populando o grafo com os vértices
            for x in grafo:
                grafo_largura.add_vertice(Vertice_L(x))

            # Populando o grafo com as arestas
            conexoes = grafo.values()
            for x in grafo:
                for y in conexoes:
                    grafo_largura.add_aresta(x, y)

            grafo_largura.buscaEmLargura(Vertice_L(fim))
            grafo_largura.print_mapa()

        # ======================== BUSCA EM PROFUNDIDADE ========================
        if escolha == 2:
            # Instanciando um Grafo ideal para se realizar buscas em profundidade
            grafo_profundidade = Grafo_P()

            # Populando o grafo com os vértices
            for x in vertices:
                grafo_profundidade.add_vertice(Vertice_P(x))

            # Populando o grafo com as arestas
            for x in linhas:
                if(x[1] != ";"):
                    grafo_profundidade.add_aresta(Vertice_P(x[0]), Vertice_P(x[2]))

            grafo_profundidade.buscaEmProfundidade(Vertice_P(vertices[0]))
            grafo_profundidade.print_mapa()

        # ======================== BUSCA EM CUSTO UNIFORME ========================
        if escolha == 3:
            # Instanciando um Grafo ideal para se realizar buscas em profundidade
            grafo_custo = Grafo_U()

            # Populando o grafo com os vértices, arestas e pesos respectivos
            for x in linhas:
                grafo_custo

            # Populando o grafo com as arestas
            for x in linhas:
                if(x[1] != ";"):
                    grafo_custo.add_aresta(x[0], x[2])
    