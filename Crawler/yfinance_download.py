# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 14:30:01 2020

@author: desti
"""

import yfinance as yf
import csv
import time

with open('//data//opt//users//destiny//resource//Stock_List.csv','r') as stocklist:
    rstocklist = csv.reader(stocklist)
    for row in rstocklist:
        print(row)
        print(row[0])
        print(row[1])