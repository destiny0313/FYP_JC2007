# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 21:17:47 2020

@author: user
"""

import mysql.connector as mc
import pandas as pd

mydb = mc.connect(
       host = "localhost",
       user = "root",
       password = "",
       database = "fyp jc2007"
)

mycursor = mydb.cursor()
sql_query = "SELECT * FROM Stock_List"
mycursor.execute(sql_query)
stock_code = mycursor.fetchall()

list_dict = {"Stock_Code":[], "Company_Name":[]}

for stock in stock_code:
    list_dict["Stock_Code"].append(stock[0])
    list_dict["Company_Name"].append(stock[1])
    

df = pd.DataFrame.from_dict(list_dict)
df.to_csv(r"C:\Users\user\FYP_JC2007\Source\Stock_List.csv", index = False)