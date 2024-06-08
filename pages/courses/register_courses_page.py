import time

import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ################
    ### Locators ###
    ################
    _allcourses_button = "//a[@class='dynamic-link'][contains(text(), 'ALL COURSES')]"
    _search_box = "search"
    _search_button="//button[@class='find-course search-course']"
    _course = "//div[contains(@class, 'zen-course-list')]//h4[contains(text(), '{0}')]"
    _all_courses = "//div[@class='zen-course-list']"
    _enroll_button = "//button[@class='dynamic-button btn btn-default btn-lg btn-enroll']"
    _cc_num = "//input[@aria-label='Credit or debit card number']"
    _cc_exp = "exp-date"
    _cc_cvv = "cvc"
    _submit_enroll = "//button[@class='zen-subscribe sp-buy btn btn-default btn-lg btn-block btn-gtw btn-submit checkout-button dynamic-button']"
    _enroll_error_message = "//div[contains(@class, 'card-errors has-error')]//span[contains(text(), 'Your card number is invalid')]"

    ############################
    ### Element Interactions ###
    ############################

    def clickAllCoursesButton(self):
        self.elementClick(locator=self._allcourses_button, locatorType= "xpath")

    def enterCourseName(self, name):
        self.sendKeys(name, locator=self._search_box)

    def clickSearchButton(self):
        self.elementClick(locator=self._search_button,locatorType="xpath")

    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick(locator=self._course.format(fullCourseName), locatorType="xpath")

    def clickOnEnrollButton(self):
        self.elementClick(locator=self._enroll_button,locatorType="xpath")

    def enterCardNum(self, num):
        # This frame takes at least 6 seconds to show, it may take more for you
        time.sleep(6)
        # self.switchToFrame(name="__privateStripeFrame8")
        self.SwitchFrameByIndex(self._cc_num, locatorType="xpath")
        self.sendKeysWhenReady(num, locator=self._cc_num, locatorType="xpath")
        self.switchToDefaultContent()

    def enterCardExp(self, exp):
        # self.switchToFrame(name="__privateStripeFrame9")
        self.SwitchFrameByIndex(self._cc_exp, locatorType="name")
        self.sendKeys(exp, locator=self._cc_exp, locatorType="name")
        self.switchToDefaultContent()

    def enterCardCVV(self, cvv):
        # self.switchToFrame(name="__privateStripeFrame10")
        self.SwitchFrameByIndex(self._cc_cvv, locatorType="name")
        self.sendKeys(cvv, locator=self._cc_cvv, locatorType="name")
        self.switchToDefaultContent()

    # def clickEnrollSubmitButton(self):
    #    self.elementClick() since we cannot click if card is invalid

    def enterCreditCardInformation(self, num, exp, cvv):
        self.enterCardNum(num)
        time.sleep(3)
        self.enterCardExp(exp)
        time.sleep(3)
        self.enterCardCVV(cvv)

    def enrollCourse(self, num="", exp="", cvv=""):
        self.clickOnEnrollButton()
        self.webScroll(direction="down")
        self.enterCreditCardInformation(num, exp, cvv)
        #self.clickEnrollSubmitButton()

    def verifyEnrollFailed(self):
        # messageElement = self.waitForElement(self._enroll_error_message, locatorType="xpath") this line is not necessary now because error message appears without clicking on anything
        result = self.isElementDisplayed(self._enroll_error_message, locatorType="xpath")
        return result

    def verifyBuyButton(self):
        result = self.isEnabled(locator=self._submit_enroll, locatorType="xpath",
                                info="Enroll Button")
        return not result