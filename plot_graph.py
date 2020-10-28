# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 15:00:47 2020

@author: user
"""

# Import the yfinance. If you get module not found error the run !pip install yfinance from your Jupyter notebook
import yfinance as yf

# Get the data for the stock AAPL
data = yf.download('AAPL','2016-01-01','2020-10-26')
data2 = yf.download('TSLA','2016-01-01', '2020-10-26')
data3 = yf.download('A', '2016-01-01', '2020-10-26')

# Import the plotting library
import matplotlib.pyplot as plt


# Plot the close price of the AAPL
data['Adj Close'].plot()
data2['Adj Close'].plot()
data3['Adj Close'].plot()
fig = plt.figure()
fig.show()