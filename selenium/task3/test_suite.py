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


@pytest.fixture(scope="session")
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


def test_2_alerts(browser):
    expected_alert_text = "I am a JS Alert"
    expected_confirm_text = "I am a JS Confirm"
    expected_prompt_text = "I am a JS prompt"
    # специально некорректный текст? Prompt -> prompt

    expected_result_alert_text = "You successfully clicked an alert"
    # специально некорректный текст? subccessfuly -> successfully
    expected_result_confirm_text = "You clicked: Ok"

    wait = WebDriverWait(driver=browser, timeout=DEFAULT_TIMEOUT)
    browser.get(f"{HEROKUAPP_URL}javascript_alerts")

    wait.until(EC.element_to_be_clickable(BUTTON_JS_ALERT)).click()
    # Нажать на кнопку “Click for JS Alert“

    alert_appearance(wait)
    alert = wait.until(lambda d: d.switch_to.alert)
    alert_text_verification(alert, expected_alert_text)
    # Отображается Alert с текстом “I am a
    # JS Alert“

    alert.accept()
    # В Alert нажать кнопку “OK“

    check_text_in_result(wait, expected_result_alert_text)
    # Alert закрылся. В секции “Result“
    # отображается текст “You subccessfuly
    # clicked an alert

    wait.until(EC.element_to_be_clickable(BUTTON_JS_CONFIRM)).click()
    # Нажать на кнопку “Click for JS Confirm“

    alert_appearance(wait)
    alert = wait.until(lambda d: d.switch_to.alert)
    alert_text_verification(alert, expected_confirm_text)
    # Отображается Alert с текстом “I am a
    # JS Confirm“

    alert.accept()
    # В Alert нажать кнопку “OK“

    check_text_in_result(wait, expected_result_confirm_text)
    # Alert закрылся. В секции “Result“
    # отображается текст “You clicked: Ok“

    wait.until(EC.element_to_be_clickable(BUTTON_JS_PROMPT)).click()
    # Нажать кнопку “Click for JS Prompt“

    alert_appearance(wait)
    alert = wait.until(lambda d: d.switch_to.alert)
    alert_text_verification(alert, expected_prompt_text)
    # Отображается Alert с текстом “I am a
    # JS Prompt“

    random_text = Faker().sentence(nb_words=2)

    alert.send_keys(random_text)
    alert.accept()
    # Ввести в поле ввода случайно
    # сгенерированный текст. Нажать кнопку
    # “OK“

    check_text_in_result(wait, f"You entered: {random_text}")
    # Alert закрылся. В секции “Result“
    # отображается текст “You entered:
    # %введенный случайно
    # сгенерированный текст%“
