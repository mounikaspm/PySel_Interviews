from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

class slider():
    def test(self):
        driver = Chrome(executable_path='C:/drivers/chromedriver')
        test = "https://demoqa.com/droppable/"
        find_slider = driver.find_element(By.XPATH, "//div[@id='slider']//span")
        driver.get(test)
        driver.maximize_window()
        driver.implicitly_wait(5)
        time.sleep(2)

        actions = ActionChains(driver)
        actions.drag_and_drop_by_offset(find_slider, 100).perform()


exc = slider()
exc.test()