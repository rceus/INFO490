import twitter

CONSUMER_KEY = 'gTfHpoDtJOg61HvT8OA0N8q28'
CONSUMER_SECRET ='a23gfGTukB24pXhjFoo5dHjYHjDfXQaDeN1cmn1dJPyeVvgg4A'
OAUTH_TOKEN = '1266814304-ZPf6Hti2lyi0JErbKZF0x196n894AamPejy7JEP'
OAUTH_TOKEN_SECRET = 'e9K2RQtbZKSxNvKoDugslInRmM4kdmatZUJV7x4uvuKH1'

auth = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

twitter_api = twitter.Twitter(auth=auth)


print twitter_api


