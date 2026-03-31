class Pilha:

    def __init__(self, tamanho_max):
        self.tamanho_max = tamanho_max
        self.lista = []

    def adicionar(self, item):
        counter  = 0
        tip = self.get_top()
        counter += 1
        if(tip == self.tamanho_max):
            counter += 1
            print("Tamanho máximo atingido.")
            #print(f"Numero de passos para adição malssucedida: {counter}")
            return -1

        self.lista.append(item) 
        counter += 1
        #print(f"Numero de passos para adição feita com sucesso: {counter}")
        return 1

    def remover(self):
        counter = 0
        tip = self.get_top()
        if(tip == 0):
            counter += 1
            print("Pilha vazia.")
            #print(f"Numero de passos para remoção malssucedida: {counter}")
            return -1

        removed = self.lista.pop()
        counter += 1
        #print(f"Numero de passos para remoção feita com sucesso: {counter}")
        return removed

    def get_top(self):
        return len(self.lista)

    def exibir(self):
        tip = self.get_top()
        if(tip == 0):
            print("Pilha vazia.")
            return -1

        for i in range(tip - 1, -1, -1):
            print(self.lista[i], end=" ")
        print()
