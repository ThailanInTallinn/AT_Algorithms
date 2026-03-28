def bubble_sort(lista):
    count_bubble = 0
    copies_bubble = 0
    done = False
    while not done:
        done = True
        for i in range(0, len(lista) - 1):
            count_bubble += 1
            if(lista[i] > lista[i + 1]):
                done = False
                temp = lista[i + 1]
                lista[i + 1] = lista[i]
                lista[i] = temp
                copies_bubble += 3
    print(f"Numero de comparações bubble sort({len(lista)} itens): {count_bubble}")
    print(f"Numero de cópias bubble sort({len(lista)} itens): {copies_bubble}")
    return lista

def selection_sort(lista):
    new_lista = lista
    count_selection = 0
    copies_selection = 0

    for i in range(len(new_lista)):
        min_index = i

        for j in range(i + 1, len(new_lista)):
            count_selection += 1
            if(new_lista[j] < new_lista[min_index]):
                min_index = j

        temp = new_lista[i]
        new_lista[i] = new_lista[min_index]
        new_lista[min_index] = temp
        copies_selection += 3
 
    print(f"Numero de comparações selection sort({len(lista)} itens): {count_selection}")
    print(f"Numero de cópias selection sort({len(lista)} itens): {copies_selection}")
    return new_lista

def insertion_sort(lista):
    count_insertion = 0
    copies_insertion = 0
    new_lista = lista
    for i in range(1, len(new_lista)):
        chave = new_lista[i]
        count_insertion += 1
        j = i - 1
    
        while(j >= 0) and (new_lista[j] > chave):
            new_lista[j + 1] = new_lista[j]
            copies_insertion += 3
            j -= 1
            count_insertion += 1

        copies_insertion += 3
        new_lista[j + 1] = chave
    print(f"Numero de comparações insertion sort({len(lista)} itens): {count_insertion}")
    print(f"Numero de cópias insertion sort({len(lista)} itens): {copies_insertion}")
    return new_lista 

