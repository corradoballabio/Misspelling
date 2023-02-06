'''
Created on 28 mag 2016

@author: Work
'''

from tweetToCsv import TweetToCsv
from ground_truth import Ground_Truth
from hmm import Hmm

import sys
import prediction_capabilities
import csv

if __name__ == '__main__':
    print("INIZIO MISPELLING")

    csv = TweetToCsv()
    esteem = Ground_Truth()

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
    csv.cleanCsv()
    csv.perturbate_tweets()

    esteem.transiction()
    clean_tweets = open('csv/lp_tweets.csv')
    perturbed_tweets = open('csv/perturbation_tweets.csv')
    esteem.observations_p(clean_tweets, perturbed_tweets)

    ##############################################################################################
    print("GENERAZIONE MODELLO HMM")
    hmm = Hmm(esteem.transition_p, esteem.obs_matrix, esteem.pigreco, esteem.final_p )
    hmm.create_hmm(csv.error_list)


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