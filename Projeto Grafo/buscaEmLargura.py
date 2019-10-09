def busca_de_Largura (grafo, inicio, fim, fila):
    for i in inicio:
        if i in fila:
            print("ja na fila")
            continue
        fila.append(i)
        print("Fila atual: " + str(fila))

        if fila[-1] == fim:
            print("chegou no fim")
            return fila

        vizinhos = grafo[i]
        print ("vizinhos: " + str(vizinhos))

        c = 0
        for vizinho in vizinhos:
            print ("No vizinho " + vizinho)
            if vizinho not in fila:
                c += 1
            if vizinho == fim:
                fila.append(vizinho)
                return fila

        if c == 0:
            fila.pop()
            return fila
        if len(inicio) > 1:
            fila.pop()
    vizs = []
    for vizinho in vizinhos:
        viz = grafo[vizinho]
        for v in viz:
            vizs.append(v)
    fila.append(vizinho)
    fila = busca_de_Largura(grafo, vizs, fim, fila)
    print(fila)
    if fila[-1] == fim:
        return fila
    return fila