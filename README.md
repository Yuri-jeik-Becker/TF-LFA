# TF-LFA
## Trabalho Final de LFA primeira etapa
Esta primeira etapa do trabalho consiste em implementar um simulador de Autômatos com Pilha (Pushdown Automaton)  
A linguagem escolhida foi Python e são utilizadas as bibliotecas Graphviz e Streamlit que podem ser instaladas pelo arquivo `requirements.txt`

## Executar
Para utilizar a ferramenta basta clonar o repositório na pasta desejada e utilizar o comando: 
```
streamlit run stack.py
```

## Utilização
Com a interface aberta será utilizado `ε` como palavra ou transição vazia  
Campos preenchidos pelo usuário:

### Estado inicial:
Neste campo digitar o estado inicial
Exemplo: `Q0`

### Estados:
Neste campo digitar todos os estados separados por vírgulas  
Exemplo: `Q0, Q1, Q2`

### Estados de Aceitação:
Neste campo digitar todos os estados de aceitação ou finais separados por vírgulas  
Exemplo: `Q2`

### Alfabeto de Entrada:
Neste campo digitar todos os símbolos do alfabeto de entrada da fita separados por vírgulas  
Exemplo: `a, b, c`

### Alfabeto da Pilha:
Neste campo digitar todos os símbilos do alfabeto da pilha separados por vírgulas  
Exemplo: `A, B, C`

### Transições:
Neste campo digitar a tabela de transições sendo cada linha uma transição e seus elementos separados por vírgulas no formato `estado atual, símbolo de entrada, símbolo a ser desempilhado, estado atingido, símbolo a ser empilhado`  
Exemplo: 
```
Q0, a, ε, Q1, A
Q1, b, A, Q2, ε
```

## Funções
Após preenchidos os campos o Autômato com Pilha pode ser gerado graficamente pressionando o botão: `Gerar Autômato`  
Fitas de entrada poderão ser testadas pressionando o botão: `Testar Fita`  

### Entrada a ser Testada:
Nesse campo digitar a fita de entrada apenas digitando os símbolos em sequência  
Exemplo: `aabbacbb`
