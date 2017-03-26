from watson import get_feelings
from datetime import datetime
from scipy import stats
import numpy as np

#Given the text of each comment we're analyzing, generate Watson analysis and do math on it
#How it works, based on scores for data
#Regression - find if you are on a downward trend
#Z-score of this data - how bad is the most recent post?
#Median of the data - is the baseline bad?

#Format of texts:
#[(text, date), (text, date)...]
def analyze(texts):
    results = []
    anger = []
    disgust = []
    fear = []
    joy = []
    sadness = []
    sentiment = []
    dates = []
    for text in texts:
        t = get_feelings(text[0])
        results.append(t)
        anger.append(t['analysis']['emotion']['document']['emotion']['anger'])
        disgust.append(t['analysis']['emotion']['document']['emotion']['disgust'])
        fear.append(t['analysis']['emotion']['document']['emotion']['fear'])
        joy.append(t['analysis']['emotion']['document']['emotion']['joy'])
        sadness.append(t['analysis']['emotion']['document']['emotion']['sadness'])
        sentiment.append(t['analysis']['sentiment']['document']['score'])
        dates.append(datetime(text[1]))
    #Find regression data - the trend
    slop, intercept, r, p, stderr = stats.linregress(dates, sentiment)

    
def test():
    pprint(analyze(['I want to die', 'Life is great']))