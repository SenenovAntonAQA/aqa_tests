import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.ie.webdriver import WebDriver


@pytest.fixture(scope="session")
def config():
    from selenium_tasks.task3.utils.config_reader import ConfigReader
    return ConfigReader.load_config()

@pytest.fixture
def browser(config):
    options = webdriver.ChromeOptions()
    if config["browser"]["headless"]:
        options.add_argument("--headless=new")
    if config["browser"]["window_size"] == "maximized":
        options.add_argument("--start-maximized")
    else:
        options.add_argument(f"--window-size={config["browser"]['window_size']}")

    driver = webdriver.Chrome(options=options)


    yield driver
    driver.quit()
