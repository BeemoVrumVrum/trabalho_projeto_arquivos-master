class Cor:
    VERMELHO = "vermelho"
    PRETO = "preto"

class NoRN:
    def __init__(self, pai=None, esquerda=None, direita=None, cor=Cor.VERMELHO, valor=0):
        self.pai = pai
        self.esquerda = esquerda
        self.direita = direita
        self.cor = cor
        self.valor = valor

class ArvoreRN:
    def __init__(self):
        self.nulo = NoRN(cor=Cor.PRETO)
        self.raiz = self.nulo

    @staticmethod
    def incrementar_operacoes(self, qtd_operacoes):
        qtd_operacoes[0] += 1

    def vaziaRN(self):
        return self.raiz == self.nulo

    def cria_noRN(self, pai, valor):
        no = NoRN(pai=pai, esquerda=self.nulo, direita=self.nulo, valor=valor)
        return no

    def adicionar_noRN(self, no, valor, qtd_operacoes):
        qtd_operacoes[0] += 1
        if valor > no.valor:
            if no.direita == self.nulo:
                no.direita = self.cria_noRN(no, valor)
                no.direita.cor = Cor.VERMELHO
                return no.direita
            else:
                return self.adicionar_noRN(no.direita, valor, qtd_operacoes)
        else:
            if no.esquerda == self.nulo:
                no.esquerda = self.cria_noRN(no, valor)
                no.esquerda.cor = Cor.VERMELHO
                return no.esquerda
            else:
                return self.adicionar_noRN(no.esquerda, valor, qtd_operacoes)

    def adicionarRN(self, valor, qtd_operacoes):
        if self.vaziaRN():
            self.raiz = self.cria_noRN(self.nulo, valor)
            self.raiz.cor = Cor.PRETO
            return self.raiz
        else:
            no = self.adicionar_noRN(self.raiz, valor, qtd_operacoes)
            self.balancearRN(no, qtd_operacoes)
            return no

    def localizarRN(self, valor):
        if not self.vaziaRN():
            no = self.raiz
            while no != self.nulo:
                if no.valor == valor:
                    return no
                no = no.esquerda if valor < no.valor else no.direita
        return None

    def balancearRN(self, no, qtd_operacoes):
        while no.pai.cor == Cor.VERMELHO:
            qtd_operacoes[0] += 1
            if no.pai == no.pai.pai.esquerda:
                tio = no.pai.pai.direita
                if tio.cor == Cor.VERMELHO:
                    tio.cor = Cor.PRETO
                    no.pai.cor = Cor.PRETO
                    no.pai.pai.cor = Cor.VERMELHO
                    no = no.pai.pai
                else:
                    if no == no.pai.direita:
                        no = no.pai
                        self.rotacionar_esquerda(no, qtd_operacoes)
                    no.pai.cor = Cor.PRETO
                    no.pai.pai.cor = Cor.VERMELHO
                    self.rotacionar_direita(no.pai.pai, qtd_operacoes)
            else:
                tio = no.pai.pai.esquerda
                if tio.cor == Cor.VERMELHO:
                    tio.cor = Cor.PRETO
                    no.pai.cor = Cor.PRETO
                    no.pai.pai.cor = Cor.VERMELHO
                    no = no.pai.pai
                else:
                    if no == no.pai.esquerda:
                        no = no.pai
                        self.rotacionar_direita(no, qtd_operacoes)
                    no.pai.cor = Cor.PRETO
                    no.pai.pai.cor = Cor.VERMELHO
                    self.rotacionar_esquerda(no.pai.pai, qtd_operacoes)
        self.raiz.cor = Cor.PRETO

    def rotacionar_esquerda(self, no, qtd_operacoes):
        qtd_operacoes[0] += 1
        direita = no.direita
        no.direita = direita.esquerda
        if direita.esquerda != self.nulo:
            direita.esquerda.pai = no
        direita.pai = no.pai
        if no.pai == self.nulo:
            self.raiz = direita
        elif no == no.pai.esquerda:
            no.pai.esquerda = direita
        else:
            no.pai.direita = direita
        direita.esquerda = no
        no.pai = direita

    def rotacionar_direita(self, no, qtd_operacoes):
        qtd_operacoes[0] += 1
        esquerda = no.esquerda
        no.esquerda = esquerda.direita
        if esquerda.direita != self.nulo:
            esquerda.direita.pai = no
        esquerda.pai = no.pai
        if no.pai == self.nulo:
            self.raiz = esquerda
        elif no == no.pai.direita:
            no.pai.direita = esquerda
        else:
            no.pai.esquerda = esquerda
        esquerda.direita = no
        no.pai = esquerda

    def percorrer_pre_order(self, no, callback):
        if no != self.nulo:
            callback(no.valor)
            self.percorrer_pre_order(no.esquerda, callback)
            self.percorrer_pre_order(no.direita, callback)

    def percorrer_pos_order(self, no, callback):
        if no != self.nulo:
            self.percorrer_pos_order(no.esquerda, callback)
            self.percorrer_pos_order(no.direita, callback)
            callback(no.valor)

    def percorrer_in_order(self, no, callback):
        if no != self.nulo:
            self.percorrer_in_order(no.esquerda, callback)
            callback(no.valor)
            self.percorrer_in_order(no.direita, callback)
    def removerRN(self, valor, qtd_operacoes):
        no = self.localizarRN(valor)
        if no is None:
            return None  # O nó não existe na árvore

        if no.esquerda != self.nulo and no.direita != self.nulo:
            # Caso o nó tenha dois filhos, substituímos o nó pelo seu sucessor (o menor nó da subárvore direita)
            sucessor = self.encontrar_sucessor(no)
            no.valor = sucessor.valor
            no = sucessor  # Agora removemos o sucessor
        # Agora, o nó tem no máximo um filho
        filho = no.esquerda if no.esquerda != self.nulo else no.direita

        if filho != self.nulo:
            # Substituímos o nó a ser removido pelo seu filho
            filho.pai = no.pai
            if no.pai == self.nulo:
                self.raiz = filho
            elif no == no.pai.esquerda:
                no.pai.esquerda = filho
            else:
                no.pai.direita = filho
            if no.cor == Cor.PRETO:
                # Se o nó removido era preto, precisamos corrigir a árvore
                self.balancear_remocao(filho, qtd_operacoes)
        else:
            # O nó é uma folha, basta removê-lo
            if no.pai == self.nulo:
                self.raiz = self.nulo
            elif no == no.pai.esquerda:
                no.pai.esquerda = self.nulo
            else:
                no.pai.direita = self.nulo
            if no.cor == Cor.PRETO:
                self.balancear_remocao(no, qtd_operacoes)

        qtd_operacoes[0] += 1
        return no

    def encontrar_sucessor(self, no):
        # Encontra o sucessor (o nó com o menor valor na subárvore direita)
        no = no.direita
        while no.esquerda != self.nulo:
            no = no.esquerda
        return no

    def balancear_remocao(self, no, qtd_operacoes):
        while no != self.raiz and no.cor == Cor.PRETO:
            qtd_operacoes[0] += 1
            if no == no.pai.esquerda:
                irmão = no.pai.direita
                if irmão.cor == Cor.VERMELHO:
                    irmão.cor = Cor.PRETO
                    no.pai.cor = Cor.VERMELHO
                    self.rotacionar_esquerda(no.pai, qtd_operacoes)
                    irmão = no.pai.direita
                if irmão.esquerda.cor == Cor.PRETO and irmão.direita.cor == Cor.PRETO:
                    irmão.cor = Cor.VERMELHO
                    no = no.pai
                else:
                    if irmão.direita.cor == Cor.PRETO:
                        irmão.esquerda.cor = Cor.PRETO
                        irmão.cor = Cor.VERMELHO
                        self.rotacionar_direita(irmão, qtd_operacoes)
                        irmão = no.pai.direita
                    irmão.cor = no.pai.cor
                    no.pai.cor = Cor.PRETO
                    irmão.direita.cor = Cor.PRETO
                    self.rotacionar_esquerda(no.pai, qtd_operacoes)
                    no = self.raiz
            else:
                irmão = no.pai.esquerda
                if irmão.cor == Cor.VERMELHO:
                    irmão.cor = Cor.PRETO
                    no.pai.cor = Cor.VERMELHO
                    self.rotacionar_direita(no.pai, qtd_operacoes)
                    irmão = no.pai.esquerda
                if irmão.esquerda.cor == Cor.PRETO and irmão.direita.cor == Cor.PRETO:
                    irmão.cor = Cor.VERMELHO
                    no = no.pai
                else:
                    if irmão.esquerda.cor == Cor.PRETO:
                        irmão.direita.cor = Cor.PRETO
                        irmão.cor = Cor.VERMELHO
                        self.rotacionar_esquerda(irmão, qtd_operacoes)
                        irmão = no.pai.esquerda
                    irmão.cor = no.pai.cor
                    no.pai.cor = Cor.PRETO
                    irmão.esquerda.cor = Cor.PRETO
                    self.rotacionar_direita(no.pai, qtd_operacoes)
                    no = self.raiz
        no.cor = Cor.PRETO
