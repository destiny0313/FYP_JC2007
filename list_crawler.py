from selenium import webdriver
import selenium.webdriver.support.ui as ui

driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
driver.get("https://www.nyse.com/listings_directory/stock")

wait = ui.WebDriverWait(driver, 10)

wait.until(lambda driver: driver.find_element_by_link_text('2'))
next_page = driver.find_element_by_link_text('2')
driver.execute_script("arguments[0].click();",next_page)