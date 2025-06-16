import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

URL_STEAM = "https://store.steampowered.com/"
LOGIN_HREF = (By.XPATH, "//a[contains(@class, 'global_action_link')]")
USERNAME = (By.XPATH, "//input[@type='text']")  # поле ввода имени аккаунта
PASS = (By.XPATH, "//input[@type='password']")  # поле ввода пароля
SUBMIT_BUT = (By.XPATH, "//button[@type='submit']")  # кнопка войти
WRONG_CREDENTIALS = (By.XPATH, "//button[@type='submit']/../following-sibling::div[string-length(normalize-space(text())) > 1]")
DEFAULT_TIMEOUT = 10


@pytest.fixture(scope="session")
def driver():
    """Фикстура для инициализации браузера (Chrome)"""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_try_login_to_steam(driver):
    wait = WebDriverWait(driver, timeout=DEFAULT_TIMEOUT)
    driver.get(url=URL_STEAM)
    # Navigate to main page.

    wait.until(EC.presence_of_element_located(LOGIN_HREF)).click()
    # Click login button.

    fake_username = Faker().user_name()
    fake_password = Faker().password(length=10, special_chars=True, digits=True, upper_case=True)

    wait.until(EC.element_to_be_clickable(USERNAME)).send_keys(fake_username)
    wait.until(EC.element_to_be_clickable(PASS)).send_keys(fake_password)
    # Input random strings as credentials.

    wait.until(EC.element_to_be_clickable(SUBMIT_BUT)).click()
    # Click sign in button.

    actual_text = wait.until(EC.visibility_of_element_located(WRONG_CREDENTIALS)).text
    expected_text = "Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова."

    assert actual_text == expected_text, f"После ввода некорректных (рандомных) данных ожидали текст {expected_text}, а получили {actual_text}"
    # Error text corresponds to the stated.