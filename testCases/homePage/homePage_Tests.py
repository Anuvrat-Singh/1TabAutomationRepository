from pages.home.landingPage import homePage
from utilities.testStatus import TestStatus
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class loginTests(unittest.TestCase):

    # driver = webdriver.Chrome()
    # driver.maximize_window()
    # driver.implicitly_wait(10)
    # driver.set_page_load_timeout(10)
    # homePageObj = homePage(driver)

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.homePageObj = homePage(self.driver)
        self.testStatusObj = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def testValidLogin(self):
#        self.driver.get("https://qamain.1tab.com/")
        self.homePageObj.login("9899958909", "Anuvrat@1")
        result1 = self.homePageObj.verifyLoginTitle()
#        assert result1 == True
        self.testStatusObj.mark(result1, "Title Verification Failed!!!")
#        self.driver.close()
        result2 = self.homePageObj.verifyLogin()
#        assert result2 == True
        self.testStatusObj.markFinal("testValidLogin", result2, "User Login Verification Failed!!!")

    @pytest.mark.run(order=1)
    def testInvalidLogin(self):
#        self.driver.get("https://qamain.1tab.com/")
        self.homePageObj.login("s.anuvrat@1tab.com", "Anuvrat@")
        result = self.homePageObj.verifyLoginFailed()
#        assert result == True
#        self.driver.close()
        self.testStatusObj.markFinal("testInvalidLogin", result, "Login is Successful")
