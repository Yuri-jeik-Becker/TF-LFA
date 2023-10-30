import streamlit as st
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
        key = (current_state, symbol, stack[-1] if stack else 'ε')  # Create a key for the transition
        if key in transitions:
            to_state, push_symbols = transitions[key]
            label = f"{symbol}, {stack[-1] if stack else 'ε'} -> {push_symbols}"
            dot.edge(current_state, to_state, label=label)  # Use label to specify transition
            current_state = to_state

            if push_symbols != 'ε':
                if stack:
                    stack.pop()
                stack.extend(list(push_symbols))

    st.image(dot.pipe(format='svg').decode('utf-8'))

    if current_state in accept_states and not stack:
        st.write("A entrada é aceita.")
    else:
        st.write("A entrada é rejeitada.")

def get_user_input_sextuple():
    st.subheader("Informe os estados separados por vírgula (ex: q0,q1,q2):")
    states = st.text_input("Estados", key="states").split(',')

    st.subheader("Informe o alfabeto separado por vírgula (ex: a,b,c):")
    alphabet = st.text_input("Alfabeto", key="alphabet").split(',')

    st.subheader("Informe o alfabeto da pilha separado por vírgula (ex: X,Y,Z):")
    stack_alphabet = st.text_input("Alfabeto da Pilha", key="stack_alphabet").split(',')

    start_state = st.text_input("Informe o estado inicial", key="start_state")
    
    st.subheader("Informe os estados de aceitação separados por vírgula (ex: q2,q3):")
    accept_states = st.text_input("Estados de Aceitação", key="accept_states").split(',')

    transitions = {}
    st.subheader("Informe as transições (estado atual, símbolo de entrada, símbolo da pilha, estado de destino, símbolos a serem empilhados):")
    transition_count = st.number_input("Quantidade de transições", value=1, min_value=1, key="transition_count")
    for i in range(transition_count):
        current_state = st.text_input(f"Estado atual {i+1}", key=f"current_state_{i}")
        if current_state == 'fim':
            break
        input_symbol = st.text_input(f"Símbolo de entrada {i+1}", key=f"input_symbol_{i}")
        stack_symbol = st.text_input(f"Símbolo da pilha {i+1}", key=f"stack_symbol_{i}")
        to_state = st.text_input(f"Estado de destino {i+1}", key=f"to_state_{i}")
        push_symbols = st.text_input(f"Símbolos a serem empilhados {i+1} (ε para vazio)", key=f"push_symbols_{i}")
        transitions[(current_state, input_symbol, stack_symbol)] = (to_state, push_symbols)

    return states, alphabet, stack_alphabet, transitions, start_state, accept_states

def main():
    st.title("Simulador de Autômatos com Pilha")
    sextuple = get_user_input_sextuple()
    input_string = st.text_input("Digite a entrada:")
    
    if st.button("Simular"):
        create_pda_from_sextuple(sextuple, input_string)

if __name__ == "__main__":
    main()