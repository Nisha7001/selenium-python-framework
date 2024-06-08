import time

from selenium import webdriver
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
    #need to verify two verification points
    #1 fails, code will not go to next verification point
    #if assert fails, it stops current test execution and
    #moves to next test method
    @pytest.mark.run(order=2)
    def test_validLogin(self):
        # verify login
        self.lp.login("n.shrestha8393@gmail.com", "ns@8393")
        result2 = self.lp.verifyLoginSucessful()
        self.ts.markFinal("test_validlogin", result2, "Login was successful")
        #verify title
        time.sleep(3)
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1, "Title Verification")

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.logout()
        self.lp.login("n.shrestha8393@gmail.com", "vxcvxcv")
        result = self.lp.verifyLoginFailed()
        assert result == True
