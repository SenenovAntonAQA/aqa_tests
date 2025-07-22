from elements.web_element import WebElement
from .base_page import BasePage


class NewWindowPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@class='example']//h3"

    TEXT_ON_PAGE_LOC = "//*[@class='example']//h3"

    def __init__(self, browser):
        super().__init__(browser)
        self.name = "New Window Page"

        self.unique_element = WebElement(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="New Window Page -> Page header"
        )

        self.text_on_page = WebElement(
            self.browser,
            self.TEXT_ON_PAGE_LOC,
            description="New Window Page -> Text on page"
        )

    def get_text_new_page(self) -> str:
        text = self.text_on_page
        self.text_on_page.wait_for_visible()
        return text.get_text()


class WindowsPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//h3"

    NEW_WINDOW_LINK_LOC = "//*[@class='example']//a"

    def __init__(self, browser):
        super().__init__(browser)
        self.name = "Windows Page"

        self.unique_element = WebElement(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Windows Page -> Page header"
        )

        self.new_window_link = WebElement(
            self.browser,
            self.NEW_WINDOW_LINK_LOC,
            description="Windows Page -> Link 'Click Here'"
        )

    def open_new_window(self):
        self.new_window_link.wait_for_clickable()
        self.new_window_link.click()
