from elements.multi_web_element import MultiWebElement
from elements.web_element import WebElement
from .base_page import BasePage


class InfinityScrollPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[contains(@class,'jscroll-added')][1]"

    PARAGRAPHS_MULTI_WEB_ELEMENT = "//*[contains(@class,'jscroll-added')][{}]"

    def __init__(self, browser):
        super().__init__(browser)
        self.name = "Infinity Scroll"

        self.unique_element = WebElement(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Infinity Scroll -> First paragraphs"
        )

        self.all_par = MultiWebElement(
            self.browser,
            self.PARAGRAPHS_MULTI_WEB_ELEMENT,
            description="Infinity Scroll -> Elements of Group paragraphs"
        )

        self.count = 1

    def verify_element_number(self, number: int):
        self.count = self.all_par.count_elements()
        return self.count >= number

    def scroll_to_page_down(self):
        last_par = self.all_par.get_element(self.count)
        last_par.wait_for_visible()
        self.browser.execute_script(
            "window.scrollTo(0, document.body.scrollHeight)"
        )
