from listgenerator import gerar_lista

def bubble_sort(lista):
    done = False

    while not done:
        done = True
        for i in range(0, len(lista) - 1):
            if(lista[i] > lista[i + 1]):
                done = False
                temp = lista[i + 1]
                lista[i + 1] =  lista[i]
                lista[i] = temp

    return lista

