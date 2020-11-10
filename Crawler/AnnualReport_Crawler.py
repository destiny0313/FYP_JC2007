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
    url = ("https://www.annualreports.com/HostedData/AnnualReports/PDF/NYSE_" + company_id + "_2019.pdf")
    try:
        ur.urlretrieve(url, "//data//opt//users//destiny//Annual_Report//" + company_id + "_AR_2019.pdf")
    except HTTPError as error:
        print(error);
    mydb.commit()
    count = count + 1
    if count%1000 == 0:
        time.sleep(600)
 
mycursor.close()
