from selenium import webdriver

from selenium import webdriver
import time
from PIL import Image

''' Scroll functionality '''
driver = webdriver.Firefox(executable_path='C:/drivers/geckodriver.exe')
driver.get("https://courses.letskodeit.com/practice")
driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
time.sleep(3)
# driver.close()

''' Take Screenshot '''

driver.get_screenshot_as_file('ss4.png')  # driver.save_screenshot('image.png')
print('SS taken')
driver.close()
