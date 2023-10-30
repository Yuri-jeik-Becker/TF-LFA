import graphviz
def create_pda_from_sextuple(sextuple, input_string):
    states, alphabet, stack_alphabet, transitions, start_state, accept_states = sextuple

    dot = graphviz.Digraph(format='png')

    for state in states:
        if state in accept_states:
            dot.node(state, shape='doublecircle')
        else:
            dot.node(state, shape='circle')

    current_state = start_state
    stack = []

    for symbol in input_string:
        if (current_state, symbol, stack[-1]) in transitions:
            to_state, push_symbols = transitions[(current_state, symbol, stack[-1])]
            label = f"{symbol}, {stack[-1]} -> {push_symbols}"
            dot.edge(current_state, to_state, label)
            current_state = to_state

            if push_symbols != 'e':
                stack.pop()
                stack.extend(list(push_symbols))

    return dot



def get_user_input_sextuple():
    states = input("Informe os estados separados por vírgula (ex: q0,q1,q2): ").split(',')
    alphabet = input("Informe o alfabeto separado por vírgula (ex: a,b,c): ").split(',')
    stack_alphabet = input("Informe o alfabeto da pilha separado por vírgula (ex: A,B,C): ").split(',')
    start_state = input("Informe o estado inicial: ")
    accept_states = input("Informe os estados de aceitação separados por vírgula (ex: q2,q3): ").split(',')

    transitions = {}
    while True:
        transition = input("Informe uma transição (de, símbolo, pilha): ").split(',')
        if len(transition) == 1 and transition[0] == 'fim':
            break
        to_state = input("Informe o estado de destino: ")
        push_symbols = input("Informe os símbolos a serem empilhados (e para vazio): ")
        transitions[(transition[0], transition[1], transition[2])] = (to_state, push_symbols)

    return states, alphabet, stack_alphabet, transitions, start_state, accept_states

def main():
    sextuple = get_user_input_sextuple()
    #while -> testar varias fitas
    input_string = input("Digite a entrada: ")
    
    pda = create_pda_from_sextuple(sextuple, input_string)
    pda.render('automaton')

    if pda.load_input(input_string):
        print("A entrada é aceita.")
    else:
        print("A entrada é rejeitada.")


if __name__ == "__main__":
    main()
