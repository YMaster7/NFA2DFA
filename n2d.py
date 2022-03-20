from ruamel.yaml import YAML
from fa import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    '-i', '--input', default='nfa.yml', help='input file (default: nfa.yml)'
)
parser.add_argument(
    '-o', '--output', default='dfa.yml', help='output file (default: dfa.yml)'
)
parser.add_argument(
    '-r',
    '--random',
    action='store_true',
    help='generate random NFA for input AND write to input file',
)
args = parser.parse_args()

# load nfa
yaml = YAML()
yaml.default_flow_style = True
if args.random:
    with open(args.input, 'w') as f:
        nfa = random_fa()
        yaml.dump(nfa.__dict__(), f)
else:
    with open(args.input, 'r') as f:
        nfa = fa(**yaml.load(f))

# convert nfa to dfa
dfa = fa([], nfa.alphabet, nfa.start_state, [], dict())
new_states_counter = 1
new_states_dict = {0: [nfa.start_state]}
q = [0]  # unprocessed states
while q:
    current_state = q[0]
    q.pop(0)
    current_state_list = new_states_dict[current_state]

    # update dfa states
    dfa.states.append(current_state)

    # update dfa final
    for s in nfa.final_states:
        if s in current_state_list:
            dfa.final_states.append(current_state)
            break

    # update dfa transitions, for each letter
    for a in nfa.alphabet:
        # generate next state list
        next_state_list = set()
        for s in current_state_list:
            next_state_list.update(nfa.transitions[s][a])
        # map current_state_list to new_state
        if next_state_list not in new_states_dict.values():
            new_states_dict[new_states_counter] = next_state_list
            next_state = new_states_counter
            new_states_counter += 1
            # add to queue to wait for processing
            q.append(next_state)
        else:
            next_state = list(new_states_dict.keys())[
                list(new_states_dict.values()).index(next_state_list)
            ]
        # update
        dfa.transitions.setdefault(current_state, dict())
        dfa.transitions[current_state][a] = next_state

with open(args.output, 'w') as f:
    data = dfa.__dict__()
    for k, v in new_states_dict.items():
        new_states_dict[k] = list(v)
    data['representation'] = new_states_dict
    yaml.dump(data, f)
