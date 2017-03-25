#Tools for utilizing IBM watson
#Using https://github.com/watson-developer-cloud/python-sdk
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as features
from pprint import pprint

natural_language_understanding = NaturalLanguageUnderstandingV1(version='2017-02-27', username='c3948056-aeb0-4492-8422-fd16cc613f7f', password='iFbA4CvlCxYS')


#Analyze the text for the emotions and sentiments in it
def get_feelings(text):
    global natural_language_understanding
    response = natural_language_understanding.analyze(text=text, features=[features.Emotion(), features.Sentiment()])
    return response
