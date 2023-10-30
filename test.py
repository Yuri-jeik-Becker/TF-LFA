def load_dpda_from_file(filename):
    dpda = {'Pilha': '', 'Inicial': '', 'Transicoes': []}

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('Pilha:'):
                dpda['Pilha'] = line.split(':')[1].strip()
            elif line.startswith('Inicial:'):
                dpda['Inicial'] = line.split(':')[1].strip()
            elif line.startswith('Transicao:'):
                parts = line.split(': ')[1].split(' -> ')
                estado_atual, entrada, topo_pilha = parts[0].split(', ')
                estado_destino, substituir_topo_pilha = parts[1].split(', ')
                dpda['Transicoes'].append((estado_atual, entrada, topo_pilha, estado_destino, substituir_topo_pilha))

    return dpda

def run_dpda(dpda, entrada):
    pilha = [dpda['Pilha']]
    estado_atual = dpda['Inicial']

    for simbolo in entrada:
        transicao_encontrada = False

        for transicao in dpda['Transicoes']:
            estado, entrada_simbolo, topo_pilha = transicao[:3]

            if estado == estado_atual and entrada_simbolo == simbolo and topo_pilha == pilha[-1]:
                estado_destino, substituir_topo_pilha = transicao[3:]

                if substituir_topo_pilha != 'vazio':
                    pilha.pop()
                    pilha.extend(reversed(substituir_topo_pilha))

                estado_atual = estado_destino
                transicao_encontrada = True
                break

        if not transicao_encontrada:
            return "Rejeita"

    if estado_atual == 'aceita' and len(pilha) == 1 and pilha[0] == 'Z':
        return "Aceita"
    else:
        return "Rejeita"

def main():
    dpda = load_dpda_from_file("automato.txt")

    while True:
        entrada = input("Digite uma entrada (ou 'exit' para sair): ")
        if entrada == 'exit':
            break
        resultado = run_dpda(dpda, entrada)
        print(f"Resultado para '{entrada}': {resultado}")

if __name__ == "__main":
    main()
