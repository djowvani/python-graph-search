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

    # Populando o dicionário com as conexões
    dict_conexoes = {}
    listv = []
    list1 = []

    for x in linhas:
        if ',' in x:
            leitura = x.split(',')
            if leitura[0] not in listv:
                listv.append(leitura[0])
                list1.append(leitura[1])
                listv.append(leitura[1])
                list1.append(leitura[0])
            else:
                for i in range(len(listv)):
                    if listv[i] == leitura[0]:
                        list2 = []
                        for n in list1[i]:
                            list2.append(n)
                        list2.append(leitura[1])
                        list1[i] = list2
                if leitura[1] not in listv:
                    listv.append(leitura[1])
                    list1.append(leitura[0])
                else:
                    for i in range(len(listv)):
                        if listv[i] == leitura[1]:
                            list2 = []
                            for n in list1[i]:
                                list2.append(n)
                            list2.append(leitura[0])
                            list1[i] = list2

    print (listv)
    for i in range(len(listv)):
        dict_conexoes[listv[i]] = list1[i]
    print("\n=== LISTA DE VÉRTICES E SUAS CONEXÕES ===")
    print(dict_conexoes)
    print("======\n")

    print("INÍCIO: " + inicio + "\nFIM: " + fim + "\n")

    return dict_conexoes, inicio, fim

def lerArquivo2(arquivo):
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

    # Populando o dicionário com as conexões
    dict_conexoes = {}
    listv = []
    list1 = []

    for x in linhas:
        if ',' in x:
            leitura = x.split(',')
            if leitura[0] not in listv:
                listv.append(leitura[0])
                list_peso = []
                list_peso.append(leitura[1])
                list_peso.append(leitura[2].replace(';', ''))
                list1.append([list_peso])
                listv.append(leitura[1])
                list_peso = []
                list_peso.append(leitura[0])
                list_peso.append(leitura[2].replace(';', ''))
                list1.append([list_peso])
            else:
                for i in range(len(listv)):
                    if listv[i] == leitura[0]:
                        list_peso = []
                        list_peso.append(leitura[1])
                        list_peso.append(leitura[2].replace(';', ''))
                        list1[i].append(list_peso)
                if leitura[1] not in listv:
                    listv.append(leitura[1])
                    list_peso = []
                    list_peso.append(leitura[0])
                    list_peso.append(leitura[2].replace(';', ''))
                    list1.append([list_peso])
                else:
                    for i in range(len(listv)):
                        if listv[i] == leitura[1]:
                            list2 = []
                            for n in list1[i]:
                                list2.append(n)
                            list_peso = []
                            list_peso.append(leitura[0])
                            list_peso.append(leitura[2])
                            list2.append(list_peso)
                            list1[i] = list2

    print (listv)
    for i in range(len(listv)):
        dict_conexoes[listv[i]] = list1[i]

    print("\n=== LISTA DE VÉRTICES E SUAS CONEXÕES COM PESOS ===")
    print(dict_conexoes)
    print("======\n")

    print("INÍCIO: " + inicio + "\nFIM: " + fim + "\n")

    return dict_conexoes, inicio, fim