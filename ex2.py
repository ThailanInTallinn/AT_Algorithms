from listgenerator import gerar_lista
from sort import *
from tree import *


# listas com 1000 itens
print()
print("============================== 1000 itens ===========")
print()
print("##### lista ordenada #####")
lista_ord = gerar_lista(1000)
bubble_sort(lista_ord)
insertion_sort(lista_ord)
selection_sort(lista_ord)
tree = ArvoreAVL()
for i in range(0, len(lista_ord)):
    tree.raiz = tree.inserir(tree.raiz, lista_ord[i])

contagem = tree.visualizar()[1]
print(f"Chamadas à função de atravessamento: {tree.counter}")
print(f"Numero de comparações: {tree.comparacoes}")


print("##### lista reversa #####")
lista_rev = gerar_lista(1000, reverso=True)
bubble_sort(lista_rev)
insertion_sort(lista_rev)
selection_sort(lista_rev)
tree_2 = ArvoreAVL()
for i in range(0, len(lista_rev)):
    tree_2.raiz = tree_2.inserir(tree_2.raiz, lista_rev[i])

contagem = tree_2.visualizar()[1]
print(f"Chamadas à função de atravessamento: {tree_2.counter}")
print(f"Numero de comparações: {tree_2.comparacoes}")

print("##### lista aleatória #####")
lista_random = gerar_lista(1000, aleatorio=True)
bubble_sort(lista_random)
insertion_sort(lista_random)
selection_sort(lista_random)
tree_3 = ArvoreAVL()
for i in range(0, len(lista_random)):
    tree_3.raiz = tree_3.inserir(tree_3.raiz, lista_random[i])

contagem = tree_3.visualizar()[1]
print(f"Chamadas à função de atravessamento: {tree_3.counter}")
print(f"Numero de comparações: {tree_3.comparacoes}")

print("##### lista quase ordenada #####")
lista_quase_ord = gerar_lista(1000, quase_ord=True)
bubble_sort(lista_quase_ord)
insertion_sort(lista_quase_ord)
selection_sort(lista_quase_ord)
tree_4 = ArvoreAVL()
for i in range(0, len(lista_quase_ord)):
    tree_4.raiz = tree_4.inserir(tree_4.raiz, lista_quase_ord[i])

contagem = tree_4.visualizar()[1]
print(f"Chamadas à função de atravessamento: {tree_4.counter}")
print(f"Numero de comparações: {tree_4.comparacoes}")

# lista com 10000 itens
print()
print("============================== 10000 itens ===========")
print()
print("##### lista ordenada #####")

lista_ord = gerar_lista(10000)
bubble_sort(lista_ord)
insertion_sort(lista_ord)
selection_sort(lista_ord)
tree_5 = ArvoreAVL()
for i in range(0, len(lista_ord)):
    tree_5.raiz = tree_5.inserir(tree_5.raiz, lista_ord[i])

contagem = tree_5.visualizar()[1]
print(f"Chamadas à função de atravessamento: {tree_5.counter}")
print(f"Numero de comparações: {tree_5.comparacoes}")

print("##### lista reversa #####")

lista_rev = gerar_lista(10000, reverso=True)
bubble_sort(lista_rev)
insertion_sort(lista_rev)
selection_sort(lista_rev)
tree_6 = ArvoreAVL()
for i in range(0, len(lista_rev)):
    tree_6.raiz = tree_6.inserir(tree_6.raiz, lista_rev[i])

contagem = tree_6.visualizar()[1]
print(f"Chamadas à função de atravessamento: {tree_6.counter}")
print(f"Numero de comparações: {tree_6.comparacoes}")

print("##### lista aleatória #####")

lista_random = gerar_lista(10000, aleatorio=True)
bubble_sort(lista_random)
insertion_sort(lista_random)
selection_sort(lista_random)
tree_7 = ArvoreAVL()
for i in range(0, len(lista_random)):
    tree_7.raiz = tree_7.inserir(tree_7.raiz, lista_random[i])

contagem = tree_7.visualizar()[1]
print(f"Chamadas à função de atravessamento: {tree_7.counter}")
print(f"Numero de comparações: {tree_7.comparacoes}")

print("##### lista quase ordenada #####")

lista_quase_ord = gerar_lista(10000, quase_ord=True)
bubble_sort(lista_quase_ord)
insertion_sort(lista_quase_ord)
selection_sort(lista_quase_ord)
tree_8 = ArvoreAVL()
for i in range(0, len(lista_quase_ord)):
    tree_8.raiz = tree_8.inserir(tree_8.raiz, lista_quase_ord[i])

contagem = tree_8.visualizar()[1]
print(f"Chamadas à função de atravessamento: {tree_8.counter}")
print(f"Numero de comparações: {tree_8.comparacoes}")

# lista com 25000 itens
print()
print("============================== 25000 itens ===========")
print()
print("##### lista ordenada #####")

lista_ord = gerar_lista(25000)

"""
bubble_sort(lista_ord)
insertion_sort(lista_ord)
selection_sort(lista_ord)
"""
tree_9 = ArvoreAVL()
for i in range(0, len(lista_ord)):
    tree_9.raiz = tree_9.inserir(tree_9.raiz, lista_ord[i])

contagem = tree_9.visualizar()[1]
print(f"Chamadas à função de atravessamento: {tree_9.counter}")
print(f"Numero de comparações: {tree_9.comparacoes}")

print("##### lista reversa #####")

lista_rev = gerar_lista(25000, reverso=True)
"""
bubble_sort(lista_rev)
insertion_sort(lista_rev)
selection_sort(lista_rev)
"""
tree_10 = ArvoreAVL()
for i in range(0, len(lista_rev)):
    tree_10.raiz = tree_10.inserir(tree_10.raiz, lista_rev[i])

contagem = tree_10.visualizar()[1]
print(f"Chamadas à função de atravessamento: {tree_10.counter}")
print(f"Numero de comparações: {tree_10.comparacoes}")


print("##### lista aleatória #####")

lista_random = gerar_lista(25000, aleatorio=True)
"""
bubble_sort(lista_random)
insertion_sort(lista_random)
selection_sort(lista_random)
"""
tree_11 = ArvoreAVL()
for i in range(0, len(lista_random)):
    tree_11.raiz = tree_11.inserir(tree_11.raiz, lista_random[i])

contagem = tree_11.visualizar()[1]
print(f"Chamadas à função de atravessamento: {tree_11.counter}")
print(f"Numero de comparações: {tree_11.comparacoes}")

print("##### lista quase ordenada #####")

lista_quase_ord = gerar_lista(25000, quase_ord=True)
"""
bubble_sort(lista_quase_ord)
insertion_sort(lista_quase_ord)
selection_sort(lista_quase_ord)
"""
tree_12 = ArvoreAVL()
for i in range(0, len(lista_quase_ord)):
    tree_12.raiz = tree_12.inserir(tree_12.raiz, lista_quase_ord[i])

contagem = tree_12.visualizar()[1]
print(f"Chamadas à função de atravessamento: {tree_12.counter}")
print(f"Numero de comparações: {tree_12.comparacoes}")

# lista com 50000 itens
print()
print("============================== 50000 itens ===========")
print()
print("##### lista ordenada #####")

lista_ord = gerar_lista(50000)
"""
bubble_sort(lista_ord)
insertion_sort(lista_ord)
selection_sort(lista_ord)
"""
tree_13 = ArvoreAVL()
for i in range(0, len(lista_ord)):
    tree_13.raiz = tree_13.inserir(tree_13.raiz, lista_ord[i])

contagem = tree_13.visualizar()[1]
print(f"Chamadas à função de atravessamento: {tree_13.counter}")
print(f"Numero de comparações: {tree_13.comparacoes}")


print("##### lista reversa #####")

lista_rev = gerar_lista(50000, reverso=True)
"""
bubble_sort(lista_rev)
insertion_sort(lista_rev)
selection_sort(lista_rev)
"""
tree_14 = ArvoreAVL()
for i in range(0, len(lista_rev)):
    tree_14.raiz = tree_14.inserir(tree_14.raiz, lista_rev[i])

contagem = tree_14.visualizar()[1]
print(f"Chamadas à função de atravessamento: {tree_14.counter}")
print(f"Numero de comparações: {tree_14.comparacoes}")


print("##### lista aleatória #####")

lista_random = gerar_lista(50000, aleatorio=True)
"""
bubble_sort(lista_random)
insertion_sort(lista_random)
selection_sort(lista_random)
"""
tree_15 = ArvoreAVL()
for i in range(0, len(lista_random)):
    tree_15.raiz = tree_15.inserir(tree_15.raiz, lista_random[i])

contagem = tree_15.visualizar()[1]
print(f"Chamadas à função de atravessamento: {tree_15.counter}")
print(f"Numero de comparações: {tree_15.comparacoes}")

print("##### lista quase ordenada #####")

lista_quase_ord = gerar_lista(50000, quase_ord=True)
"""
bubble_sort(lista_quase_ord)
insertion_sort(lista_quase_ord)
selection_sort(lista_quase_ord)
"""
tree_16 = ArvoreAVL()
for i in range(0, len(lista_quase_ord)):
    tree_16.raiz = tree_16.inserir(tree_16.raiz, lista_quase_ord[i])

contagem = tree_16.visualizar()[1]
print(f"Chamadas à função de atravessamento: {tree_16.counter}")
print(f"Numero de comparações: {tree_16.comparacoes}")


# lista com 100000 itens
print()
print("============================== 100000 itens ===========")
print()
print("##### lista ordenada #####")

lista_ord = gerar_lista(100000)
"""
bubble_sort(lista_ord)
insertion_sort(lista_ord)
selection_sort(lista_ord)
"""
tree_17 = ArvoreAVL()
for i in range(0, len(lista_ord)):
    tree_17.raiz = tree_17.inserir(tree_17.raiz, lista_ord[i])

contagem = tree_17.visualizar()[1]
print(f"Chamadas à função de atravessamento: {tree_17.counter}")
print(f"Numero de comparações: {tree_17.comparacoes}")

print("##### lista reversa #####")

lista_rev = gerar_lista(100000, reverso=True)
"""
bubble_sort(lista_rev)
insertion_sort(lista_rev)
selection_sort(lista_rev)
"""
tree_18 = ArvoreAVL()
for i in range(0, len(lista_rev)):
    tree_18.raiz = tree_18.inserir(tree_18.raiz, lista_rev[i])

contagem = tree_18.visualizar()[1]
print(f"Chamadas à função de atravessamento: {tree_18.counter}")
print(f"Numero de comparações: {tree_18.comparacoes}")

print("##### lista aleatória #####")
lista_random = gerar_lista(100000, aleatorio=True)
"""
bubble_sort(lista_random)
insertion_sort(lista_random)
selection_sort(lista_random)
"""
tree_19 = ArvoreAVL()
for i in range(0, len(lista_random)):
    tree_19.raiz = tree_19.inserir(tree_19.raiz, lista_random[i])

contagem = tree_19.visualizar()[1]
print(f"Chamadas à função de atravessamento: {tree_19.counter}")
print(f"Numero de comparações: {tree_19.comparacoes}")

print("##### lista quase ordenada #####")

lista_quase_ord = gerar_lista(100000, quase_ord=True)
"""
bubble_sort(lista_quase_ord)
insertion_sort(lista_quase_ord)
selection_sort(lista_quase_ord)
"""
tree_20 = ArvoreAVL()
for i in range(0, len(lista_quase_ord)):
    tree_20.raiz = tree_20.inserir(tree_20.raiz, lista_quase_ord[i])

contagem = tree_20.visualizar()[1]
print(f"Chamadas à função de atravessamento: {tree_20.counter}")
print(f"Numero de comparações: {tree_20.comparacoes}")

lista_rev = gerar_lista(25000, reverso=True)
bubble_sort(lista_rev)
insertion_sort(lista_rev)
selection_sort(lista_rev)


