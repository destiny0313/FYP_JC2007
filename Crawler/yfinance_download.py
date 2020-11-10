# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 14:30:01 2020

@author: desti
"""

import yfinance as yf
import csv
import pandas as pd

with open('//data//opt//users//destiny//resource//Stock_List.csv','r') as stocklist:
    rstocklist = csv.reader(stocklist)
    for row in rstocklist:
       stock = yf.Ticker(row[0])
       hist = stock.history(period="max")
       df = pd.DataFrame(hist)
       name = "//data//opt//users//destiny//resource//history//"+row[0]+"_history.csv"
       df.to_csv(name)