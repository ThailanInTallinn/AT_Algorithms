import random

def gerar_lista(tamanho, reverso=False, aleatorio=False, quase_ord=False):
    inicio, fim, pace = 0, tamanho, 1
    if aleatorio:
        lista = []
        for i in range(0, tamanho):
            lista.append(random.randint(1, tamanho))
        return lista

    if reverso:
        inicio = tamanho
        fim = 0
        pace = -1

    lista = [i for i in range(inicio, fim, pace)]  
    if(quase_ord):
        temp = lista[len(lista) - 1]
        temp2 = lista[0]
        lista[0] = temp 
        lista[len(lista) - 1] = temp2

    return lista
