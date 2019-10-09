def buscaProfundidade (grafo, inicio, fim, pilha):
    if inicio in pilha:
        print("Já na pilha: ")
        return pilha
    pilha.append(inicio)
    print("Pilha atual: " + str(pilha))
    if pilha[-1] == fim:
        print("Chegou no Fim!\n")
        return pilha
    vizinhos = grafo[inicio]
    print ("Vizinhos: " + str(vizinhos))
    for vizinho in vizinhos:
        print ("Estou no vizinho: " + vizinho)
        if vizinho not in pilha:
            pilha = buscaProfundidade(grafo, vizinho, fim, pilha)
            if pilha[-1] == fim:
                return pilha
        print("Vizinho na Pilha")
        print ("Pilha: " + str(pilha))
        if vizinho == vizinhos[-1]:
            pilha.pop()
            print("Pilha depois do pop: " + str(pilha))
            return pilha
    return pilha