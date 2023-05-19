# data analysis and wrangling
import pandas as pd
import numpy as np
import random as rnd
# visualization
import seaborn as sns
import matplotlib.pyplot as plt
#matplotlib inline

# machine learning
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

#pip install vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
tweets = pd.read_csv('ITM310Tweets.csv')
authors = pd.read_csv('ITM310Authors.csv')
#using sentiment analyzer to grade sentiment
sentiment = []
analyzer = SentimentIntensityAnalyzer()

for index,row in tweets.iterrows():
    tweet = str(row['Tweet'])
    vs = analyzer.polarity_scores(tweet)
    sentiment.append(vs)
tweets['VaderSentiment'] = sentiment
compound = []
for index, row in tweets.iterrows():
    compound.append(row['VaderSentiment']['compound'])
    
tweets['sentiment'] = compound
tweets.head()
# Dropping duplicate rows based on the "column_name" column
authors = authors.drop_duplicates(subset=['AuthorId'], keep= 'last')

# Printing the resulting DataFrame without duplicate rows
print(authors)
combo = tweets.merge(authors, on='AuthorId',how='left')
#labeling the tweets negative positive and neutral 
def get_sentiment_label(sentiment):
    if sentiment < -0.1:
        return 'negative'
    elif sentiment > 0.1:
        return 'positive'
    else:
        return 'neutral'

# Create a new column in the dataframe with the sentiment labels
combo['sentiment_label'] = combo['sentiment'].apply(get_sentiment_label)


# Display the updated dataframe
print(combo)
combo['Unreal'] = combo['Tweet'].str.contains('Unreal' or 'UnrealEngine' or 'unreal' or 'unrealengine' or 'unrealgames' or 'UnrealGames')
combo['unity'] = combo['Tweet'].str.contains('Unity' or 'UnityEngine' or 'unity' or 'unityengine' or 'unitygames' or 'UnityGames')
#!pip install wordcloud

