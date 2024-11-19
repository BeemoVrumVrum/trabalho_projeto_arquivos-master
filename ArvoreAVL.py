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

    def fb(self, no, qtd_operacoes):
        self.incrementar_operacoes_ArvoreAVL(qtd_operacoes)
        esquerda = no.esquerda.alturaAVL if no.esquerda else 0
        direita = no.direita.alturaAVL if no.direita else 0
        return esquerda - direita

    def adicionarAVL(self, valor, qtd_operacoes):
        no = self.raiz

        while no:
            self.incrementar_operacoes_ArvoreAVL(qtd_operacoes)  
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


    def balancearAVL(self, no, qtd_operacoes):
        while no:
            self.incrementar_operacoes_ArvoreAVL(qtd_operacoes)
            no.alturaAVL = self.maxAVL(self.alturaAVL(no.esquerda), self.alturaAVL(no.direita)) + 1
            fator = self.fb(no, qtd_operacoes)

            if fator > 1:  
                # árvore mais pesada para esquerda
                # rotação para a direita
                if self.fb(no.esquerda, qtd_operacoes) > 0:
                    self.rsd(no, qtd_operacoes)  #rotação simples a direita, pois o FB do filho tem sinal igual
                else:
                    self.rdd(no, qtd_operacoes)  #rotação dupla a direita, pois o FB do filho tem sinal diferente
            elif fator < -1:  
                #árvore mais pesada para a direita
                #rotação para a esquerda
                if self.fb(no.direita, qtd_operacoes) < 0:
                    #rotação simples a esquerda, pois o FB do filho tem sinal igual
                    self.rse(no, qtd_operacoes)  
                else:
                    #rotação dupla a esquerda, pois o FB do filho tem sinal diferente
                    self.rde(no, qtd_operacoes)  

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
        no = self.localizarAVL(self.raiz, valor, qtd_operacoes)
        if not no:
            return

        self.incrementar_operacoes_ArvoreAVL(qtd_operacoes)
        pai = no.pai

        # não possui filhos
        if not no.esquerda and not no.direita:
            if not pai:
                self.raiz = None
            elif pai.esquerda == no:
                pai.esquerda = None
            else:
                pai.direita = None
        elif no.esquerda and no.direita:  # possui nó na esquerda e direita
            # procura a folha para adicionar a esquerda lá e balancear depois
            folha = no.direita
            while folha.esquerda:
                folha = folha.esquerda
            folha.esquerda = no.esquerda
            no.esquerda.pai = folha

            if not pai:
                self.raiz = no.direita
                self.raiz.pai = None
            elif pai.direita == no:
                pai.direita = no.direita
            else:
                pai.esquerda = no.direita
            no.direita.pai = pai

        else:  # possui nó apenas na esquerda ou apenas na direita
            filho = no.esquerda if no.esquerda else no.direita
            if not pai:
                self.raiz = filho
            elif no == pai.esquerda:
                pai.esquerda = filho
            else:
                pai.direita = filho
            filho.pai = pai

        self.balancearAVL(pai if pai else self.raiz, qtd_operacoes)
