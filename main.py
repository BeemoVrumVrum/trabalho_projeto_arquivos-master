import random
from ArvoreAVL import ArvoreAVL
from ArvoreB import ArvoreB
from ArvoreRN import ArvoreRN

NUM_CONJUNTOS = 10
MAX_CHAVES = 10000

def main():
    # Gerar números aleatórios
    numeros = [[random.randint(1, 10000) for _ in range(MAX_CHAVES)] for _ in range(NUM_CONJUNTOS)]

    # AVL
    arvore_avl = ArvoreAVL()

    # Adição - AVL
    qtd_operacoes = [0]
    for i in range(NUM_CONJUNTOS):
        for j in range(MAX_CHAVES):
            arvore_avl.adicionarAVL(numeros[i][j], qtd_operacoes)
        print(f"Adição AVL #{i + 1} - {qtd_operacoes[0]}")

    # Remoção - AVL
    qtd_operacoes = [0]
    for i in range(NUM_CONJUNTOS):
        for j in range(MAX_CHAVES):
            qtd_operacoes += arvore_avl.removerAVL(numeros[i][j], qtd_operacoes)
        print(f"Remoção AVL #{i + 1} - {qtd_operacoes[0]}")

    # Árvore B (ordem 1)
    arvore_b1 = ArvoreB(1)
    qtd_operacoes = [0]
    for i in range(NUM_CONJUNTOS):
        for j in range(MAX_CHAVES):
            qtd_operacoes += arvore_b1.adicionaChaveB(numeros[i][j], qtd_operacoes)
        print(f"Adição B1 #{i + 1} - {qtd_operacoes[0]}")

    # Árvore B (ordem 5)
    arvore_b5 = ArvoreB(5)
    qtd_operacoes = [0]
    for i in range(NUM_CONJUNTOS):
        for j in range(MAX_CHAVES):
            qtd_operacoes += arvore_b5.adicionaChaveB(numeros[i][j], qtd_operacoes)
        print(f"Adição B5 #{i + 1} - {qtd_operacoes[0]}")

    # Árvore B (ordem 10)
    arvore_b10 = ArvoreB(10)
    qtd_operacoes = [0]
    for i in range(NUM_CONJUNTOS):
        for j in range(MAX_CHAVES):
            qtd_operacoes += arvore_b10.adicionaChaveB(numeros[i][j], qtd_operacoes)
        print(f"Adição B10 #{i + 1} - {qtd_operacoes[0]}")
    # Remoção - B (ordem 1)
    qtd_operacoes_b1 = [0]
    for conjunto in range(NUM_CONJUNTOS):
        for j in range(MAX_CHAVES):
            qtd_operacoes_b1[0] += arvore_b1.removeChaveB(numeros[conjunto][j], qtd_operacoes_b1)
        print(f"Remoção B1 #{conjunto + 1} - {qtd_operacoes_b1[0]}")

    # Remoção - B (ordem 5)
    qtd_operacoes_b5 = [0]
    for conjunto in range(NUM_CONJUNTOS):
        for j in range(MAX_CHAVES):
            qtd_operacoes_b5[0] += arvore_b5.removeChaveB(numeros[conjunto][j], qtd_operacoes_b5)
        print(f"Remoção B5 #{conjunto + 1} - {qtd_operacoes_b5[0]}")

    # Remoção - B (ordem 10)
    qtd_operacoes_b10 = [0]
    for conjunto in range(NUM_CONJUNTOS):
        for j in range(MAX_CHAVES):
            qtd_operacoes_b10[0] += arvore_b10.removeChaveB(numeros[conjunto][j], qtd_operacoes_b10)
        print(f"Remoção B10 #{conjunto + 1} - {qtd_operacoes_b10[0]}")

    # Soma total de operações de remoção
    total_operacoes_b = qtd_operacoes_b1[0] + qtd_operacoes_b5[0] + qtd_operacoes_b10[0]
    print(f"Remoção total B - {total_operacoes_b}")

    # Árvore RN
    arvore_rn = ArvoreRN()
    qtd_operacoes = [0]
    for i in range(NUM_CONJUNTOS):
        for j in range(MAX_CHAVES):
            qtd_operacoes += arvore_rn.adicionarRN(numeros[i][j], qtd_operacoes)
        print(f"Adição RN #{i + 1} - {qtd_operacoes[0]}")

    # Remoção - RN
    qtd_operacoes = [0]
    for i in range(NUM_CONJUNTOS):
        for j in range(MAX_CHAVES):
            qtd_operacoes += arvore_rn.removerRN(numeros[i][j], qtd_operacoes)
        print(f"Remoção RN #{i + 1} - {qtd_operacoes[0]}")

if __name__ == "__main__":
    main()