from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class AlertConfirm:
    def test1(self):
        url = "https://letskodeit.teachable.com/pages/practice"
        driver = Chrome(executable_path='C:/drivers/chromedriver')
        driver.maximize_window()
        driver.get(url)
        time.sleep(5)

        textBox_name = driver.find_element(By.ID, "name")
        textBox_name.send_keys("mounika")

        alert_btn = driver.find_element(By.ID, "alertbtn")
        confirm_btn = driver.find_element(By.ID, "confirmbtn")

        alert_btn.click()
        alt = driver.switch_to.alert
        alt.accept()

        confirm_btn.click()
        cnf = driver.switch_to.alert
        cnf.dismiss()
        # cnf.accept()

        '''
        alert has JS popup, they do not have id or xpath
        find JS functions in script tag, linked to alert and confirm bottons of onclick()
        '''
