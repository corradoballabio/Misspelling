'''
Created on 28 mag 2016

@author: Work
'''

import tweet_to_csv
import ground_truth
import prediction_capabilities
from hmm import Hmm

if __name__ == '__main__':
    print("INIZIO MISPELLING")

    ##############################################################################################
    """
    print("SCARICA TWEETS")
    tweet_to_csv.get_all_tweets("UKLabour")
    tweet_to_csv.get_all_tweets("Conservatives")
    tweet_to_csv.get_all_tweets("David_Cameron")
    tweet_to_csv.get_all_tweets("MayorofLondon")
    tweet_to_csv.get_all_tweets("UniofOxford")
    tweet_to_csv.get_all_tweets("Cambridge_Uni")
    """
    ##############################################################################################
    print("PULIZIA TWEETS")
    tweet_to_csv.clean_csv()
    tweet_to_csv.perturbate_tweets()

    ground_truth.transiction()
    clean_tweets = open('csv/lp_tweets.csv')
    perturbed_tweets = open('csv/perturbation_tweets.csv')
    ground_truth.observations_p(clean_tweets, perturbed_tweets)

    ##############################################################################################
    print("GENERAZIONE MODELLO HMM")
    hmm = Hmm(ground_truth.transition_p, ground_truth.obs_matrix, ground_truth.pigreco, ground_truth.final_p )
    hmm.create_hmm(tweet_to_csv.error_list)


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