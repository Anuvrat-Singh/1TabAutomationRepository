from selenium import webdriver
from selenium.webdriver.common.by import By
from base.customMethods import SeleniumDriver
from base.basePage import BasePage
import logging
import utilities.custom_Logger as cl


class homePage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators section
    _login_Link = "//*[text()='Login ']"
    _username_Input = "user_input"
    _password_Input = "password"
    _submit_Button = "//button[@class='btn btn-success tab_yellowbtn w-100']"
    _login_Error = "//*[text() ='Provide valid Credentials']"

    # Finding Elements

    # def getLoginLink(self):
    #     return self.driver.find_element(By.XPATH, self._login_Link)
    #
    # def getEmailID(self):
    #     return self.driver.find_element(By.ID, self._username_Input)
    #
    # def getPasswordField(self):
    #     return self.driver.find_element(By.ID, self._password_Input)
    #
    # def getSubmitButton(self):
    #     return self.driver.find_element(By.XPATH,self._submit_Button)

    # Actions on locators

    def clickLoginLink(self):
        self.elementClick(self._login_Link, "xpath")

    def enterUsername(self, username):
        self.sendKeys(username, self._username_Input)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_Input)

    def clickSubmitButton(self):
        self.elementClick(self._submit_Button, "xpath")

    # class methods
    def login(self, username="", password=""):
        self.clickLoginLink()
        self.enterUsername(username)
        self.enterPassword(password)
        print("************************************")
        self.clickSubmitButton()

    def verifyLoginFailed(self):
        result = self.isElementPresent(self._login_Error, "xpath")
        return result

    def verifyLogin(self):
        result = self.isElementPresent("//*[text()='My Account']", "xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("India's One Of Most Trusted")
