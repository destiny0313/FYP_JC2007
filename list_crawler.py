from selenium import webdriver
import selenium.webdriver.support.ui as ui
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
driver.get("https://www.nyse.com/listings_directory/stock")

time.sleep(3)

k=2
i = 3
for j in range(i):
    wait = ui.WebDriverWait(driver, 10)
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    trlist = soup.find_all('tr')
    for tr in trlist:
        tdlist = tr.find_all('td')
        for td in tdlist:
            print(td.text)
    wait.until(lambda driver: driver.find_element_by_link_text(str(k)))
    next_page = driver.find_element_by_link_text(str(k))
    driver.execute_script("arguments[0].click();",next_page)
    k=k+1
    time.sleep(1)


driver.quit()
