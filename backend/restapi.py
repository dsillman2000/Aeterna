#How it works, based on scores for data
#Regression - find if you are on a downward trend
#Z-score of this data - how bad is the most recent post?
#Median of the data - is the baseline bad?

from twittertools import get_posts

from flask import Flask
app = Flask(__name__)

@app.route('/analyze/<twitter>')
def index(twitter):
    posts = get_posts(twitter)
    print(twitter)
    print(posts)
    return "This is twitter: " + str(posts)

if __name__ == '__main__':
    app.run()