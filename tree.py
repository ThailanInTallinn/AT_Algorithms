class Nodo:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None

class BST:
    def __init__(self):
        self.raiz = None
        
    def inserir(self, chave):
        if self.raiz == None:
            self.raiz = Nodo(chave)
        else:
            self._inserir_recursivo(self.raiz, chave)

    def _inserir_recursivo(self, no_atual, chave):
        if chave < no_atual.chave:
            if no_atual.esquerda == None:
                no_atual.esquerda = Nodo(chave)
            else:
                self._inserir_recursivo(no_atual.esquerda, chave)
        elif chave > no_atual.chave:
            if no_atual.direita == None:
                no_atual.direita = Nodo(chave)
            else:
                self._inserir_recursivo(no_atual.direita, chave)

    def buscar(self, chave):
        counter = 0
        return self._buscar_recursivo(self.raiz, chave)

    def _buscar_recursivo(self, no_atual, chave):
        counter += 1 
        if no_atual == None or no_atual == chave:
            return no_atual
        if chave < no_atual.chave:
            return self._buscar_recursivo(no_atual.esquerda, chave)
        return self._buscar_recursivo(no_atual.direita, chave)
    
    def em_ordem(self, no_atual, counter):
        counter += 1 
        if no_atual:
            self.em_ordem(no_atual.esquerda, counter)
            print(no_atual.valor, end=" ")
            self.em_ordem(no_atual.direita, counter)


    
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        self.altura = 1

class ArvoreAVL:
    def __init__(self):
        self.raiz = None
        self.counter = 0
        self.comparacoes = 0

    def _get_altura(self, no):
        if not no:
            return 0
        return no.altura

    def _get_fat_bal(self, no):
        if not no:
            return 0
        return self._get_altura(no.esquerda) - self._get_altura(no.direita)

    def _rotacao_direita(self, z):
        y = z.esquerda
        t = y.direita
        y.direita = z
        z.esquerda = t
        z.altura = 1 + max(self._get_altura(z.esquerda), self._get_altura(z.direita))
        y.altura = 1 + max(self._get_altura(y.esquerda), self._get_altura(y.direita))

        return y

    def _rotacao_esquerda(self, z):
        y = z.direita
        t = y.esquerda
        y.esquerda = z
        z.direita = t
        z.altura = 1 + max(self._get_altura(z.esquerda), self._get_altura(z.direita))
        y.altura = 1 + max(self._get_altura(y.esquerda), self._get_altura(y.direita))

        return y

    def inserir(self, raiz, valor):
        if not raiz:
            self.comparacoes += 1
            return No(valor)
        if valor < raiz.valor:
            self.comparacoes += 1
            raiz.esquerda = self.inserir(raiz.esquerda, valor)
        elif valor > raiz.valor:
            self.comparacoes += 1
            raiz.direita = self.inserir(raiz.direita, valor)
        else:
            return raiz

        raiz.altura = 1 + max(self._get_altura(raiz.esquerda), self._get_altura(raiz.direita))
        balanceamento = self._get_fat_bal(raiz)
        
        if balanceamento > 1 and valor < raiz.esquerda.valor:
            return self._rotacao_direita(raiz)

        if balanceamento < -1 and valor > raiz.direita.valor:
            return self._rotacao_esquerda(raiz)

        if balanceamento > 1 and valor > raiz.esquerda.valor:
            raiz.esquerda = self._rotacao_esquerda(raiz.esquerda)
            return self._rotacao_direita(raiz)
        
        if balanceamento < -1 and valor < raiz.direita.valor:
            raiz.direita = self._rotacao_direita(raiz.direita)
            return self._rotacao_esquerda(raiz)
        return raiz

    def em_ordem(self, no):
        self.counter += 1
        if not no:
            return []
        return (self.em_ordem(no.esquerda) +
                [no.valor] + 
                self.em_ordem(no.direita))

    def visualizar(self):
        return self.em_ordem(self.raiz)

    def exibir(self, no_atual=None, nivel=0):
        if no_atual == None and nivel == 0:
            no_atual = self.raiz
        if no_atual is not None:
            self.exibir(no_atual.direita, nivel+1)
            print('     '*nivel + f'-> {no_atual.valor}')
            self.exibir(no_atual.esquerda, nivel+1)
