# TF-LFA
## Trabalho Final de LFA primeira etapa
A primeira etapa do trabalho consiste em implementar um simulador de Automatos com Pilha (pushdown automata), a linguagem escolhida foi Python e são utilizadas as bibliotecas Graphviz e Streamlit que podem ser instaladas pelo arquivo `requirements.txt`

## Executar
Para utilizar a ferramenta basta clonar o repositório na pasta desejada e utilizar o comando: `streamlit run stack.py`

## Utilização
Alguns campos serão preenchidos pelo usuário:

### Estado inicial:
Neste campo digitar o estado inicial
Exemplo: `Q0`

### Estados:
Neste campo digitar todos os estados separados por vírgula
Exemplo: `Q0, Q1, Q2`

### Estados de Aceitação:
Neste campo digitar todos os estados de aceitação ou finais separados por vírgula
Exemplo: `Q2`

### Alfabeto de Entrada:
Neste campo digitar todos os símbolos do alfabeto de entrada da fita separados por vírgula
Exemplo: `a, b, c`

### Alfabeto da Pilha:
Neste campo digitar todos os símbilos do alfabeto da pilha separados por vírgula

### Transições:
Neste campo digitar a tabela de transições sendo cada linha uma transição no formato `estado atual, símbolo de entrada, símbolo a ser desempilhado, estado atingido, símbolo a ser empilhado`
Exemplo: `Q0, a, &epsilon;`
