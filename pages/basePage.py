import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
class BasePage():

    base_url = "https://opensource-demo.orangehrmlive.com/"

    def __init__(self, browser):
        self.browser = browser

    def entertext(self, element: WebElement, text: str):
        try:
            element.clear()
            element.send_keys(text)
        except Exception as e:
            print(f"Error while entering text: {e}")


    def clickElement(self, element: WebElement):
        try:
            self.waitUntilElementClickable(element)
            element.click()
        except Exception as e:
            time.sleep(1)
            element.click()

    def waitUntilElementClickable(self,element: WebElement):
        wait = WebDriverWait(self.browser, timeout=0)
        wait.until(EC.element_to_be_clickable(element))
        return element

    def waitUntileElementDisplayed(self,element: WebElement):
        wait = WebDriverWait(self.browser, timeout=0)
        wait.until(EC.visibility_of(element))
        return element


