import streamlit as st
from graphviz import Digraph

def pushdown_automaton(input_string, transitions, start_state, accept_states):
    stack = []
    current_state = start_state

    for char in input_string:
        key = (current_state, char, stack[-1] if stack else '')
        if key in transitions:
            new_state, push_symbols = transitions[key]
            current_state = new_state
            if push_symbols != '':
                stack.extend(push_symbols)

        else:
            return False

    return current_state in accept_states

def main():
    st.title("Simulador de Autômatos com Pilha (Pushdown Automaton)")

    st.sidebar.header("Definir Autômato")

    start_state = st.sidebar.text_input("Estado Inicial:")
    states = st.sidebar.text_input("Estados (separados por vírgula):")
    accept_states = st.sidebar.text_input("Estados de Aceitação (separados por vírgula):")
    input_alphabet = st.sidebar.text_input("Alfabeto de Entrada:")
    stack_alphabet = st.sidebar.text_input("Alfabeto da Pilha:")
    transitions_text = st.sidebar.text_area("Transições (estado, entrada, pilha) -> (novo estado, símbolos a serem empilhados):")

    transitions = {}
    for line in transitions_text.split('\n'):
        parts = line.split(',')
        if len(parts) == 5:
            state, char, stack_top, new_state, push_symbols = parts
            transitions[(state, char, stack_top)] = (new_state, push_symbols)

    generate_automaton = st.sidebar.button("Gerar Autômato")

    if generate_automaton:
        # Gerar e mostrar o diagrama do autômato
        dot = Digraph(comment='Pushdown Automaton')

        # Adicione os estados ao diagrama
        states_list = states.split(',')
        for state in states_list:
            if state in accept_states:
                dot.node(state, shape='doublecircle')
            else:
                dot.node(state, shape='circle')

        # Adicione as transições ao diagrama
        for transition, (new_state, push_symbols) in transitions.items():
            current_state, char, stack_top = transition
            dot.edge(current_state, new_state, label=f"{char}, {stack_top} -> {push_symbols}")

        st.graphviz_chart(dot.source, use_container_width=True)

    test_tape = st.sidebar.button("Testar Fita")
    if test_tape:
        input_string = st.text_input("Entrada a ser Testada:")
        result = pushdown_automaton(input_string, transitions, start_state, accept_states.split(','))

        if result:
            st.success("Aceito")
        else:
            st.error("Rejeitado")

if __name__ == '__main__':
    main()
