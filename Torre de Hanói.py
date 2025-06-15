from array import array

# Exceções e classe Pilha conforme definidas anteriormente
class PilhaCheiaErro(Exception):
    pass

class PilhaVaziaErro(Exception):
    pass

class TipoErro(Exception):
    pass

class Pilha:
    def __init__(self, tipo: str, capacidade: int):
        if tipo not in ('i', 'u'):
            raise TipoErro("Tipo deve ser 'i' para inteiro ou 'u' para caractere")
        self._tipo = tipo
        self._capacidade = capacidade
        self._dados = array(tipo)
    
    def empilha(self, dado):
        if self.pilha_esta_cheia():
            raise PilhaCheiaErro("A pilha está cheia")
        if self._tipo == 'i' and not isinstance(dado, int):
            raise TipoErro("Dado deve ser inteiro")
        if self._tipo == 'u' and not (isinstance(dado, str) and len(dado) == 1):
            raise TipoErro("Dado deve ser caractere único")
        self._dados.append(dado)
    
    def desempilha(self):
        if self.pilha_esta_vazia():
            raise PilhaVaziaErro("A pilha está vazia")
        return self._dados.pop()
    
    def pilha_esta_vazia(self):
        return len(self._dados) == 0
    
    def pilha_esta_cheia(self):
        return len(self._dados) == self._capacidade
    
    def troca(self):
        if len(self._dados) < 2:
            raise PilhaVaziaErro("Não há elementos suficientes para trocar")
        self._dados[-1], self._dados[-2] = self._dados[-2], self._dados[-1]
    
    def tamanho(self):
        return len(self._dados)
    
    def __str__(self):
        # Mostra os discos do fundo (esquerda) para o topo (direita)
        return "[ " + " ".join(str(d) for d in reversed(self._dados)) + " ]"


def imprimir_torre_visual(pinos, movimentos, n):
    print(f"\nPosição: {movimentos} passos\n")

    altura = n
    largura_max = n + 2  # largura máxima do disco para alinhamento

    for nivel in range(altura - 1, -1, -1):
        linha = ""
        for pino in pinos:
            # Se o disco existe nessa altura (índice 0 é fundo, topo é último)
            if pino.tamanho() > nivel:
                disco = pino._dados[nivel]
                tam = disco
                lado = "#" * tam
                espaço = " " * (largura_max - tam)
                linha += espaço + lado + "|" + lado + espaço + "   "
            else:
                linha += " " * largura_max + "|" + " " * largura_max + "   "
        print(linha)

    # Imprime a base dos pinos
    base = ""
    for _ in pinos:
        base += "_" * (largura_max * 2 + 1) + "   "
    print(base)


def torre_de_hanoi(n, origem, destino, auxiliar, pinos, contador, m):
    if n == 1:
        disco = pinos[origem].desempilha()
        pinos[destino].empilha(disco)
        contador[0] += 1

        if contador[0] % m == 0:
            imprimir_torre_visual(pinos, contador[0], len(pinos[0]._dados) + pinos[1].tamanho() + pinos[2].tamanho())
            input("Pressione [ENTER] para continuar...")
    else:
        torre_de_hanoi(n-1, origem, auxiliar, destino, pinos, contador, m)
        torre_de_hanoi(1, origem, destino, auxiliar, pinos, contador, m)
        torre_de_hanoi(n-1, auxiliar, destino, origem, pinos, contador, m)


def main():
    n = int(input("Digite o número de discos: "))
    m_str = input("Digite a quantidade de movimentos entre exibições (padrão 1): ")
    m = int(m_str) if m_str.strip() else 1

    # Inicializa os pinos
    pino_inicial = Pilha('i', n)
    pino_intermediario = Pilha('i', n)
    pino_destino = Pilha('i', n)

    # Empilha discos no pino inicial do maior (n) no fundo para o menor (1) no topo
    for disco in range(n, 0, -1):
        pino_inicial.empilha(disco)

    pinos = [pino_inicial, pino_intermediario, pino_destino]

    print("\nPosição Inicial: 0 passos")
    imprimir_torre_visual(pinos, 0, n)

    contador = [0]  # contador mutável

    torre_de_hanoi(n, 0, 2, 1, pinos, contador, m)

    print(f"\nPosição Final : {contador[0]} passos")
    imprimir_torre_visual(pinos, contador[0], n)


if __name__ == "__main__":
    main()
