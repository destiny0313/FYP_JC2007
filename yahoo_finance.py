import mysql.connector as mc
import urllib.request as ur
import time
from urllib.error import HTTPError


mydb = mc.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "fyp jc2007"
)

mycursor = mydb.cursor()
sql_select_query = "select * from stock_list;"
mycursor.execute(sql_select_query)
records = mycursor.fetchall()

sql = "INSERT IGNORE INTO historical_price (Company_ID, filepath) VALUES (%s, %s);"
count = 0

for row in records :
    company_id = row[0]
    url = ("https://query1.finance.yahoo.com/v7/finance/download/" + company_id + "?period1=1441929600&period2=1599782400&interval=1d&events=history")
    try:
        ur.urlretrieve(url, "C:\\Users\\user\\fyp_price\\" + company_id + ".csv")
        path = ("C:\\Users\\user\\fyp_price\\" + company_id + ".csv")
        mycursor.execute(sql, (company_id, path))
    except HTTPError as error:
        print(error);
        mycursor.execute(sql, (company_id, "No data available"))
    mydb.commit()
    count = count + 1
    if count%1000 == 0:
        time.sleep(600)
 
mycursor.close()
