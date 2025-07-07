from pages.basic_auth import BasicAuthPage
from utils.config_reader import ConfigReader


def test_1_basic_authorization(browser):
    login = ConfigReader.get("credentials.username")
    password = ConfigReader.get("credentials.password")

    browser.get(ConfigReader.get("urls.basic_auth").format(login, password))

    page_after_auth = BasicAuthPage(browser)

    expected_text = "Congratulations! You must have the proper credentials."
    actual_text = page_after_auth.get_congratulation_text()

    assert expected_text == actual_text, (
        f"После авторизации на сайте нет надписи {expected_text}."
    )
