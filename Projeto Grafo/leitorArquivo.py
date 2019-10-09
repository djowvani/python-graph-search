class dicionario(dict): 

	# __init__
	def __init__(self): 
		self = dict() 
		
	# Function to add key:value 
	def add(self, key, value): 
		self[key] = value

def lerArquivo(arquivo):
    # Leitura do arquivo de entrada
    with open(arquivo, "r") as f:
        linhas = f.readlines()

    # Removendo breaklines e gerando lista de vértices
    linhas = [x.strip() for x in linhas]

    # Pegando pontos de início e fim da busca
    fim = linhas.pop()
    fim = fim.replace(';', '')

    inicio = linhas.pop()
    inicio = inicio.replace(';', '')

    # Instanciando objeto de dicionário a ser utilizado
    dict_conexoes = dicionario() 

    # Populando o dicionário com as conexões
    todos_vertices = []
    for x in linhas:
        if ',' in x:
            leitura = x.split(',')

            if leitura[0] not in todos_vertices:
                todos_vertices.append(leitura[0])
            if leitura[1] not in todos_vertices:
                todos_vertices.append(leitura[1])
    
    todos_vertices.sort()

    comprimento = len(todos_vertices)
    i = 0
    for i in range(comprimento):
        dict_conexoes.add(todos_vertices[i], '')
        i += 1

    for x in linhas:
        if ',' in x:
            leitura = x.split(',')

            dict_conexoes.add(leitura[0], leitura[1])

    # vertice = leitura[0]
    # dict_conexoes.add(vertice, '')
    # vertice = leitura[1]
    # dict_conexoes.add(vertice, '')


# conexoes = leitura[1]
    # Populando o dicionário com as conexões 
    # for x in linhas:
    #     if ',' in x:
    #         leitura = x.split(',')
    #         vertice = leitura[0]
    #         conexao_peso = leitura[1] + "-" + leitura[2].replace(';','')
    #         dict_conexoes.add(vertice, conexao_peso)

    print("\n=== LISTA DE VÉRTICES E SUAS CONEXÕES ===")
    print(dict_conexoes)
    print("======\n")

    print("INÍCIO: " + inicio + "\nFIM: " + fim + "\n")

    return True