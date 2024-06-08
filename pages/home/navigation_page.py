# from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    _my_courses= "ALL COURSES" #linktext
    _all_courses = "MY COURSES" #linktext
    _home= "HOME"
    _user_settings_icon = "dropdownMenu1" #linktext

    def navigateToAllCourses(self):
        self.elementClick(locator=self._all_courses, locatorType="link")

    def navigateToMyCourses(self):
        self.elementClick(locator=self._my_courses, locatorType="link")

    def navigateToHome(self):
        self.elementClick(locator=self._home, locatorType="link")

    def navigateToUser(self):
        self.elementClick(locator=self._user_settings_icon, locatorType="id")




