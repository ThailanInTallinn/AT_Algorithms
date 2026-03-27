def bubble_sort(lista):
    done = False
    while not done:
        done = True
        for i in range(0, len(lista) - 1):
            if(lista[i] > lista[i + 1]):
                done = False
                temp = lista[i + 1]
                lista[i + 1] = lista[i]
                lista[i] = temp
    return lista

def selection_sort(lista):
    new_lista = lista
    count = 0

    for i in range(len(new_lista)):
        min_index = i

        for j in range(i + 1, len(new_lista)):
            count += 1
            if(new_lista[j] < new_lista[min_index]):
                min_index = j

        temp = new_lista[i]
        new_lista[i] = new_lista[min_index]
        new_lista[min_index] = temp

    print(f"Numero de passos: {count}")
    return new_lista

def insertion_sort(lista):
    count = 0
    new_lista = lista
    count += 1
    for i in range(1, len(new_lista)):
        count += 2
        chave = new_lista[i]
        count += 1
        j = i - 1
        count += 1
    
        while(j >= 0) and (new_lista[j] > chave):
            count += 4
            new_lista[j + 1] = new_lista[j]
            count += 2
            j -= 1
            count += 1

        new_lista[j + 1] = chave
        count += 1
    count += 1
    print(f"Numero de passos, comparações e deslocamentos: {count}")
    return new_lista 

                
