class Hashtable:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def _funcao_hash(self, chave):
        return chave % self.tamanho

    def inserir(self, chave, valor):
        index = self._funcao_hash(chave)
        bucket = self.tabela[index]

        for i, (chave_ex, _) in enumerate(bucket):
            if(chave_ex == chave):
                bucket[i] = (chave, valor)
                return 
            
        bucket.append((chave, valor))



    def buscar(self, chave):
        index = self._funcao_hash(chave)
        bucket = self.tabela[index]

        for chave_ex, valor in bucket:
            if(chave_ex == chave):
                return valor

        return None

    def remover(self, chave):
        index = self._funcao_hash(chave)
        bucket = self.tabela[index]

        for i, (chave_ex, valor) in enumerate(bucket):
            if chave_ex == chave:
                del bucket[i]

        return None

