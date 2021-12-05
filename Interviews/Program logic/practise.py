from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

url = 'https://www.nyse.com/trader-update/history#'
driver = webdriver.Firefox(executable_path='C:\drivers\geckodriver.exe')
driver.get(url)
driver.execute_script("window.scrollBy(0,200);")
time.sleep(3)
table = "//table[@class='table has-loader']"

columns = "//*[@id='business-unit-history']/div[1]/table/thead/tr/th"
rows = "//*[@id='business-unit-history']/div[1]/table/tbody/tr"

data = "//*[@id='business-unit-history']/div[1]/table/tbody/tr[1]/td[5]/span"

nColumns_path = driver.find_elements(By.XPATH, columns)
nRows_path = driver.find_elements(By.XPATH, rows)

a = len(nColumns_path) - 1  # 4
b = len(nRows_path)  # 9

