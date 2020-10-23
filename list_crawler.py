from selenium import webdriver
import selenium.webdriver.support.ui as ui
import time
import mysql.connector as mc
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options


# MySQL server connection
mydb = mc.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "FYP"
    )

mycursor = mydb.cursor()
sql_insert = "INSERT IGNORE INTO stock_list (stock_code, company_name) VALUES (%s, %s);"


# Connect chrome browser to open NYSE offical page
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
                     
driver = webdriver.Chrome(executable_path="/data/opt/users/destiny/chromedriver")
driver.get("https://www.nyse.com/listings_directory/stock")


############################################# Preparation is done above #############################################

# Loop 653 times to crawl 653 pages

stock = ""
name = ""
i = 1
j = 1

while i <= 653:
    time.sleep(3)
    k = i + 1
    wait = ui.WebDriverWait(driver, 10)
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    trlist = soup.find_all('tr')
    
    for tr in trlist:
        tdlist = tr.find_all('td')
            
        for td in tdlist:
            if ((stock != '')and(name != '')):
                mycursor.execute(sql_insert, (stock, name))
                mydb.commit()
                stock = ''
                name = ''
                
            if j == 1:
                stock = td.text
                j = j + 1
                continue
            
            if j == 2:
                name = td.text
                j = j - 1
                continue
                
    wait.until(lambda driver: driver.find_element_by_link_text(str(k)))
    next_page = driver.find_element_by_link_text(str(k))
    driver.execute_script("arguments[0].click();",next_page)
    i = i + 1
    time.sleep(0.1)

html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
trlist = soup.find_all('tr')
    
mycursor.close
driver.quit()
