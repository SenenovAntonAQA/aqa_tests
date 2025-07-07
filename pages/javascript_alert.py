from elements.button import Button
from elements.web_element import WebElement
from .base_page import BasePage


class JSAlertsPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//h3"

    BUTTON_JS_ALERT_LOC = "//*[@onclick='jsAlert()']"
    BUTTON_JS_CONFIRM_LOC = "//*[@onclick='jsConfirm()']"
    BUTTON_JS_PROMPT_LOC = "//*[@onclick='jsPrompt()']"
    RESULT_JAVASCRIPT_ALERTS_LOC = "//*[@id='result' and normalize-space() != '']"

    def __init__(self, browser):
        super().__init__(browser)
        self.name = "JS Alerts Page"

        self.unique_element = WebElement(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="JS Alerts Page -> Header Page"
        )

        self.alert_button = Button(
            self.browser,
            self.BUTTON_JS_ALERT_LOC,
            description="JS Alerts Page -> JS Alert Button"
        )
        self.confirm_button = Button(
            self.browser,
            self.BUTTON_JS_CONFIRM_LOC,
            description="JS Alerts Page -> JS Confirm Button"
        )
        self.prompt_button = Button(
            self.browser,
            self.BUTTON_JS_PROMPT_LOC,
            description="JS Alerts Page -> JS Prompt Button"
        )
        self.result_field = WebElement(
            self.browser,
            self.RESULT_JAVASCRIPT_ALERTS_LOC,
            description="JS Alerts Page -> Result Field on Page"
        )

    def text_in_result(self):
        return self.result_field.get_text()

    def click_alert(self):
        self.alert_button.click()

    def click_confirm(self):
        self.confirm_button.click()

    def click_prompt(self):
        self.prompt_button.click()

    def click_js_alert(self):
        self.alert_button.js_click()

    def click_js_confirm(self):
        self.confirm_button.js_click()

    def click_js_prompt(self):
        self.prompt_button.js_click()
