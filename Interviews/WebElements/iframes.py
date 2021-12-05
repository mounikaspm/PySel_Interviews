from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from itertools import count
import time

class iFrame():
    def test1(self):
        url = "https://letskodeit.teachable.com/pages/practice"
        driver = Chrome(executable_path='C:/drivers/chromedriver')
        driver.maximize_window()
        driver.get(url)
        time.sleep(5)
        driver.execute_script("window.scrollBy(0,100);")

        '''
        iFrame elements cannot be accessed directly
        iFrame is a complete other page embedded in one part of page
        searchbox search fails for iFrame
        switch to iframe page from dom, in dom check document start of iFrame, switch to top window and work
        under iFrame tag, there will be id or name or number of iframe
        '''

        #iframe can be switched by id, name or number
        driver.switch_to.frame("courses-iframe") #by id
        #driver.switch_to.frame("iframe-name")  # by name
        #driver.switch_to.frame(0)  # by number, hit and trail method for number

        iframe_searchBox = driver.find_element(By.ID, "search")
        iframe_searchBox.send_keys("python")

        #switch to main content from iFrame
        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0,-100);")

        #enter text in textbox for confirmation
        driver.find_element(By.ID, "name").send_keys("mounika")






