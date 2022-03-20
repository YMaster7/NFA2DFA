import random
import string


class fa:
    def __init__(self, states, alphabet, start_state, final_states, transitions):
        self.states = states
        self.alphabet = alphabet
        self.start_state = start_state
        self.final_states = final_states
        self.transitions: dict = transitions

    def __str__(self):
        return "States: {}\nAlphabet: {}\nStart: {}\nFinal: {}\nTransition: {}".format(
            self.states,
            self.alphabet,
            self.start_state,
            self.final_states,
            self.transitions,
        )

    def __dict__(self):
        return {
            'states': self.states,
            'alphabet': self.alphabet,
            'start_state': self.start_state,
            'final_states': self.final_states,
            'transitions': self.transitions,
        }


class random_fa(fa):
    def __init__(self, Nstates=5, Nalphabet=2, Nfinal_states=1, Ntransitions=2):
        self.states = list(range(Nstates))
        self.alphabet = list(string.ascii_lowercase)[0:Nalphabet]
        self.start_state = 0
        self.final_states = random.sample(
            self.states[1:], random.randint(1, Nfinal_states)
        )
        self.transitions = {}
        for s in self.states:
            for a in self.alphabet:
                self.transitions.setdefault(s, {})
                self.transitions[s][a] = random.sample(
                    self.states, random.randint(1, Ntransitions)
                )
