from singlylinkedlist import *
from listgenerator import *

lista = SinglyLinkedList()
for item in gerar_lista(100):
    lista.insert_last(item)

lista.insert_first(532)
"""
curr_node = lista.inicio
while curr_node:
    print(f"Index: {curr_node.index} | Valor: {curr_node.value}")
    curr_node = curr_node.next
"""
"""
result = lista.search(96)   
if(result.value):
    print(f"Valor {result.value} encontrado no index {result.index}")
    """

lista.delete(37)
curr_node = lista.inicio
while curr_node:
    print(f"Index: {curr_node.index} | Valor: {curr_node.value}")
    curr_node = curr_node.next
