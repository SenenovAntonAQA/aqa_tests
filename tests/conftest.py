import pytest
from browser.browser import Browser
from utils.config_reader import ConfigReader
from browser.browser_factory import BrowserFactory, AvailableDriverName


@pytest.fixture(scope="session")
def config():
    return ConfigReader.load_config()


@pytest.fixture
def browser(config):
    browser_name = config["browser"]["name"]
    headless = config["browser"]["headless"]
    window_size = config["browser"]["window_size"]

    options = []
    if headless:
        options.append("--headless=new")
    if window_size == "maximized":
        options.append("--start-maximized")
    else:
        options.append(f"--window-size={window_size}")

    driver = BrowserFactory.get_driver(
        driver_name=AvailableDriverName(browser_name),
        options=options
    )

    browser_instance = Browser(driver)
    yield browser_instance
    browser_instance.quit()
