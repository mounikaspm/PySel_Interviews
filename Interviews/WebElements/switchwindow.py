from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from itertools import count
import time


class SwitchWindow():
    def test1(self):
        url = "https://letskodeit.teachable.com/pages/practice"
        driver = Chrome(executable_path='C:/drivers/chromedriver')
        driver.maximize_window()
        driver.get(url)
        time.sleep(5)
        driver.execute_script("windows.scrollTo(0,100);")

        # find current window -> current_window_handles, window_handles
        parent_window = driver.current_window_handle

        click_button_open = driver.find_element(By.ID, "openwindow")
        click_button_open.click()
        time.sleep(5)

        # to know no of windows open
        handles = driver.window_handles
        a = 0
        for handle in handles:
            print("handle id is" + handle)
            a = a + 1
        print("No of current handles or current windows open are" + a)

        # switch to child window
        for handle in handles:
            if handle not in parent_window:
                driver._switch_to.window(handle)
                print("Window switched to" + handle)
                #code in child window
                time.sleep(5)
                searchBox_id = driver.find_element(By.ID, "search")
                searchBox_id.send_keys("python")
                driver.close()
                break

        # back to parent window
        driver.switch_to.window(parent_window)
        driver.find_element(By.ID, "name").send_keys("abc")

