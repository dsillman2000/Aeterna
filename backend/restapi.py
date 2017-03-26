from twittertools import get_posts
from flask import Flask
app = Flask(__name__)

@app.route('/analyze/<twitter>')
def index(twitter):
    posts = get_posts(twitter)
    texts = [post.text for post in posts]
    print(texts)

    return str(posts)

if __name__ == '__main__':
    app.run()