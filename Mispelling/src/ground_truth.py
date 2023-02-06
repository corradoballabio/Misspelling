'''
Created on 30 mag 2016

@author: corrado
'''
import numpy

global TEST

TEST = "F"

def is_letter(carattere):
    return ord(carattere) > 96 and ord(carattere) < 123

def is_word_correct(parola):
    for i in range(len(parola)) :
        if not is_letter(parola[i]) :
            return False
    return True

def file_to_string(file_input):
    file_string = ""
    for line in file_input:
        for word in line.split():
            for i in range(len(word)-1):
                file_string += word[i]
    return file_string


pigreco = numpy.zeros(26)
final_p = numpy.zeros(26)
transition_p = numpy.zeros((26,26))
obs_matrix = numpy.zeros(shape = (26, 26))

def transiction():
    print("Start transiction")

    input_file = open('csv/gt_tweets.csv')
    word_counter = 0
    for line in input_file : #leggo tutte le parole
        for word in line.split() : #divido lo stream di char in string appena trovo uno spazio
            if is_word_correct(word): #se la word contiene solo char alfabetici(escludo i # ma anche la punteggiatura)
                if is_letter(word[0]) : #DOVREBBE ESSERE INUTILE
                    pigreco[ord(word[0]) - 97] += 1
                    word_counter += 1
                if is_letter(word[len(word) - 1]):
                    final_p[ord(word[len(word) - 1]) - 97] += 1
            #ora controllo le P di passare da una lettera all'altra
                if not len(word) == 1 : #se la parola ha length almeno uguale a 2
                    for j in range(len(word)-1): #primo iteratore //faccio -1 perche incremento subito i
                        i = j + 1
                        if is_letter(word[i]): #se e' falso qua itera unaltra volta
                            if is_letter(word[j]): #se sono tutti e due lettere
                                transition_p[ord(word[j]) - 97][ord(word[i])- 97] += 1
    input_file.close()

    if not word_counter == 0:
        for i in range(len(pigreco)):
            pigreco[i] = pigreco[i]/word_counter #divido ogni i dell'array per il # di parole cosi' ho la distr. di P
            final_p[i] = final_p[i]/word_counter

    for i in range(len(transition_p)):
        counter = 0
        for j in range(len(transition_p[i])):
            counter += transition_p[i][j]
        if not counter == 0:
            for j in range(len(transition_p[i])):
                transition_p[i][j] = transition_p[i][j]/counter #round(transition_p[i][j]/(counter), 4)

    if (TEST == "T"):
        #stampa vettore pigreco
        print("vettore pigreco:")
        print(pigreco)
        print("\n")

        #stampa matrice di transizioni
        print("matrice transizione:")
        for line in transition_p:
            print(line)

    print("End transiction")


def observations_p(cleaned_tweets, perturbated_tweets):
    print("Start observations_p")

    clean_string = file_to_string(cleaned_tweets)
    pert_string = file_to_string(perturbated_tweets)

    if len(clean_string) == len(pert_string): #potremmo togliere questo controllo se ci fidiamo, risparimiamo 2n di computazione
        for i in range(len(clean_string)): #per ogni char controllo se sono uguali tra i due file
            if is_letter(clean_string[i]): #controllo se sono lettere (se dal parse tolgo i numeri posso toglierlo)
                obs_matrix[ord(clean_string[i])-97][ord(pert_string[i])-97] += 1 #altrimenti non fare nulla
    else:
        print("ERROR: le lunghezze dei due file non coincidono")

    for i in range(len(obs_matrix)):
        counter = 0.0
        for j in range(len(obs_matrix[i])):
            counter += obs_matrix[i][j]
        if not counter == 0:
            for j in range(len(obs_matrix[i])):
                obs_matrix[i][j] = float(obs_matrix[i][j])/counter

    print("End observations_p")
