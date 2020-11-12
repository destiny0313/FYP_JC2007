# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 20:33:07 2020

@author: user
"""

import FundamentalAnalysis as fa
import csv


api_key = "6e5ecde1494f8945f457010be7b7920e"
revenue = {}


for stock in stocks:
    print(stock[0])
    income_statement_annually = fa.income_statement(stock[0], api_key, period="annual")
    if stock[0]=='AAP':
        break
    if income_statement_annually.empty:
        revenue[stock[0]] = "No data available"
    else:
        revenue[stock[0]] = income_statement_annually['2019'].revenue


print(revenue)