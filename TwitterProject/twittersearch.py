#####################################################################################
############################### First Part #########################################
#####################################################################################


import datetime
import csv
from TwitterSearch import *
try:
    tso = TwitterSearchOrder()      # create a TwitterSearchOrder object
    tso.set_keywords(['uiuc'])      # let's define all words we would like to have a look for
    tso.set_language('en')          # we want to see English tweets only
    tso.set_include_entities(False) # and don't give us all those entity information
    #tso.set_since(datetime.date(2014, 11, 8))
    #tso.set_count(10)
    tso.set_until(datetime.date(2014, 11, 9))

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = '',
        consumer_secret = '',
        access_token = '',
        access_token_secret = ''
    )

    # this is where the fun actually starts :)
    number = 0
    c = csv.writer(open("test2.csv", "wb"))

    for tweet in ts.search_tweets_iterable(tso):
        print( '%s : %s : %s' % ( tweet['user']['screen_name'], tweet['created_at'], tweet['retweet_count']) )
        ts =  tweet['created_at']
        c.writerow([ts[:3].lower(), tweet['retweet_count']])
        number = number+1

    print "Total Number of Links:", number


except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)
