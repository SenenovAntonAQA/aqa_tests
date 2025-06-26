import pytest
from driver import Driver
from config_reader import ConfigReader


@pytest.fixture(scope="session")
def config_reader():
    return ConfigReader()


@pytest.fixture(scope="session")
def browser(request, config_reader):
    language = getattr(request, 'param', 'en')

    driver = Driver(
        options=config_reader.get_browser_options(language=language))
    yield driver
    driver.quit()
