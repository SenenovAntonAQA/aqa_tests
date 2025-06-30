from selenium_tasks.task3.pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from enum import StrEnum


class JSAlertsPage(BasePage):
    HEROKUAPP_URL = "https://the-internet.herokuapp.com/"
    DEFAULT_TIMEOUT = 10
    CONGRATULATION_XPATH = (By.XPATH, "//*[@id='content']//p")
    BUTTON_JS_ALERT = (By.XPATH, "//*[@onclick='jsAlert()']")
    BUTTON_JS_CONFIRM = (By.XPATH, "//*[@onclick='jsConfirm()']")
    BUTTON_JS_PROMPT = (By.XPATH, "//*[@onclick='jsPrompt()']")
    RESULT_JAVASCRIPT_ALERTS = (
        By.XPATH, "//*[@id='result' and normalize-space() != '']")

    def alert_appearance(self):
        """Ожидание появления алёрта."""
        self.wait.until(EC.alert_is_present())

    def click_js_alert(self):
        """Кликаем на кнопку JS Alert."""
        self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_JS_ALERT)
        ).click()
        self.alert_appearance()

    def alert_accept(self):
        """Берем в фокус алёрт и нажимаем на "Принять" / "Ок"."""
        alert = self.wait.until(lambda d: d.switch_to.alert)
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
