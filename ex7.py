from deque import *

def testar_deque():
    print("--- Iniciando Bateria de Testes do Deque ---", end="\n\n")
    d = Deque()

    # Teste de estado inicial
    assert d.is_empty() == True, "Erro: Deque deveria estar vazio no inicio."
    print("Teste 1 Passou: Deque inicializado vazio corretamente.")

    # Sequencia de insercoes alternadas
    d.insert_left(10)
    d.insert_right(20)
    d.insert_left(5)
    d.insert_right(30)

    # Verificando se as pontas estao corretas sem remover
    assert d.peek_left() == 5, "Erro: O elemento da esquerda deveria ser 5."
    assert d.peek_right() == 30, "Erro: O elemento da direita deveria ser 30."
    print("Teste 2 Passou: Insercoes alternadas nas pontas funcionaram.")

    # Sequencia de remocoes alternadas
    removido_esq = d.remove_left()
    assert removido_esq == 5, f"Erro: Esperado 5, removeu {removido_esq}"
    
    removido_dir = d.remove_right()
    assert removido_dir == 30, f"Erro: Esperado 30, removeu {removido_dir}"
    
    assert d.peek_left() == 10, "Erro: Apos remocoes, a nova ponta esquerda deveria ser 10."
    assert d.peek_right() == 20, "Erro: Apos remocoes, a nova ponta direita deveria ser 20."
    print("Teste 3 Passou: Primeira rodada de remocoes alternadas funcionou perfeitamente.")

    # Esvaziando o Deque cruzando as pontas
    removido_cruzado_esq = d.remove_right()
    assert removido_cruzado_esq == 20, f"Erro: Esperado 20, removeu {removido_cruzado_esq}"

    removido_cruzado_dir = d.remove_left()
    assert removido_cruzado_dir == 10, f"Erro: Esperado 10, removeu {removido_cruzado_dir}"

    assert d.is_empty() == True, "Erro: O Deque deveria estar vazio apos remover tudo."
    print("Teste 4 Passou: Esvaziamento completo cruzando as pontas foi um sucesso.")

    # Comportamento com a estrutura vazia
    print("\nTestando comportamento de erro esperado (Deque vazio):")
    d.remove_left()   
    d.remove_right()  
    
if __name__ == "__main__":
    testar_deque()