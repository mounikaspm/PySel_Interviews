from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class DragAndDrop():

    def test(self):
        test = "https://demoqa.com/droppable/"
        driver = Chrome(executable_path='C:/drivers/chromedriver')
        driver.maximize_window()
        driver.get(test)
        driver.implicitly_wait(5)

        driver.switchto.frame(0)

        from_element = driver.find_element(By.ID, "draggable")
        to_element = driver.find_element(By.ID, "droppable")
        time.sleep(2)

        actions = ActionChains(driver)
        # actions.drag_and_drop(from_element, to_element).perform()
        # time.sleep(2)
        actions.click_and_hold(from_element).move_to_element(to_element).release().perform()
        time.sleep(2)

        print("drag passed")


exc = DragAndDrop()
exc.test()
