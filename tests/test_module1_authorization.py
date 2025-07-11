from pages.basic_auth import BasicAuthPage
from utils.config_reader import ConfigReader

def open_with_auth(url, login, password):
    auth_url = url.replace("http://", f"http://{login}:{password}@")
    return auth_url

def test_case_1_basic_authorization(browser):

    browser.get(
        open_with_auth(
        url=ConfigReader.get("urls.basic_auth"),
        login=ConfigReader.get("credentials.username"),
        password=ConfigReader.get("credentials.password")
        )
    )

    page_after_auth = BasicAuthPage(browser)
    page_after_auth.wait_for_open()

    expected_text = "Congratulations! You must have the proper credentials."
    actual_text = page_after_auth.get_congratulation_text()

    assert expected_text == actual_text, (
        f"После авторизации на сайте нет надписи {expected_text}."
    )
