from elements.web_element import WebElement
from .base_page import BasePage


class ContextMenuPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//h3"

    CONTEXT_MENU_BOX_LOC = "hot-spot"

    def __init__(self, browser):
        super().__init__(browser)
        self.name = "Context Menu Page"

        self.unique_element = WebElement(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Context Menu -> Header Page"
        )

        self.context_menu_box = WebElement(
            self.browser,
            self.CONTEXT_MENU_BOX_LOC,
            description="Context Menu -> Right-click target area"
        )

    def right_click_box(self):
        self.context_menu_box.context_click()
