import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker


@pytest.fixture(scope="session", autouse=True)
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def fake_username():
    return Faker().user_name()


@pytest.fixture
def fake_password():
    return Faker().password(length=10, special_chars=True, digits=True, upper_case=True)


def test_try_login_to_steam(driver, fake_username, fake_password):
    URL_STEAM = "https://store.steampowered.com/"
    LOGIN_HREF = (By.XPATH, "//a[contains(@class, 'global_action_link')]")
    USERNAME = (By.XPATH, "//input[@type='text']")  # поле ввода имени аккаунта
    PASS = (By.XPATH, "//input[@type='password']")  # поле ввода пароля
    SUBMIT_BUT = (By.XPATH, "//button[@type='submit']")  # кнопка войти
    WRONG_CREDENTIALS = (By.XPATH, "//form//div[contains(text(), 'проверьте')]")

    wait = WebDriverWait(driver, timeout=10, poll_frequency=1)
    driver.get(url=URL_STEAM)

    wait.until(EC.presence_of_element_located(LOGIN_HREF)).click()

    wait.until(EC.element_to_be_clickable(USERNAME)).send_keys(fake_username)

    wait.until(EC.element_to_be_clickable(PASS)).send_keys(fake_password)

    wait.until(EC.element_to_be_clickable(SUBMIT_BUT)).click()

    assert wait.until(EC.visibility_of_element_located(WRONG_CREDENTIALS)).text == "Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова.", "Текст при ошибочных кредах после клика на 'Войти' не соответствует ТЗ"