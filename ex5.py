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

print("=" * 20, "FILA", "="*20) 
fila.exibir()

# Pilha como estrutura de dados auxiliar

pilha = Pilha(150)

for item in tree.traverse_em_ordem(tree.raiz):
    pilha.adicionar(item)
print("=" * 20, "PILHA", "="*20) 
pilha.exibir()

