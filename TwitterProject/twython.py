from twython import Twython

TWITTER_APP_KEY = 'gTfHpoDtJOg61HvT8OA0N8q28' #supply the appropriate value
TWITTER_APP_KEY_SECRET = 'a23gfGTukB24pXhjFoo5dHjYHjDfXQaDeN1cmn1dJPyeVvgg4A' 
TWITTER_ACCESS_TOKEN = '1266814304-ZPf6Hti2lyi0JErbKZF0x196n894AamPejy7JEP'
TWITTER_ACCESS_TOKEN_SECRET = 'e9K2RQtbZKSxNvKoDugslInRmM4kdmatZUJV7x4uvuKH1'

t = Twython(app_key=TWITTER_APP_KEY, 
            app_secret=TWITTER_APP_KEY_SECRET, 
            oauth_token=TWITTER_ACCESS_TOKEN, 
            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

search = t.search(q='#omg',   #**supply whatever query you want here**
                  count=100)

tweets = search['statuses']

for tweet in tweets:
  print tweet['id_str'], '\n', tweet['text'], '\n\n\n'