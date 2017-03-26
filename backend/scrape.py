from datetime import datetime
from twittertools import get_posts

def get_inputs(twitter_name):
    posts = get_posts(twitter_name)
    inputs = []
    for post in posts:
        inputs.append((post.text, post.created_at_in_seconds))
    return inputs
