import praw
r = praw.Reddit(user_agent='info490_application')
r.login('lelouchlamparouge','codegeass123')
submissions = r.get_subreddit('uiuc').get_hot(limit=10)
for i in submissions:
	for j in 
		print(j)