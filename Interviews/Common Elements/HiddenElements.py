
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver

'''
Hidden elements
destroyed or not destroyed when hidden
search elements when hidden
'''

driver = webdriver.Firefox(executable_path='C:/drivers/geckodriver.exe')
driver.get("https://courses.letskodeit.com/practice")
driver.maximize_window()
driver.implicitly_wait(20)

driver.find_element(By.ID, "hide-textbox")
driver.find_element(By.ID, "show-textbox")



