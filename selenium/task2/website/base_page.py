from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    DEFAULT_TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.DEFAULT_TIMEOUT)
