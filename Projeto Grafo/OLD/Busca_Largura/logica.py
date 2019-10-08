mapa = open('Busca_Largura/mapa_largura.txt','r')
caminhos = mapa.read()
lista = caminhos.replace(';', ',')
lista_ok = lista.split(',')

print(lista_ok)

i = 0
j = 0
percorrido[]

while i < len(lista_ok):
    atual = lista_ok[i]
    while j < len(lista_ok):
        if (lista_corrida[i] = atual)
            break
        else:
            percorrido.write(atual)
        j += 1
    i += 1