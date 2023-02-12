import constants
import string
import csv
import ground_truth
import pomegranate

class Hmm:
    transition_p = []
    observations_p = []
    pi = []
    final_p = []
    model = ""

    def __init__(self, transitions, observations, pi, final):
        self.transition_p = transitions
        self.observations_p = observations
        self.pi = pi
        self.final_p = final


    def create_hmm(self, error_list):
        alphabet = list(string.ascii_lowercase)
        self.model = pomegranate.HiddenMarkovModel("Mispelling")

        for i in range(len(alphabet)):
            discrete_distribution = {}

            for j in range(len(alphabet)):
                discrete_distribution[alphabet[j]] = self.observations_p[i][j]

            globals()[alphabet[i]] = pomegranate.State(
                pomegranate.DiscreteDistribution(discrete_distribution),
                name = alphabet[i])

            self.model.add_state(globals()[alphabet[i]])

        for i in range(len(alphabet)):
            self.model.add_transition(self.model.start, globals()[alphabet[i]], self.pi[i])

        for i in range(len(alphabet)):
            self.model.add_transition(globals()[alphabet[i]], self.model.end, self.final_p[i])

        for i in range(len(alphabet)):
            for j in range(len(alphabet)):
                self.model.add_transition(globals()[alphabet[i]], globals()[alphabet[j]], self.transition_p[i][j])

        self.model.bake(True,None)

        csv_test = open("csv/perturbation_tweets.csv")
        inferred_text = []
        test_rows = []

        for line in csv_test:
            for word in line.split():
                if not ground_truth.is_word_correct(word):
                    continue
                if word == 'nan':
                    inferred_text.append('man ')
                    continue
                if word == 'inf':
                    inferred_text.append('inc ')
                    continue

                logp, path = self.model.viterbi(word)
                for idx, state in path:
                    if (state.name not in ['Mispelling-start', 'Mispelling-end']):
                        inferred_text.append(state.name.strip())
                inferred_text.append(constants.BLANK_SPACE)

            test_rows.append(''.join(inferred_text).strip())
            inferred_text = []

        with open('csv/output_tweets.csv', 'w') as w:
            writer = csv.writer(w, delimiter= '\n')
            writer.writerows([test_rows])

    txt = []
    out = ""

    def correct_from_input(self, input_text):
        self.txt = []
        for word in str(input_text).lower().split():
            # TODO how to resolve these keyword errors?
            if (word == "nan"):
                word = "man"
            if (word == "inf"):
                word = "inc"
            self.correct_word(word)
        return ''.join(self.txt).strip()


    def correct_word(self, word):
        for i in range(len(word)): # loop for each char
            if not ground_truth.is_letter(word[i]): # if is not a letter??
                if not len(word[:i]) == 0: # if is not the last char of the word
                    logp, path = self.model.viterbi(word[:i])
                    for idx, state in path:
                        if (state.name not in ['Mispelling-start', 'Mispelling-end']):
                            self.txt.append(state.name.strip())
                    self.txt.append(word[i])
                if len(word[i+1:]) == 0:
                    self.txt.append(constants.BLANK_SPACE)
                else:
                    self.correct_word(word[i+1:])
                return
        if not len(word) == 0:
            logp, path = self.model.viterbi(word)
            for idx, state in path:
                if (state.name not in ['Mispelling-start', 'Mispelling-end']):
                    self.txt.append(state.name.strip())
            self.txt.append(constants.BLANK_SPACE)
