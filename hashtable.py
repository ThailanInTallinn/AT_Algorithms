class HashTableChained:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def _funcao_hash(self, chave):
        return chave % self.tamanho

    def put(self, chave, valor):
        index = self._funcao_hash(chave)
        bucket = self.tabela[index]
        counter = 0

        for i, (chave_ex, _) in enumerate(bucket):
            counter += 1
            if(chave_ex == chave):
                bucket[i] = (chave, valor)
                return 
        print(f"Número de comparações para inserção: {counter}") 
        bucket.append((chave, valor))



    def get(self, chave):
        counter = 0
        index = self._funcao_hash(chave)
        bucket = self.tabela[index]

        for chave_ex, valor in bucket:
            counter += 1
            if(chave_ex == chave):
                return valor
        print(f"Número de comparações para busca: {counter}")
        return None

    def delete(self, chave):
        index = self._funcao_hash(chave)
        bucket = self.tabela[index]
        counter = 0

        for i, (chave_ex, valor) in enumerate(bucket):
            counter += 1
            if chave_ex == chave:
                del bucket[i]

        print(f"Número de comparações para deleção: {counter}")
        return None

    def __len__(self):
        count = 0
        for item in self.tabela:
            count += len(item)

        return count
