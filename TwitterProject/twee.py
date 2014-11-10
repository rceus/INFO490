import tweepy

CONSUMER_KEY="gTfHpoDtJOg61HvT8OA0N8q28"
CONSUMER_SECRET="a23gfGTukB24pXhjFoo5dHjYHjDfXQaDeN1cmn1dJPyeVvgg4A"
APP_TOKEN="1266814304-ZPf6Hti2lyi0JErbKZF0x196n894AamPejy7JEP"
APP_SECRET="e9K2RQtbZKSxNvKoDugslInRmM4kdmatZUJV7x4uvuKH1"

OAUTH_KEYS = {'consumer_key': CONSUMER_KEY, 'consumer_secret': CONSUMER_SECRET, 'access_token_key':APP_TOKEN, 'access_token_secret':APP_SECRET}

auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])
auth.set_access_token(APP_TOKEN, APP_SECRET)

api = tweepy.API(auth)

print("#Twitter")
search_results = api.search(q=" ", count=100)
#for tweet in tweepy.Cursor(api.search, q=('"tree"'), since='2014-01=01', until='2014-09-30').items(5):
#	print("tweet")

for i in search_results:
	print(i)