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
