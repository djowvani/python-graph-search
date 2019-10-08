# for each hashmap

mapa = open('Busca_Largura/logica.txt','r')
caminhos = mapa.read()
lista = caminhos.replace(';', '')
lista_top = lista.split('\n')


grafo = open('Busca_Largura/grafo.txt','w+')
i = 0
while i < len(caminhos):
    grafo.write(caminhos[i])
    i += 1
grafo.close()