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

sql = "INSERT IGNORE INTO annualreport_2019 (Company_ID, filepath) VALUES (%s, %s);"
count = 0

for row in records :
    company_id = row[0]
    url = ("https://www.annualreports.com/HostedData/AnnualReports/PDF/NYSE_" + company_id + "_2019.pdf")
    try:
        ur.urlretrieve(url, "C:\\Users\\user\\fyp_reports\\" + company_id + ".pdf")
        path = ("C:\\Users\\user\\fyp_reports\\" + company_id + ".pdf")
        mycursor.execute(sql, (company_id, path))
    except HTTPError as error:
        print(error);
        mycursor.execute(sql, (company_id, "No data available"))
    mydb.commit()
    count = count + 1
    if count%1000 == 0:
        time.sleep(600)
 
mycursor.close()
