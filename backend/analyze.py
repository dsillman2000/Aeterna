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
    worsttext = ''
    worstscore = 0
    for i in range(len(results)):
        if sentiment[i] < worstscore:
            worstscore = sentiment[i]
            worsttext = texts[i]
    #Find regression data - the trend
    slope, intercept, r, p, stderr = stats.linregress(dates, sentiment)
    worsening = False
    if p < 0.05 and slope < 0: #Significant result and negative
        worsening = True

    #Find the percentiles - Q1, Median, Q3
    #Results affected by Fear, Sadness, sentiment
    f1, f2, f3 = np.percentile(fear, 25), np.percentile(fear, 50), np.percentile(fear, 75)
    sad1, sad2, sad3 = np.percentile(sadness, 25), np.percentile(sadness, 50), np.percentile(sadness, 75)
    sen1, sen2, sen3 = np.percentile(sentiment, 25), np.percentile(sentiment, 50), np.percentile(sentiment, 75)
    suicidal = False
    #If the Q3 sentiment score minus the Q1 sad and fear scores is bad enough
    if sen3 - sad1 - f1 < -0.50:
        suicidal = True
    
    return {
        'suicidal': suicidal,
        'worsening': worsening,
        'worsttext': worsttext
    }

    
def test():
    pprint(analyze(['I want to die', 'Life is great']))