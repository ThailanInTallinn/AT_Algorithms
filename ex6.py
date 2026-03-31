from singlylinkedlist import *
from listgenerator import *

lista = SinglyLinkedList()
for item in gerar_lista(100):
    lista.insert_last(item)

print("Inserção na primeira posição da lista com insert_first(valor 532)")
lista.insert_first(532)
print(f"Primeiro nó da lista: {lista.inicio.value}", end="\n\n")

print("Busca por valor com search() - Bem-sucedida")
result = lista.search(96)   
if(result.value):
    print(f"Valor {result.value} encontrado no index {result.index}", end="\n\n")
print("Busca por valor com search() - Malssucedida")
result = lista.search(800)

print("Deleção básica por valor com delete(valor 37) - Bem-sucedida", end="\n\n")

lista.delete(37)
lista.exibir()

print("Deleção básica por valor com delete() - Malssucedida")

lista.delete(800)

print("Inserção com insert_at(index 1000, valor 1841) - Bem-sucedida")
lista.insert_at(1000, 1841)
print(f"Sendo o index inserido maior do que o index da ponta da lista, a inserção é feita na ponta da lista: {lista.tail.value}", end="\n\n")

print("Inserção com insert_at(index -1, valor 1000) - Malssucedida")
lista.insert_at(-1, 1000)

print("Deleção com delete_at(index 40) - Bem-sucedida(Não haverá saída de texto)")
lista.delete_at(40)
print("Deleção com delete_at(index -1) - Malssucedida")
lista.delete_at(-1)

print(f"Saída do método __len__() - Comprimento da lista: {lista.__len__()}", end="\n\n")

print(f"Saída do método __str__() - Malssucedido")
lista2 = SinglyLinkedList()
lista2.__str__()

print(f"Saída do método __str__() - Bem-sucedido")
lista.__str__()


"""
curr_node = lista.inicio
while curr_node:
    print(f"Index: {curr_node.index} | Valor: {curr_node.value}")
    curr_node = curr_node.next
"""
