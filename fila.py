class Fila:
    def __init__(self, tamanho_maximo):
        self.lista = []
        self.contador_insercao = 0
        self.contador_remocao = 0
        self.tamanho_max = tamanho_maximo
        self.pointer = 0

    def adicionar(self, item):
        if(self.pointer >= self.tamanho_max):
            self.contador_insercao += 1
            print("Fila já atingiu seu tamanho máximo.")
            #print(f"Numero de passos para adição malssucedida: {self.contador_insercao}")
            return -1
        
        self.lista[self.pointer] = item
        self.pointer += 1
        self.contador_insercao += 1
        #print(f"Numero de passos para adicao feita com sucesso: {self.contador_insercao}")
        return 1

    def remover(self, lista):
        if(lista[0] == "\0"):
            self.contador_remocao += 1
            print("Fila vazia.")
            print(f"Numero de passos para remoçao malssucedida: {self.contador_remocao}")
            return -1

        self.contador_remocao += 1
        for i in range(1, self.tamanho_max - 1):
            self.lista[i - 1] = self.lista[i]
            self.lista[i] = "\0"
            self.contador_remocao += 2
            
        print(f"Numero de passos para remoção feita com sucesso: {self.contador_remocao}")
        return 1

    def preencher(self):
        for i in range(0, self.tamanho_max):
            self.lista.append("\0")

    def exibir(self):
        for item in self.lista:
            if item != '\0':
                print(item, end=" ")
        print()
