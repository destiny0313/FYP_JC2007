# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 10:27:05 2020

@author: user
"""

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import mysql.connector as mc

mydb = mc.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "fyp jc2007"
)

mycursor = mydb.cursor()
select_query = "SELECT Content, Date FROM tweet WHERE Stock_code = 'TSLA'"
mycursor.execute(select_query)
tweets = mycursor.fetchall()
#################################################################################################################


SIA = SentimentIntensityAnalyzer()

pos_dict = {}
neg_dict = {}

pos_extra = pd.read_excel(r'LoughranMcDonald_SentimentWordLists_2018.xlsx', sheet_name = "Positive", header=None)
neg_extra = pd.read_excel(r'LoughranMcDonald_SentimentWordLists_2018.xlsx', sheet_name = "Negative", header=None)

for index, row in pos_extra.iterrows():
    pos_dict[row[0].lower()] = row[1]

for index, row in neg_extra.iterrows():
    neg_dict[row[0].lower()] = row[1]
    

SIA.lexicon.update(pos_dict)
SIA.lexicon.update(neg_dict)

data = {}
i = 0

for tweet in tweets:
    if(SIA.polarity_scores(str(tweet[0]))['compound']>0.05):
        status="Positive"
    elif(SIA.polarity_scores(str(tweet[0]))['compound']<0.05):
        status="Negative"
    else:
        status="Neutral"
    data[i] = [str(tweet[1]), status]
    i = i+1
    
print(data)

df = pd.DataFrame(data)
print(df)