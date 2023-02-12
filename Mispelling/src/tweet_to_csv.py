#!/usr/bin/env python
# encoding: utf-8

import tweepy
import csv
import re
import random
import ground_truth

#Twitter API credentials

consumer_key="F9TnxzJ3eEK4xB1hTbIYuPERa"
consumer_secret="E18qbpu8pEiQpxRzlWRW44ZmpmGwWV2zb1Y9eZ3G8vCrrIcPZP"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token="250822105-ufFJci3R3aV5IALFpmzVBTrSCVIYQDsH2Nt6k7Jn"
access_token_secret="8Hfv7AN8RnSwfM6oA9KOq8loSdWwvaJiQOcq6DwY8GB0T"

# it contains the keyboard button's letter aroun each letter of the alphabet
error_list = [
    ("s","q","z"),#a
    ("v","n","h","g"),#b
    ("x","v","f","d"),#c
    ("s","f","x","e"),#d
    ("w","r","d"),#e
    ("d","g","c","r","t"),#f
    ("f","h","v","t","y"),#g
    ("g","j","b","y","u"),#h
    ("u","o","k"),#i
    ("h","k","n","u"),#j
    ("j","l","m","i","o"),#k
    ("k","o","p","m"),#l
    ("j","k","l"),#m
    ("b","m","j","h"),#n
    ("i","p","k","l"),#o
    ("o","l"),#p
    ("w","a"),#q
    ("e","t","d","f"),#r
    ("a","d","z","w","e"),#s
    ("r","y","f","g"),#t
    ("y","i","h","j"),#u
    ("c","b","g"),#v
    ("q","e","a","s"),#w
    ("z","c","d","s"),#x
    ("t","u","g","h"),#y
    ("x","s","a")#z
]

def get_all_tweets(screen_name):

    print("start get_all_tweets")

    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    #initialize a list to hold all the tweepy Tweets
    all_tweets = []

    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)

    #save most recent tweets
    all_tweets.extend(new_tweets)

    #save the id of the oldest tweet less one
    oldest = all_tweets[-1].id - 1

    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print("getting tweets gefore %s" % (oldest))

        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)

        #save most recent tweets
        all_tweets.extend(new_tweets)

        #update the id of the oldest tweet less one
        oldest = all_tweets[-1].id - 1

    print("...%s tweets downloaded so far" % (len(all_tweets)))

    #transform the tweepy tweets into a 2D array that will populate the csv
    out_tweets = [[ tweet.text.encode("utf-8")] for tweet in all_tweets]

    #write the csv
    with open('csv/%s_tweets.csv' % screen_name, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(out_tweets)
    print("end get_all_tweets")


def clean_csv():

    print("Start clean_csv")

    #list with name of csv
    #source_accounts = ["BBCBreaking","WSJPolitics","NBA","nytimes","Pontifex","POTUS","SkyFootball","UN","WSJ","WWF"]
    source_accounts = ["UKLabour", "Conservatives", "David_Cameron", "MayorofLondon", "UniofOxford","Cambridge_Uni"]
    cleaned_text = []

    for source in source_accounts:
        with open('csv/%s_tweets.csv' % source, 'r') as source_file:
            reader = csv.reader(source_file)

            #clean rows removing punctuation and keywords that would make the parsing to fail
            for row in reader:
                cleaned_row = row[0].strip().lower()
                cleaned_row = re.sub('([^a-zA-Z0-9_ # @ \- \'])', '', cleaned_row.strip())
                cleaned_row = re.sub('([^a-z # @ \- \'])', '', cleaned_row.strip())
                cleaned_row = re.sub('-', ' ', cleaned_row.strip())
                cleaned_row = re.sub('\'', '', cleaned_row.strip())
                cleaned_row = re.sub('\"', '', cleaned_row.strip())
                cleaned_row = re.sub('(https)[a-z  # @ \%\']*', '', cleaned_row.strip())
                cleaned_row = re.sub('(http)[a-zA-Z0-9_  # @ \%\']*', '', cleaned_row.strip())
                cleaned_row = re.sub('(@[a-z]*)', '', cleaned_row.strip())
                cleaned_row = re.sub('(#[a-z]*)', '', cleaned_row.strip())
                cleaned_row = re.sub('(^rt\s[a-z \s]*)', '', cleaned_row.strip())
                cleaned_row = re.sub('nan', '', cleaned_row.strip())
                cleaned_row = re.sub('ban', '', cleaned_row.strip())
                cleaned_row = re.sub('han', '', cleaned_row.strip())
                cleaned_row = re.sub('jan', '', cleaned_row.strip())
                cleaned_row = re.sub('inf', '', cleaned_row.strip())
                cleaned_row = re.sub('^rt', '', cleaned_row.strip())
                cleaned_row = cleaned_row.strip()
                if len(cleaned_row) > 0:
                    cleaned_text.append(cleaned_row.lower().strip())

    #write the csv
    with open('csv/clean_tweets.csv', 'w') as clean_tweets:
        writer = csv.writer(clean_tweets, delimiter='\n')
        writer.writerows([cleaned_text])

    with open('csv/clean_tweets.csv', 'r') as clean_tweets:
        reader = csv.reader(clean_tweets)
        ns = []
        for line in reader:
            r = re.sub("\s\s+" , " ", line[0].strip())
            ns.append(r)

    with open('csv/clean_tweets.csv', 'w') as clean_tweets:
        writer = csv.writer(clean_tweets, delimiter='\n')
        writer.writerows([ns])

    # split source text in 80/20 for learning
    gt_rows = []
    test_rows = []
    with open('csv/clean_tweets.csv', 'r') as clean_tweets:
        reader = csv.reader(clean_tweets)
        for line in reader:
            r = random.random()
            if r < 0.8:
                gt_rows.append(line[0])
            else:
                test_rows.append(line[0])

    with open('csv/gt_tweets.csv', 'w') as gt, open('csv/lp_tweets.csv', 'w') as test:
        writer_gt = csv.writer(gt, delimiter = '\n')
        writer_gt.writerows([gt_rows])
        writer_test = csv.writer(test, delimiter = '\n')
        writer_test.writerows([test_rows])

    print("End clean_csv")


def perturbate_tweets():

    print("Start perturbation")

    perturbated_rows = []
    with open('csv/lp_tweets.csv', 'r') as r:
        reader = csv.reader(r)
        for line in reader:
            tweet = line[0]
            for i in range(len(tweet)):
                if ground_truth.is_letter(tweet[i]):
                    r = random.random()
                    if r < 0.1:
                        r_index = random.randint(0, len(error_list[ord(tweet[i])-97]) - 1)
                        tweet = tweet[:i] + error_list[ord(tweet[i])-97][r_index] + tweet[i+1:]
                if i == len(tweet)-1:
                    perturbated_rows.append(tweet)

    with open('csv/perturbation_tweets.csv', 'w') as w:
        writer = csv.writer(w, delimiter='\n')
        writer.writerows([perturbated_rows])

    print("End perturbation")