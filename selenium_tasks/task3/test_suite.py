import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from faker import Faker

HEROKUAPP_URL = "https://the-internet.herokuapp.com/"
DEFAULT_TIMEOUT = 10
CONGRATULATION_XPATH = (By.XPATH, "//*[@id='content']//p")
BUTTON_JS_ALERT = (By.XPATH, "//*[@onclick='jsAlert()']")
BUTTON_JS_CONFIRM = (By.XPATH, "//*[@onclick='jsConfirm()']")
BUTTON_JS_PROMPT = (By.XPATH, "//*[@onclick='jsPrompt()']")
RESULT_JAVASCRIPT_ALERTS = (
    By.XPATH, "//*[@id='result' and normalize-space() != '']")


@pytest.fixture(scope="module")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


def alert_appearance(wait):
    assert wait.until(EC.alert_is_present()), "Алёрт не появился"


def alert_text_verification(alert, text):
    assert alert.text == text, (f"Текст алерта ({alert.text}) не соответствует"
                                f" {text}")


def check_text_in_result(wait, expected_text):

    element = wait.until(
        EC.visibility_of_element_located(RESULT_JAVASCRIPT_ALERTS)
    )
    actual_text = element.text
    assert actual_text == expected_text, (
        f"В секции 'Result' отображается некорректный текст: '{actual_text}'. "
        f"Ожидалось: '{expected_text}'"
    )


def test_1_basic_authorization(browser):
    login = "admin"
    password = "admin"
    wait = WebDriverWait(driver=browser, timeout=DEFAULT_TIMEOUT)
    browser.get(
        url=f"http://{login}:{password}@the-internet.herokuapp.com/basic_auth")

    text_expected_result = "Congratulations! You must have the proper credentials."

    assert wait.until(
        EC.text_to_be_present_in_element(
            CONGRATULATION_XPATH,
            text_expected_result)), f"После авторизации на сайте нет надписи"
    f" {text_expected_result}."



