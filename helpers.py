def read_csv(none):
    
    with open('/home/ucas/LFA/Files/simulation.csv', 'r') as f:
        for Quintupla in f:
            if Quintupla !=',':

    return Estados,Alfabeto,Pilha,Inicial,Finais

def create_pda_from_sextuple(sextuple):
    states, alphabet, stack_alphabet, transitions, start_state, accept_states = sextuple

    dot = graphviz.Digraph(format='png')

    for state in states:
        if state in accept_states:
            dot.node(state, shape='doublecircle')
        else:
            dot.node(state, shape='circle')

    for (from_state, symbol, stack_symbol), (to_state, push_symbols) in transitions.items():
        label = f"{symbol}, {stack_symbol} -> {push_symbols}"
        dot.edge(from_state, to_state, label)

    return dot