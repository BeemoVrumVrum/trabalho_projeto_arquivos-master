class NoB:
    def __init__(self, ordem):
        self.total = 0
        self.chaves = [None] * (2 * ordem + 1)
        self.filhos = [None] * (2 * ordem + 2)
        self.pai = None


class ArvoreB:
    def __init__(self, ordem):
        self.ordem = ordem
        self.raiz = self.cria_no_ArvoreB()

    def incrementar_operacoes(self, qtd_operacoes):
        qtd_operacoes[0] += 1  # Incrementa a contagem de operações

    def cria_no_ArvoreB(self):
        return NoB(self.ordem)

    def percorreArvoreB(self, no):
        if no is not None:
            for i in range(no.total):
                self.percorreArvoreB(no.filhos[i])  # visita o filho à esquerda
                print(no.chaves[i], end=" ")
            self.percorreArvoreB(no.filhos[no.total])  # visita o último filho (à direita)

    def pesquisa_binaria_ArvoreB(self, no, chave, qtd_operacoes):
        inicio, fim = 0, no.total - 1

        while inicio <= fim:
            qtd_operacoes[0] += 1
            meio = (inicio + fim) // 2
            if no.chaves[meio] == chave:
                return meio  # encontrou
            elif no.chaves[meio] > chave:
                fim = meio - 1
            else:
                inicio = meio + 1

        return inicio  # não encontrou

    def localiza_chaveArvoreB(self, chave, qtd_operacoes):
        no = self.raiz

        while no is not None:
            i = self.pesquisa_binaria_ArvoreB(no, chave, qtd_operacoes)
            if i < no.total and no.chaves[i] == chave:
                return True  # encontrou
            no = no.filhos[i]

        return False  # não encontrou

    def localiza_no_ArvoreB(self, chave, qtd_operacoes):
        no = self.raiz

        while no is not None:
            qtd_operacoes[0] += 1
            i = self.pesquisa_binaria_ArvoreB(no, chave, qtd_operacoes)
            if no.filhos[i] is None:
                return no  # encontrou nó
            no = no.filhos[i]

        return None  # não encontrou nenhum nó

    def adiciona_chave_no_ArvoreB(self, no, novo, chave, qtd_operacoes):
        i = self.pesquisa_binaria_ArvoreB(no, chave, qtd_operacoes)
        qtd_operacoes[0] += 1

        for j in range(no.total - 1, i - 1, -1):
            no.chaves[j + 1] = no.chaves[j]
            no.filhos[j + 2] = no.filhos[j + 1]

        no.chaves[i] = chave
        no.filhos[i + 1] = novo
        no.total += 1

    def transbordo_ArvoreB(self, no, qtd_operacoes):
        qtd_operacoes[0] += 1
        return no.total > self.ordem * 2

    def divide_no_ArvoreB(self, no, qtd_operacoes):
        meio = no.total // 2
        novo = self.cria_no_ArvoreB()
        novo.pai = no.pai
        qtd_operacoes[0] += 1

        for i in range(meio + 1, no.total):
            novo.filhos[novo.total] = no.filhos[i]
            novo.chaves[novo.total] = no.chaves[i]
            if novo.filhos[novo.total] is not None:
                novo.filhos[novo.total].pai = novo
            novo.total += 1

        novo.filhos[novo.total] = no.filhos[no.total]
        if novo.filhos[novo.total] is not None:
            novo.filhos[novo.total].pai = novo

        no.total = meio
        return novo

    def adiciona_chave_recursivo_ArvoreB(self, no, novo, chave, qtd_operacoes):
        qtd_operacoes[0] += 1
        self.adiciona_chave_no_ArvoreB(no, novo, chave, qtd_operacoes)

        if self.transbordo_ArvoreB(no, qtd_operacoes):
            promovido = no.chaves[self.ordem]
            novo = self.divide_no_ArvoreB(no, qtd_operacoes)

            if no.pai is None:
                qtd_operacoes[0] += 1
                pai = self.cria_no_ArvoreB()
                pai.filhos[0] = no
                self.adiciona_chave_no_ArvoreB(pai, novo, promovido, qtd_operacoes)
                no.pai = pai
                novo.pai = pai
                self.raiz = pai
            else:
                self.adiciona_chave_recursivo_ArvoreB(no.pai, novo, promovido, qtd_operacoes)

    def adicionaChaveB(self, chave, qtd_operacoes):
        no = self.localiza_no_ArvoreB(chave, qtd_operacoes)
        self.adiciona_chave_recursivo_ArvoreB(no, None, chave, qtd_operacoes)

    def removeChaveB(self, chave, qtd_operacoes):
        # Localiza o nó onde a chave pode estar
        no = self.localiza_no_ArvoreB(chave, qtd_operacoes)
        if no is None:
            return False  # Chave não encontrada
        
        i = self.pesquisa_binaria_ArvoreB(no, chave, qtd_operacoes)
        
        # Caso 1: A chave está em um nó folha
        if no.filhos[i] is None:
            return self.remove_da_folha(no, i, qtd_operacoes)
        
        # Caso 2: A chave está em um nó interno
        return self.remove_de_no_interno(no, i, qtd_operacoes)

    def remove_da_folha(self, no, i, qtd_operacoes):
        qtd_operacoes[0] += 1
        # Remover a chave diretamente
        for j in range(i, no.total - 1):
            no.chaves[j] = no.chaves[j + 1]
        no.chaves[no.total - 1] = None
        no.total -= 1
        
        # Verificar se o nó ficou com menos de ordem // 2 chaves
        if no != self.raiz and no.total < self.ordem // 2:
            return self.balancear_remocao(no, qtd_operacoes)
        
        return True

    def remove_de_no_interno(self, no, i, qtd_operacoes):
        qtd_operacoes[0] += 1
        # Substitui a chave com o sucessor ou predecessor
        if no.filhos[i + 1] is not None:
            # Substitui com o sucessor (menor chave à direita)
            sucessor = self.encontrar_sucessor(no.filhos[i + 1])
            no.chaves[i] = sucessor
            return self.removeChaveB(sucessor, qtd_operacoes)  # Remove a chave duplicada
        elif no.filhos[i] is not None:
            # Substitui com o predecessor (maior chave à esquerda)
            predecessor = self.encontrar_predecessor(no.filhos[i])
            no.chaves[i] = predecessor
            return self.removeChaveB(predecessor, qtd_operacoes)  # Remove a chave duplicada
        
    def encontrar_sucessor(self, no):
        # Encontra o sucessor (menor chave na subárvore à direita)
        while no.filhos[0] is not None:
            no = no.filhos[0]
        return no.chaves[0]
    
    def encontrar_predecessor(self, no):
        # Encontra o predecessor (maior chave na subárvore à esquerda)
        while no.filhos[no.total] is not None:
            no = no.filhos[no.total]
        return no.chaves[no.total - 1]

    def balancear_remocao(self, no, qtd_operacoes):
        qtd_operacoes[0] += 1
        # Verifica se o nó possui um irmão suficiente (com mais de ordem // 2 chaves)
        # Caso contrário, realiza uma fusão
        indice = self.localiza_no_ArvoreB(no.chaves[0], qtd_operacoes)
        if indice > 0 and no.pai.filhos[indice - 1].total > self.ordem // 2:
            # Emprestar uma chave do irmão esquerdo
            return self.empregar_chave_do_irmao_esquerdo(no, qtd_operacoes)
        elif indice < len(no.pai.filhos) - 1 and no.pai.filhos[indice + 1].total > self.ordem // 2:
            # Emprestar uma chave do irmão direito
            return self.empregar_chave_do_irmao_direito(no, qtd_operacoes)
        else:
            # Realiza fusão entre nós
            return self.fundir_no(no, qtd_operacoes)

    def empregar_chave_do_irmao_esquerdo(self, no, qtd_operacoes):
        qtd_operacoes[0] += 1
        # Empresta uma chave do irmão à esquerda
        indice_pai = self.pesquisa_binaria_ArvoreB(no.pai, no.chaves[0], qtd_operacoes)
        no_irmao_esquerdo = no.pai.filhos[indice_pai - 1]
        
        # Empresta chave
        chave_emprestada = no_irmao_esquerdo.chaves[no_irmao_esquerdo.total - 1]
        no.chaves.insert(0, chave_emprestada)  # Insere chave na posição correta
        no_irmao_esquerdo.chaves[no_irmao_esquerdo.total - 1] = None
        no_irmao_esquerdo.total -= 1
        
        return True
    
    def empregar_chave_do_irmao_direito(self, no, qtd_operacoes):
        qtd_operacoes[0] += 1
        # Empresta uma chave do irmão à direita
        indice_pai = self.pesquisa_binaria_ArvoreB(no.pai, no.chaves[0], qtd_operacoes)
        no_irmao_direito = no.pai.filhos[indice_pai + 1]
        
        # Empresta chave
        chave_emprestada = no_irmao_direito.chaves[0]
        no.chaves.append(chave_emprestada)  # Insere chave na posição correta
        no_irmao_direito.chaves[0] = None
        no_irmao_direito.total -= 1
        
        return True
    
    def fundir_no(self, no, qtd_operacoes):
        # Funde o nó com o irmão
        indice_pai = self.pesquisa_binaria_ArvoreB(no.pai, no.chaves[0], qtd_operacoes)
        no_irmao_direito = no.pai.filhos[indice_pai + 1] if indice_pai < len(no.pai.filhos) - 1 else None
        
        if no_irmao_direito is not None:
            # Funde com o irmão à direita
            for i in range(no_irmao_direito.total):
                no.chaves.append(no_irmao_direito.chaves[i])
            no_irmao_direito = None  # Remove o irmão após fusão
        return True