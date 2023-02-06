'''
Created on 28 mag 2016

@author: Work
'''

from tweetToCsv import *
from ground_truth import *
from hmm import Hmm

import sys
import prediction_capabilities
import csv

if __name__ == '__main__':
    print("INIZIO MISPELLING")

    ##############################################################################################
    """
    print("SCARICA TWEETS")
    csv.get_all_tweets("UKLabour")
    csv.get_all_tweets("Conservatives")
    csv.get_all_tweets("David_Cameron")
    csv.get_all_tweets("MayorofLondon")
    csv.get_all_tweets("UniofOxford")
    csv.get_all_tweets("Cambridge_Uni")
    """
    ##############################################################################################
    print("PULIZIA TWEETS")
    cleanCsv()
    perturbate_tweets()

    transiction()
    clean_tweets = open('csv/lp_tweets.csv')
    perturbed_tweets = open('csv/perturbation_tweets.csv')
    observations_p(clean_tweets, perturbed_tweets)

    ##############################################################################################
    print("GENERAZIONE MODELLO HMM")
    hmm = Hmm(transition_p, obs_matrix, pigreco, final_p )
    hmm.create_hmm(error_list)


    print("################################################################")
    print("DIFFERENZA TRA ORIGINALI")
    clean_tweets = open('csv/lp_tweets.csv')
    perturbed_tweets = open('csv/perturbation_tweets.csv')
    prediction_capabilities.calculate_capabilities(clean_tweets, perturbed_tweets)

    print("################################################################")
    print("DIFFERENZA FINALE")
    clean_tweets = open('csv/lp_tweets.csv')
    output_tweets = open('csv/output_tweets.csv')
    prediction_capabilities.calculate_capabilities(clean_tweets, output_tweets, "After: ")

    ##############################################################################################