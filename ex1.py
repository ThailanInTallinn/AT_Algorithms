from listgenerator import gerar_lista
from singlylinkedlist import SinglyLinkedList



def linear_search(arr, target) -> tuple[int, str]:
    counter = 0
    if isinstance(arr, SinglyLinkedList):
        if(arr.inicio == None):
            return (0, "Lista encadeada não possui nodos")

        ptr = arr.inicio
        while ptr:
            counter += 1
            if(ptr.value == target):
                return (counter, f"Contagens busca linear em lista encadeada: {counter}")
            ptr = ptr.next
        return (-1, f"Contagens busca linear em lista encadeada para indice não localizado: {counter}")

    if(len(arr) == 0):
        return (-1, f"ERRO: array vazio. Contador: {counter}")
    if(len(arr) == 1):
        if(arr[0] == target):
            counter += 1
            return (0, f"Contagens busca linear em lista ordenada de tamanho {len(arr)}: {counter}")
        else:
            return (-1, f"Contagens busca linear em lista ordenada de tamanho {len(arr)} para indice não localizado: {counter}")


    for i in range(0, len(arr)):
        counter += 1
        if arr[i] == target:
            return (i, f"Contagens busca linear em lista ordenada de tamanho {len(arr)}: {counter}")
    return (-1, f"Contagens busca linear em lista ordenada de tamanho {len(arr)} para indice não localizado: {counter}")

def binary_search(sorted_arr, target) -> tuple[int, str]:
    sorted_asc = all(sorted_arr[i] <= sorted_arr[i + 1] for i in range(len(sorted_arr) - 1))
    sorted_desc = all(sorted_arr[i] >= sorted_arr[i + 1] for i in range(len(sorted_arr) - 1))
    counter = 0


    if(not(sorted_asc or sorted_desc)):
        return (-1,"Impossível realizar a busca binária pois o array passado como parâmetro não está ordenado em ordem crescente e nem em ordem decrescente.")
    if(len(sorted_arr) == 0):
        return (-1, f"ERRO: sorted_array vazio. Contador: {counter}")
    if(len(sorted_arr) == 1):
        if(sorted_arr[0] == target):
            counter += 1
            return (0, f"Contagens busca linear em lista ordenada de tamanho {len(sorted_arr)}: {counter}")
        else:
            return (-1, f"Contagens busca linear em lista ordenada de tamanho {len(sorted_arr)} para indice não localizado: {counter}")

    inicio = 0
    fim = len(sorted_arr) - 1

    if(sorted_asc):
        while inicio <= fim:
            meio = (inicio + fim) // 2
            counter += 1
            if(sorted_arr[meio] == target):
                return (meio, f"Contagens busca binária em lista ordenada(crescente) de tamanho {len(sorted_arr)}: {counter}" )
            if(sorted_arr[meio] > target):
                fim = meio - 1
            elif(sorted_arr[meio] < target):
                inicio = meio + 1
    else:
        while inicio <= fim:
            meio = (inicio + fim) // 2
            counter += 1
            if(sorted_arr[meio] == target):
                return (meio, f"Contagens busca binária em lista ordenada(decrescente) de tamanho {len(sorted_arr)}: {counter}" )
            if(sorted_arr[meio] > target):
                inicio = meio + 1
            elif(sorted_arr[meio] < target):
                fim = meio - 1
                
    return (-1, f"Contagens busca binária em lista ordenada de tamanho {len(sorted_arr)} para indice não localizado: {counter}") 


##### PARA EXECUCAO NO VIDEO
#print(gerar_lista(100))
#print(gerar_lista(100, True))
#print(gerar_lista(100, aleatorio=True))

#GERACAO DAS LISTAS
#listas ordenadas

lista_um_ord = gerar_lista(100)
lista_dois_ord = gerar_lista(1000)
lista_tres_ord = gerar_lista(10000)
lista_quatro_ord = gerar_lista(100000)
lista_cinco_ord = gerar_lista(1000000)

#listas reversas

lista_um_rev = gerar_lista(100, True)
lista_dois_rev = gerar_lista(1000, True)
lista_tres_rev = gerar_lista(10000, True)
lista_quatro_rev = gerar_lista(100000, True)
lista_cinco_rev = gerar_lista(1000000, True)

#listas aleatorias

lista_um_aleatoria = gerar_lista(100, aleatorio=True)
lista_dois_aleatoria = gerar_lista(1000, aleatorio=True)
lista_tres_aleatoria = gerar_lista(10000, aleatorio=True)
lista_quatro_aleatoria = gerar_lista(100000, aleatorio=True)
lista_cinco_aleatoria = gerar_lista(1000000, aleatorio=True)

#lista encadeada

lista_encadeada = SinglyLinkedList()
for i in range(0, 10000):
    lista_encadeada.add(i)

#######    Registro de contagens
demo_ordenadas = 0
demo_invertidas = 0
demo_aleatorias = 0
#listas ordenadas
if demo_ordenadas:
    result = linear_search(lista_um_ord, 90)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = linear_search(lista_um_ord, 190)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = binary_search(lista_um_ord, 90)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = binary_search(lista_um_ord, 190)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = linear_search(lista_dois_ord, 900)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = linear_search(lista_dois_ord, 1400)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = binary_search(lista_dois_ord, 900)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = binary_search(lista_dois_ord, 1400)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = linear_search(lista_tres_ord, 9600)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = linear_search(lista_tres_ord, 10001)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = binary_search(lista_tres_ord, 9600)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = binary_search(lista_tres_ord, 10001)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = linear_search(lista_quatro_ord, 99253)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = linear_search(lista_quatro_ord, 150000)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = binary_search(lista_quatro_ord, 99253)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = binary_search(lista_quatro_ord, 150000)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = linear_search(lista_cinco_ord, 999999)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = linear_search(lista_cinco_ord, 1200000)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = binary_search(lista_cinco_ord, 999999)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = binary_search(lista_cinco_ord, 1000001)
    print(result[1], '\n', f"Indice retornado: {result[0]}")



#listas invertidas
if demo_invertidas:
    result = linear_search(lista_um_rev, 90)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = linear_search(lista_um_rev, 190)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = binary_search(lista_um_rev, 90)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = binary_search(lista_um_rev, 190)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = linear_search(lista_dois_rev, 900)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = linear_search(lista_dois_rev, 1400)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = binary_search(lista_dois_rev, 900)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = binary_search(lista_dois_rev, 1400)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = linear_search(lista_tres_rev, 9600)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = linear_search(lista_tres_rev, 10001)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = binary_search(lista_tres_rev, 9600)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = binary_search(lista_tres_rev, 10001)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = linear_search(lista_quatro_rev, 99253)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = linear_search(lista_quatro_rev, 150000)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = binary_search(lista_quatro_rev, 99253)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = binary_search(lista_quatro_rev, 150000)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = linear_search(lista_cinco_rev, 999999)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = linear_search(lista_cinco_rev, 1200000)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = binary_search(lista_cinco_rev, 999999)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = binary_search(lista_cinco_rev, 1000001)
    print(result[1], '\n', f"Indice retornado: {result[0]}")
    
#listas aleatorias
    
if demo_aleatorias:
    result = linear_search(lista_um_aleatoria, 90)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = linear_search(lista_um_aleatoria, 190)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = binary_search(lista_um_aleatoria, 90)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = binary_search(lista_um_aleatoria, 190)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = linear_search(lista_dois_aleatoria, 900)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = linear_search(lista_dois_aleatoria, 1400)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = binary_search(lista_dois_aleatoria, 900)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = binary_search(lista_dois_aleatoria, 1400)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = linear_search(lista_tres_aleatoria, 9600)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = linear_search(lista_tres_aleatoria, 10001)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = binary_search(lista_tres_aleatoria, 9600)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = binary_search(lista_tres_aleatoria, 10001)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = linear_search(lista_quatro_aleatoria, 99253)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = linear_search(lista_quatro_aleatoria, 150000)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = binary_search(lista_quatro_aleatoria, 99253)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = binary_search(lista_quatro_aleatoria, 150000)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = linear_search(lista_cinco_aleatoria, 999999)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = linear_search(lista_cinco_aleatoria, 1200000)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = binary_search(lista_cinco_aleatoria, 999999)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

    result = binary_search(lista_cinco_aleatoria, 1000001)
    print(result[1], '\n', f"Indice retornado: {result[0]}")

result = linear_search(lista_encadeada, 104)
print(result[1], '\n', f"Nodo retornado: {result[0]}")

