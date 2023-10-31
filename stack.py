import streamlit as st
from graphviz import Digraph
import time

def pushdown_automaton(input_string, transitions, start_state, accept_states, tape, current_position, current_state):
    key = (current_state, input_string[current_position], tape[current_position])
    if key in transitions:
        new_state, push_symbols = transitions[key]
        current_state = new_state
        # Atualize o estado da fita de acordo com os símbolos empilhados
        tape[current_position] = push_symbols

        # Verifique se a posição da fita permite um movimento válido
        if push_symbols != 'ε':  # Movimento para a direita
            current_position += 1
        else:  # Movimento para a esquerda
            current_position -= 1

    return current_state, tape, current_position

def create_dot_file(tape, current_position, start_state, states, accept_states, input_alphabet, stack_alphabet):
    dot_file = Digraph(comment='Fita e Autômato')
    dot_file.attr(rankdir='LR')

    # Adicione informações sobre o estado inicial, estados, alfabetos e estados de aceitação
    dot_file.node(f"Estado Inicial: {start_state}", shape='plaintext')
    dot_file.node(f"Estados: {states}", shape='plaintext')
    dot_file.node(f"Alfabeto de Entrada: {input_alphabet}", shape='plaintext')
    dot_file.node(f"Alfabeto da Pilha: {stack_alphabet}", shape='plaintext')
    dot_file.node(f"Estados de Aceitação: {accept_states}", shape='plaintext')

    for i, symbol in enumerate(tape):
        if i == current_position:
            dot_file.node(f'{i}: {symbol}', color='red', shape='box')
        else:
            dot_file.node(f'{i}: {symbol}', shape='box')

        if i < len(tape) - 1:
            dot_file.edge(f'{i}: {symbol}', f'{i + 1}: {tape[i + 1]}')

    return dot_file

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

    st.sidebar.header("Testar Fita")
    input_string = st.sidebar.text_input("Entrada a ser Testada:")
    test_tape_button = st.sidebar.button("Testar Fita")

    if test_tape_button:
        current_position = 1  # Comece na posição 1
        current_state = start_state
        tape = ["Z"] * (len(input_string) + 2)  # Inicialize a fita com o símbolo de início Z
        tape[1:len(input_string) + 1] = input_string  # Preencha a fita com a entrada
        tape[current_position] = current_state

        st.subheader("Simulação do Autômato")
        while current_position >= 1 and current_position < len(tape) - 1 and current_state not in accept_states:
            # Crie o arquivo DOT com o estado atual da fita e informações do autômato
            dot_file = create_dot_file(tape, current_position, start_state, states, accept_states, input_alphabet, stack_alphabet)
            dot_file.render(filename="fita", format="png")

            # Exiba a imagem do estado atual
            st.image("fita.png")

            # Atualize o estado atual da fita e do autômato
            current_state, tape, current_position = pushdown_automaton(input_string, transitions, start_state, accept_states, tape, current_position, current_state)

            time.sleep(1)  # Adicione uma pausa de 1 segundo para a animação

        if current_state in accept_states:
            st.success("Aceito")
        else:
            st.error("Rejeitado")

if __name__ == '__main__':
    main()
