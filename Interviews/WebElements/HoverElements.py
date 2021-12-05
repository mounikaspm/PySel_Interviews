from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

url = 'https://courses.letskodeit.com/practice'
driver = webdriver.Firefox(executable_path='C:\drivers\geckodriver.exe')
driver.get(url)
driver.execute_script('window.scrollBy(0, 400);')
time.sleep(2)
hoverElement = driver.find_element(By.ID, 'mousehover')
print('first')
hoverchild1 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[4]/div/fieldset/div/div/a[1]')

Actions = ActionChains(driver)
Actions.move_to_element(hoverElement).perform()
Actions.move_to_element(hoverchild1).click().perform()
time.sleep(2)

driver.quit()

