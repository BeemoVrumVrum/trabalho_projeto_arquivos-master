class NoAVL:
    def __init__(self, valor):
        self.pai = None
        self.esquerda = None
        self.direita = None
        self.valor = valor
        self.alturaAVL = 1


class ArvoreAVL:
    def __init__(self):
        self.raiz = None

    def incrementar_operacoes_ArvoreAVL(self, qtd):
        qtd[0] += 1

    @staticmethod
    def maxAVL(a, b):
        return a if a > b else b

    def vaziaAVL(self):
        return self.raiz is None

    def alturaAVL(self, no):
        return no.alturaAVL if no else 0

    def fator_balanceamento_ArvoreAVL(self, no, qtd_operacoes):
        self.incrementar_operacoes_ArvoreAVL(qtd_operacoes)
        esquerda = no.esquerda.alturaAVL if no.esquerda else 0
        direita = no.direita.alturaAVL if no.direita else 0
        return esquerda - direita

    def adicionarAVL(self, valor, qtd_operacoes):
        no = self.raiz

        while no:
            self.incrementar_operacoes_ArvoreAVL(qtd_operacoes)  # Passa e modifica qtd_operacoes diretamente
            if valor > no.valor:
                if no.direita:
                    no = no.direita
                else:
                    break
            else:
                if no.esquerda:
                    no = no.esquerda
                else:
                    break

        novo = NoAVL(valor)
        novo.pai = no

        if not no:
            self.raiz = novo
        else:
            if valor > no.valor:
                no.direita = novo
            else:
                no.esquerda = novo
            self.balancearAVL(no, qtd_operacoes)

        return qtd_operacoes  # Retorna a lista com qtd_operacoes


    def balancearAVL(self, no, qtd_operacoes):
        while no:
            self.incrementar_operacoes_ArvoreAVL(qtd_operacoes)
            no.alturaAVL = self.maxAVL(self.alturaAVL(no.esquerda), self.alturaAVL(no.direita)) + 1
            fator = self.fator_balanceamento_ArvoreAVL(no, qtd_operacoes)

            if fator > 1:  # Mais pesado à esquerda
                if self.fator_balanceamento_ArvoreAVL(no.esquerda, qtd_operacoes) > 0:
                    self.rsd(no, qtd_operacoes)  # Rotação simples direita
                else:
                    self.rdd(no, qtd_operacoes)  # Rotação dupla direita
            elif fator < -1:  # Mais pesado à direita
                if self.fator_balanceamento_ArvoreAVL(no.direita, qtd_operacoes) < 0:
                    self.rse(no, qtd_operacoes)  # Rotação simples esquerda
                else:
                    self.rde(no, qtd_operacoes)  # Rotação dupla esquerda

            no = no.pai

    def localizarAVL(self, no, valor, qtd_operacoes):
        while no:
            self.incrementar_operacoes_ArvoreAVL(qtd_operacoes)
            if no.valor == valor:
                return no
            no = no.esquerda if valor < no.valor else no.direita
        return None

    def percorrerAVL(self, no, callback):
        if no:
            self.percorrerAVL(no.esquerda, callback)
            callback(no.valor)
            self.percorrerAVL(no.direita, callback)

    def rse(self, no, qtd_operacoes):
        self.incrementar_operacoes_ArvoreAVL(qtd_operacoes)
        direita = no.direita
        no.direita = direita.esquerda
        if direita.esquerda:
            direita.esquerda.pai = no
        direita.pai = no.pai

        if not no.pai:
            self.raiz = direita
        elif no == no.pai.esquerda:
            no.pai.esquerda = direita
        else:
            no.pai.direita = direita

        direita.esquerda = no
        no.pai = direita

        no.alturaAVL = self.maxAVL(self.alturaAVL(no.esquerda), self.alturaAVL(no.direita)) + 1
        direita.alturaAVL = self.maxAVL(self.alturaAVL(direita.esquerda), self.alturaAVL(direita.direita)) + 1
        return direita

    def rsd(self, no, qtd_operacoes):
        self.incrementar_operacoes_ArvoreAVL(qtd_operacoes)
        esquerda = no.esquerda
        no.esquerda = esquerda.direita
        if esquerda.direita:
            esquerda.direita.pai = no
        esquerda.pai = no.pai

        if not no.pai:
            self.raiz = esquerda
        elif no == no.pai.esquerda:
            no.pai.esquerda = esquerda
        else:
            no.pai.direita = esquerda

        esquerda.direita = no
        no.pai = esquerda

        no.alturaAVL = self.maxAVL(self.alturaAVL(no.esquerda), self.alturaAVL(no.direita)) + 1
        esquerda.alturaAVL = self.maxAVL(self.alturaAVL(esquerda.esquerda), self.alturaAVL(esquerda.direita)) + 1
        return esquerda

    def rde(self, no, qtd_operacoes):
        no.direita = self.rsd(no.direita, qtd_operacoes)
        return self.rse(no, qtd_operacoes)

    def rdd(self, no, qtd_operacoes):
        no.esquerda = self.rse(no.esquerda, qtd_operacoes)
        return self.rsd(no, qtd_operacoes)

    def removerAVL(self, valor, qtd_operacoes):
        # Localiza o nó com o valor a ser removido
        no = self.localizarAVL(self.raiz, valor, qtd_operacoes)
        if not no:
            return qtd_operacoes  # Se o nó não for encontrado, retorna a lista de operações

        self.incrementar_operacoes_ArvoreAVL(qtd_operacoes)
        pai = no.pai

        if not no.esquerda and not no.direita:  # Caso 1: Nó sem filhos
            if not pai:  # Caso especial: raiz
                self.raiz = None
            elif pai.esquerda == no:
                pai.esquerda = None
            else:
                pai.direita = None
        elif no.esquerda and no.direita:  # Caso 2: Nó com dois filhos
            # Encontra o sucessor (o menor nó à direita)
            folha = no.direita
            while folha.esquerda:
                folha = folha.esquerda
            folha.esquerda = no.esquerda
            no.esquerda.pai = folha

            # Ajuste dos ponteiros do pai
            if not pai:
                self.raiz = no.direita
                self.raiz.pai = None
            elif pai.direita == no:
                pai.direita = no.direita
            else:
                pai.esquerda = no.direita
            no.direita.pai = pai

        else:  # Caso 3: Nó com apenas um filho
            filho = no.esquerda if no.esquerda else no.direita
            if not pai:
                self.raiz = filho
            elif no == pai.esquerda:
                pai.esquerda = filho
            else:
                pai.direita = filho
            filho.pai = pai

        # Balanceamento após remoção
        self.balancearAVL(pai if pai else self.raiz, qtd_operacoes)

        return qtd_operacoes  # Retorna o número atualizado de operações
