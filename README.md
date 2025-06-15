# Torre de Hanói Visual com Pilha Tipada em Python 🗼

Este projeto implementa uma solução visual e interativa para o clássico problema da Torre de Hanói, utilizando o paradigma de Programação Orientada a Objetos (POO) em Python. O código apresenta uma estrutura de pilha tipada, com tratamento robusto de exceções, e uma visualização detalhada do estado dos pinos a cada passo do algoritmo.

## Funcionalidades Abordadas
 * **Pilha Tipada Genérica:**
Implementação de uma classe Pilha que pode armazenar inteiros ou caracteres, com verificação de tipo e capacidade máxima.
 * **Tratamento de Exceções:**
Exceções personalizadas para pilha cheia, pilha vazia e tipo inválido, garantindo robustez e mensagens claras de erro.
 * **Visualização Dinâmica:**
Impressão gráfica do estado dos pinos (pilhas) a cada X movimentos, permitindo acompanhar visualmente o progresso da solução.
 * **Configuração Interativa:**
O usuário define:
   * O número de discos.
   * O intervalo de movimentos entre exibições do estado.
 * **Algoritmo Recursivo:**
Solução clássica do problema da Torre de Hanói, com contagem de movimentos e visualização intermediária.
 * **Operações Extras:**
    * Troca dos dois elementos do topo da pilha.
    * Consulta ao tamanho atual da pilha.
    * Impressão customizada da pilha.

## Como Começar
### Pré-requisitos
  * Faça o download do Python 3 mais recente no seu sistema.

### Execução
  1. Salve o código em um arquivo, por exemplo, torre_hanoi.py.
  2. No terminal, navegue até o diretório do arquivo.
  3. Execute o script com:
```
python torre_hanoi.py
```


## Como Usar
Ao rodar o programa, siga as instruções do console:
  1. **Digite o número de discos:**
Escolha quantos discos deseja usar (quanto maior, mais difícil e interessante!).
  2. **Digite a quantidade de movimentos entre exibições:**
Defina de quantos em quantos movimentos o estado dos pinos será exibido (pressione ENTER para usar o padrão 1).
  3. **Visualize e acompanhe:**
O programa mostrará o estado inicial e, a cada X movimentos, imprimirá a configuração dos pinos. Pressione ENTER para avançar cada etapa.

## Arquitetura do Projeto
### Classe Pilha:
Estrutura de dados para armazenar discos, com tipagem ('i' para inteiros, 'u' para caracteres), capacidade máxima e métodos para empilhar, desempilhar, trocar elementos, verificar estado e imprimir.
### Exceções Personalizadas:
PilhaCheiaErro; PilhaVaziaErro; TipoErro
### Função de Visualização:
Função que imprime graficamente os pinos e discos, facilitando o acompanhamento visual do algoritmo.
### Função Recursiva da Torre de Hanói:
Implementação clássica, adaptada para atualizar a visualização e contar movimentos.
### Função Main:
Gerencia a entrada do usuário, inicializa as pilhas e executa o algoritmo.


## Exemplo de Uso
```
Digite o número de discos: 3
Digite a quantidade de movimentos entre exibições (padrão 1): 2

Posição Inicial: 0 passos

      #|#         |         |   
     ##|##        |         |   
    ###|###       |         |   
___________   ___________   ___________   

Posição: 2 passos

      #|#         |         |   
     ##|##        |         |   
    ###|###       |         |   
___________   ___________   ___________   
Pressione [ENTER] para continuar...
```

## Observações
  * O código pode ser facilmente adaptado para outros tipos de dados na pilha, bastando alterar o tipo no construtor.
  * A visualização é textual e funciona em qualquer terminal.
  * Excelente recurso didático para entender recursão, pilhas e o problema da Torre de Hanói.

