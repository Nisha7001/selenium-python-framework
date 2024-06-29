from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager, EdgeChromiumDriverManager

class WebDriverFactory():
    def __init__(self, browser):
        """
        Initializes WebDriverFactory class with the browser
        """
        self.browser = browser.lower()

    def getWebDriverInstance(self):
        """
        Get WebDriver Instance based on the browser configuration
        """
        baseURL = "https://www.letskodeit.com/"
        if self.browser == "iexplorer":
            driver = webdriver.Ie(service=Service(IEDriverManager().install()))
        elif self.browser == "firefox":
            options = FirefoxOptions()
            driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
        elif self.browser == "chrome":
            options = ChromeOptions()
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        elif self.browser == "edge":
            driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        else:
            raise ValueError("Unsupported browser")

        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseURL)
        return driver
