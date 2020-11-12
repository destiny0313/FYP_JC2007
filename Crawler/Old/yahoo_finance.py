import mysql.connector as mc
import urllib.request as ur
import time
from urllib.error import HTTPError


mydb = mc.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "FYP"
)

mycursor = mydb.cursor()
sql_select_query = "select * from stock_list;"
mycursor.execute(sql_select_query)
records = mycursor.fetchall()

count = 0

for row in records :
    company_id = row[0]
    
    url = ("https://query1.finance.yahoo.com/v7/finance/download/" + company_id + "?period1=1441929600&period2=1599782400&interval=1d&events=history")
    try:
        ur.urlretrieve(url, "//data//opt//users//destiny//Historical_Price//" + company_id + ".csv")

    except HTTPError as error:
        print(error)
    mydb.commit()
    count = count + 1
    if count%1000 == 0:
        time.sleep(600)
 
mycursor.close()
