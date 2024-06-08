# from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from pages.home.navigation_page import NavigationPage

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    #locators
    _login_link = "//a[normalize-space()='Sign In']"
    _email_field = "email"
    _password_field = "login-password"
    _login_button = "login"
#dont need because we added methods in selenium_driver file
    # def getLoginLink(self):
    #     return self.driver.find_element(By.XPATH, self._login_link)
    #
    # def getEmailField(self):
    #     return self.driver.find_element(By.ID, self._email_field)
    #
    # def getPasswordField(self):
    #     return self.driver.find_element(By.ID,self._password_field)
    #
    # def getLoginButton(self):
    #     return self.driver.find_element(By.ID, self._login_button)

    #actions
    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType= "xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType = "id")

#call method to perform actions
    def login(self, email="", password=""): #= empty makes optional arguments
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSucessful(self):
        result = self.isElementPresent("dropdownMenu1",locatorType="id")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//span[contains(text(),'Incorrect login details. Please try again.')]",locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("My Courses")

    def logout(self):
        self.nav.navigateToUser()
        self.elementClick(locator="//div[@class='dropdown open']//a[@href='/logout']", locatorType="xpath")


