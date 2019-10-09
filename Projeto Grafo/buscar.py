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
            
            largura, pai, aresta, nivel = buscaLargura(grafo, inicio)

            print (str(largura)+ "\n\n")
            print (str(pai)+ "\n\n")
            print (str(aresta)+ "\n\n")
            print (str(nivel)+ "\n\n")


        # ======================== BUSCA EM PROFUNDIDADE ========================
        if escolha == 2:
            # Instanciando um Grafo ideal para se realizar buscas em profundidade
            # grafo_profundidade = Grafo_P()

            # xo = None
            # yo = None
            # for x in grafo:
            #     for y in grafo[x]:
            #         xo = Vertice_L(x)
            #         yo = Vertice_L(y)
            #         xo.add_vizinho(y)
            #         yo.add_vizinho(x)
            #     grafo_profundidade.add_vertice(xo)
            #     grafo_profundidade.add_vertice(yo)
            #     grafo_profundidade.add_aresta(xo, yo)

            # grafo_profundidade.buscaEmLargura(Vertice_L(fim))

            fila = []
            fila = buscaProfundidade(grafo, inicio, fim, fila)

            print (str(fila))

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
    