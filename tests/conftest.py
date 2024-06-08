import pytest
from selenium import webdriver
from base.webdriverfactory import WebDriverFactory
from pages.home.login_page import LoginPage

@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    #the commented line is not required as we added webdriverfactory
    # if browser == 'firefox':
    #     baseURL = "https://www.letskodeit.com/"
    #     driver = webdriver.Firefox()
    #     driver.maximize_window()
    #     driver.implicitly_wait(3)
    #     driver.get(self.baseURL)
    #     print("Running tests on FF")
    # else:
    #     baseURL = "https://www.letskodeit.com/"
    #     driver = webdriver.Edge()
    #     driver.get(baseURL)
    #     print("Running tests on Edge")
    lp = LoginPage(driver)
    lp.login("n.shrestha8393@gmail.com", "ns@8393")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    #driver.quit()
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")