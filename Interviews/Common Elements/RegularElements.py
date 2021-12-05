from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox(executable_path='C:/drivers/geckodriver.exe')
driver.get("https://courses.letskodeit.com/practice")
driver.maximize_window()
driver.implicitly_wait(20)

radio_select = driver.find_element(By.ID, "bmwradio")
checkbox_select = driver.find_element(By.ID, "bmwcheck")
dropdown_select = driver.find_element(By.ID, "carselect")
multi_select = driver.find_element(By.ID, "multiple-select-example")

radio_select.click()

if checkbox_select.is_selected() is False:
    checkbox_select.click()
else:
    pass
'''
Select sel = dropdown_select.click()
sel.select_by_value("bmw")

Select sel1 = multi_select.click()
sel1.select_by_index(0)
'''







