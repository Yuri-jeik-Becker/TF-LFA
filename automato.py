import graphviz


def creat_automato(txt):
    f = graphviz.Digraph('finite_state_machine', filename='fsm.gv')
    state = []
    for stateName in txt:
        state.append(stateName)
        
    