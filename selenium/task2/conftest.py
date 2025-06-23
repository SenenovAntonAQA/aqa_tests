import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from driver import Driver


@pytest.fixture(scope="session")
def browser():
    driver = Driver()
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver.driver = webdriver.Chrome(options=options)
    yield driver

    try:
        driver.quit()
    finally:
        Driver._instances = {}

@pytest.fixture
def chrome_options(chrome_options, language):
    chrome_options.add_argument(f"--lang={language}")
    return chrome_options