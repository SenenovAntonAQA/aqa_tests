from selenium_tasks.task3.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class JSAlertsPage(BasePage):
    BUTTON_JS_ALERT = (By.XPATH, "//*[@onclick='jsAlert()']")
    BUTTON_JS_CONFIRM = (By.XPATH, "//*[@onclick='jsConfirm()']")
    BUTTON_JS_PROMPT = (By.XPATH, "//*[@onclick='jsPrompt()']")
    RESULT_JAVASCRIPT_ALERTS = (
        By.XPATH, "//*[@id='result' and normalize-space() != '']")

    def text_in_result(self):
        """Отображение текста из поля 'Result'."""
        return self.wait.until(
            EC.visibility_of_element_located(self.RESULT_JAVASCRIPT_ALERTS)
        ).text

    def click_js_alert(self):
        """Кликаем на кнопку JS Alert."""
        self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_JS_ALERT)
        ).click()
        self.wait.until(EC.alert_is_present())

    def text_in_alert(self):
        """Выводим текст алёрта."""
        alert = self.wait.until(lambda d: d.switch_to.alert)
        return alert.text

    def click_js_confirm(self):
        """Кликаем на кнопку JS Confirm."""
        self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_JS_CONFIRM)
        ).click()
        self.wait.until(EC.alert_is_present())

    def click_js_prompt(self):
        """Кликаем на кнопку JS Prompt."""
        self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_JS_PROMPT)
        ).click()
        self.wait.until(EC.alert_is_present())

    def send_text_to_alert(self, text):
        alert = self.wait.until(lambda d: d.switch_to.alert)
        alert.send_keys(text)

    def alert_accept(self):
        """Берем в фокус алёрт и нажимаем на "Принять" / "Ок"."""
        alert = self.wait.until(lambda d: d.switch_to.alert)
        alert.accept()
