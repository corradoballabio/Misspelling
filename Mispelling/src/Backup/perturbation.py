import random
import csv
import ground_truth
import tweet_to_csv

def perturbate_tweets():
    riscrittura = []
    with open('csv/clean_tweets.csv', 'r') as r:
        reader = csv.reader(r)
        for line in reader:
            tweet = line[0]
            for i in range(len(tweet)):
                if ground_truth.is_letter(tweet[i]):
                    r = random.random()
                    if r < 0.1:
                        r_index = random.randint(0, len(tweet_to_csv.error_list[ord(tweet[i])-97]) - 1)
                        tweet = tweet[:i] + tweet_to_csv.error_list[ord(tweet[i])-97][r_index] + tweet[i+1:]
                if i == len(tweet)-1:
                    riscrittura.append(tweet)

    with open('csv/perturbation_tweets.csv', 'w') as w:
        writer = csv.writer(w, delimiter='\n')
        writer.writerows([riscrittura])

    print("finito")