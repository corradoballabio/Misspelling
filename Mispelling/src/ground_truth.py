import numpy
numpy.set_printoptions(suppress=True)

global TEST

TEST = "F"

def is_letter(char):
    return ord(char) > 96 and ord(char) < 123

def is_word_correct(word):
    for char in word:
        if not is_letter(char):
            return False
    return True

def file_to_string(file_input):
    file_string = ""
    for line in file_input:
        for word in line.split():
            for i in range(len(word)-1):
                file_string += word[i]
    return file_string


pigreco = numpy.zeros(26) # occurrencies for words starting chars letter
final_p = numpy.zeros(26) # occurrencies for words trailing chars letter
transition_p = numpy.zeros((26,26)) # chances for each letter to be followed by another letter
obs_matrix = numpy.zeros((26, 26))

def transiction():
    print("Start transiction")

    with open('csv/gt_tweets.csv', 'r') as input_file:
        word_counter = 0
        for line in input_file:
            for word in line.split():
                if is_word_correct(word):
                    if is_letter(word[0]): # TODO: remove?
                        pigreco[ord(word[0]) - 97] += 1
                        word_counter += 1
                    if is_letter(word[len(word) - 1]):
                        final_p[ord(word[len(word) - 1]) - 97] += 1
                    if not len(word) == 1:
                        for j in range(len(word)-1):
                            i = j + 1
                            if is_letter(word[i]): # TODO: remove?
                                if is_letter(word[j]):
                                    transition_p[ord(word[j]) - 97][ord(word[i])- 97] += 1

    if not word_counter == 0:
        for i in range(len(pigreco)):
            pigreco[i] = pigreco[i]/word_counter
            final_p[i] = final_p[i]/word_counter

    for i in range(len(transition_p)):
        counter = 0
        for j in range(len(transition_p[i])):
            counter += transition_p[i][j]
        if not counter == 0:
            for j in range(len(transition_p[i])):
                transition_p[i][j] = transition_p[i][j]/counter

    print("End transiction")


def observations_p(cleaned_tweets, perturbated_tweets):
    print("Start observations_p")

    clean_string = file_to_string(cleaned_tweets)
    pert_string = file_to_string(perturbated_tweets)

    for i in range(len(clean_string)):
        if is_letter(clean_string[i]):
            obs_matrix[ord(clean_string[i])-97][ord(pert_string[i])-97] += 1

    for i in range(len(obs_matrix)):
        counter = 0.0
        for j in range(len(obs_matrix[i])):
            counter += obs_matrix[i][j]
        if not counter == 0:
            for j in range(len(obs_matrix[i])):
                obs_matrix[i][j] = float(obs_matrix[i][j])/counter

    print("End observations_p")
