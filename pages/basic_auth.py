from elements.web_element import WebElement
from pages.base_page import BasePage


class BasicAuthPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//h3"

    UNIQUE_TEXT_FIELD_LOC = "//*[@id='content']//p"

    def __init__(self, browser):
        super().__init__(browser)
        self.name = "Basic Auth Page"

        self.unique_element = WebElement(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="After login Page -> Header after login"
        )
        self.text_field = WebElement(
            self.browser,
            self.UNIQUE_TEXT_FIELD_LOC,
            description="After login Page -> Text after login"
        )

    def get_congratulation_text(self):
        return self.text_field.get_text()
