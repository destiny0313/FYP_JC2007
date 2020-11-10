# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 14:30:01 2020

@author: desti
"""

import yfinance as yf
import csv
import time

with open('//data//opt//users//destiny//resource//Stock_List.csv','r') as stocklist:
    for i, line in enumerate(stocklist):
        print "line{1} = {1}".format(i, line.split())