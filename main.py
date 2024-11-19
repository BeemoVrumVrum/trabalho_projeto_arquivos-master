import random
from ArvoreAVL import ArvoreAVL
from ArvoreB import ArvoreB
from ArvoreRN import ArvoreRN

NUM_CONJUNTOS = 10
MAX_CHAVES = 10000

def main():
    # gera números aleatórios
    numeros = [[random.randint(1, 10000) for _ in range(MAX_CHAVES)] for _ in range(NUM_CONJUNTOS)]

    # AVL
    arvore_avl = ArvoreAVL()

    # adição - AVL
    print('----- Adição AVL -----')
    for i in range(NUM_CONJUNTOS):
        qtd_operacoes = [0]
        for j in range(MAX_CHAVES):
            arvore_avl.adicionarAVL(numeros[i][j], qtd_operacoes)
        print(qtd_operacoes[0])

    # árvore B (ordem 1)
    arvore_b1 = ArvoreB(1)
    print('----- Adição B1 -----')
    for i in range(NUM_CONJUNTOS):
        qtd_operacoes = [0]
        for j in range(MAX_CHAVES):
            arvore_b1.adicionaChaveB(numeros[i][j], qtd_operacoes)
        print(qtd_operacoes[0])

    # adição - árvore B (ordem 5)
    arvore_b5 = ArvoreB(5)
    print('----- Adição B5 -----')
    for i in range(NUM_CONJUNTOS):
        qtd_operacoes = [0]
        for j in range(MAX_CHAVES):
            arvore_b5.adicionaChaveB(numeros[i][j], qtd_operacoes)
        print(qtd_operacoes[0])

    # adição - árvore B (ordem 10)
    arvore_b10 = ArvoreB(10)
    print('----- Adição B10 -----')
    for i in range(NUM_CONJUNTOS):
        qtd_operacoes = [0]
        for j in range(MAX_CHAVES):
            arvore_b10.adicionaChaveB(numeros[i][j], qtd_operacoes)
        print(qtd_operacoes[0])

    # adição - árvore RN
    arvore_rn = ArvoreRN()
    print('----- Adição RN -----')
    for i in range(NUM_CONJUNTOS):
        qtd_operacoes = [0]
        for j in range(MAX_CHAVES):
            arvore_rn.adicionarRN(numeros[i][j], qtd_operacoes)
        print(qtd_operacoes[0])

    # remoção - AVL
    print('----- Remoção AVL -----')
    for i in range(NUM_CONJUNTOS):
        qtd_operacoes = [0]
        for j in range(MAX_CHAVES):
            arvore_avl.removerAVL(numeros[i][j], qtd_operacoes)
        print(qtd_operacoes[0])
    
    # remoção - árvore B (ordem 1)
    print('----- Remoção B1 -----')
    for conjunto in range(NUM_CONJUNTOS):
        qtd_operacoes_b1 = [0]
        for j in range(MAX_CHAVES):
            arvore_b1.removeChaveB(numeros[conjunto][j], qtd_operacoes_b1)
        print(qtd_operacoes_b1[0])

    # remoção - árvore B (ordem 5)
    print('----- Remoção B5 -----')
    for conjunto in range(NUM_CONJUNTOS):
        qtd_operacoes_b5 = [0]
        for j in range(MAX_CHAVES):
            arvore_b5.removeChaveB(numeros[conjunto][j], qtd_operacoes_b5)
        print(qtd_operacoes_b5)

    # Remoção - árvore B (ordem 10)
    print('----- Remoção B10 -----')
    for conjunto in range(NUM_CONJUNTOS):
        qtd_operacoes_b10 = [0]
        for j in range(MAX_CHAVES):
            arvore_b10.removeChaveB(numeros[conjunto][j], qtd_operacoes_b10)
        print(qtd_operacoes_b10)

    # remoção - RN
    print('----- Remoção RN -----')
    for i in range(NUM_CONJUNTOS):
        qtd_operacoes = [0]
        for j in range(MAX_CHAVES):
            arvore_rn.removerRN(numeros[i][j], qtd_operacoes)
        print(qtd_operacoes)

if __name__ == "__main__":
    main()
