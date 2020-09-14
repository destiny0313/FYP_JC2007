import mysql.connector as mc
import urllib.request as ur


mydb = mc.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "fyp jc2007"
    )

mycursor = mydb.cursor()
sql_select_query = "select * from stock_list"
mycursor.excute(sql_select_query)
records = mycursor.fetchall()
count = mycursor.rowcount

sql = "INSERT INTO 'historical_price' ('company_id', 'filepath') VALUES (%s, %s)"

int i = 0
while i < count :
    for row in records :
        company_id = row[0]
        url = ("https://query1.finance.yahoo.com/v7/finance/download/" + company_id + "?period1=1441929600&period2=1599782400&interval=1d&events=history")
        ur.urlretrieve(url, company_id + ".csv")
        path = ("C:\python\" + company_id + ".csv")
        mycursor.execute(sql, (company_id, path))
        i ++

mydb.commit()
finally:
mycursor.close()



