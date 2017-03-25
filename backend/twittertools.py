#The scripts for interacting with twitter
#Uses python-twitter, found at https://github.com/bear/python-twitter
#Documentation at https://python-twitter.readthedocs.io/en/latest/
import twitter

#Given a user's @name (screenname), return a list of all of their statuses.
def get_posts(screenname):
    api = twitter.Api(consumer_key='ikJIFDBN0h1LZomIkCRKbQXUE', consumer_secret='NS411RIiYBO2Gzj67pqcgFnD0AY3mPV5hWjkujCklZjeLurwDa', access_token_key='280279077-y9OmVTnveqglTJTy2ND2uPCy9wLWj9PnHDA0Kl0j', access_token_secret='HYW79wDKilDY44QX5mGupWx0001V06jz8mWCLt9aYihXe')
    posts = api.GetUserTimeline(screen_name=screenname, count=200, exclude_replies=True)
    return posts
