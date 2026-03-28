import time
import random
from listgenerator import gerar_lista
from sort import *

def remover_duplicados(arr, tamanho):
    return list(set(arr))

def k_smallest_a(arr, k):
    lista = bubble_sort(arr)
    return lista[:k]

def particionar(arr, esquerda, direita):
    pivo_idx = random.randint(esquerda, direita)
    arr[direita], arr[pivo_idx] = arr[pivo_idx], arr[direita]
    
    pivo = arr[direita]
    i = esquerda
    for j in range(esquerda, direita):
        if arr[j] <= pivo:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[direita] = arr[direita], arr[i]
    return i

def quickselect(arr, esquerda, direita, k):
    if esquerda <= direita:
        pivo_index = particionar(arr, esquerda, direita)
        if pivo_index == k:
            return arr[:k]
        elif pivo_index > k:
            return quickselect(arr, esquerda, pivo_index - 1, k)
        else:
            return quickselect(arr, pivo_index + 1, direita, k)

def k_smallest_b(arr, k):
    if k <= 0: return []
    if k >= len(arr): return sorted(arr) 
    
    copia_array = arr.copy()
    esquerda, direita = 0, len(copia_array) - 1
    target = k - 1  
    
    while esquerda <= direita:
        pivo_index = particionar(copia_array, esquerda, direita)
        
        if pivo_index == target:
            break
        elif pivo_index > target:
            direita = pivo_index - 1
        else:
            esquerda = pivo_index + 1
            
    return copia_array[:k]


tamanhos = [1000, 10000, 25000, 50000, 100000]
resultados = {}

for n in tamanhos:
    
    lista_original = gerar_lista(n, aleatorio=True)
    
    start = time.time()
    lista_limpa = remover_duplicados(lista_original, n)
    tempo_limpeza = time.time() - start
    
    # 10% da lista
    k = n // 10 
    
    # sort
    start = time.time()
    res_a = k_smallest_a(lista_limpa, k)
    tempo_a = time.time() - start
    
    # quickselct
    start = time.time()
    res_b = k_smallest_b(lista_limpa, k)
    tempo_b = time.time() - start
    
    resultados[n] = (tempo_limpeza, tempo_a, tempo_b)

print(f"{'Tamanho da lista':<10} | {'Limpeza':<12} | {'Ordenado':<12} | {'Quickselect':<12}")
for n, tempos in resultados.items():
    print(f"{n} | {tempos[0]}      | {tempos[1]}      | {tempos[2]}")
