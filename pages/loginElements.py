from selenium.webdriver.common.by import By
from pages.basePage import BasePage


class LoginElements(BasePage):

    def getUsernameTextField(self):
        return self.browser.find_element(By.NAME, 'username')

    def getPasswordTextField(self):
        return self.browser.find_element(By.NAME, 'password')

    def getLoginButton(self):
        return self.browser.find_element(By.XPATH, '//*[text()=" Login "]')

    def getDashboardText(self):
        return self.browser.find_element(By.XPATH, '//h6[text()="Dashboard"]')
