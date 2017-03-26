from twittertools import get_posts
from flask import Flask
from scrape import get_inputs
from analyze import analyze
import json 
app = Flask(__name__)

@app.route('/analyze/<twitter>')
def index(twitter):
    inputs = get_inputs(twitter)
    result = analyze(inputs)
    return json.dumps(result)

if __name__ == '__main__':
    app.run()