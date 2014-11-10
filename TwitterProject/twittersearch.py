import datetime
import csv
from TwitterSearch import *
try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['uiuc']) # let's define all words we would like to have a look for
    tso.set_language('en') # we want to see German tweets only
    tso.set_include_entities(False) # and don't give us all those entity information
    #tso.set_since(datetime.date(2014, 11, 8))
    #tso.set_count(10)
    tso.set_until(datetime.date(2014, 11, 9))

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = 'Y1flWeItshriJ16N6HsfNWQHq',
        consumer_secret = '9isa7MAR3cEsFpcpMNZcIf197hSD4FkSqrnUGznDgyvHz87z0w',
        access_token = '1266814304-SGpFcwbC0C4LgnYPYe4rCiyOj2sk0icfie3BAXK',
        access_token_secret = 'UDeJuL0IfIsOlbkLviSi8vFsAX0dItXzc3prTBRDcMY4X'
    )

    # this is where the fun actually starts :)
    number = 0
    c = csv.writer(open("test.csv", "wb"))

    for tweet in ts.search_tweets_iterable(tso):
        print( '%s : %s : %s' % ( tweet['user']['screen_name'], tweet['created_at'], tweet['retweet_count']) )
        ts =  tweet['created_at']
        c.writerow([ts[:3], tweet['retweet_count']])
        number = number+1

    print "Total Number of Links:", number

    #part1: order by retweet count
    #part2: make a csv file of it: just timestamps (done)
    #mid23: add tweets per day and show them 
    #part3: take the data from the csv file to make a scatter plot

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)
