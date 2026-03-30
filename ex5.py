from tree import *
from listgenerator import *
from pilha import *
from fila import *

tree = BST()
lista_original = gerar_lista(100, aleatorio=True)
for i in lista_original:
    tree.inserir(i)

# Fila como estrutura de dados auxiliar
fila = Fila(150)
fila.preencher()
for item in tree.traverse_em_ordem(tree.raiz):
    fila.adicionar(item)

fila.exibir()

# Pilha como estrutura de dados auxiliar
