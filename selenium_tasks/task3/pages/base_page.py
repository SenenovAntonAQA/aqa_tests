from selenium.webdriver.support.wait import WebDriverWait
from selenium_tasks.task3.utils.config_reader import ConfigReader


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(
            browser,
            timeout=ConfigReader.get("timeouts.default")
        )
