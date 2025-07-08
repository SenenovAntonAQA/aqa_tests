from elements.multi_web_element import MultiWebElement
from elements.web_element import WebElement
from .base_page import BasePage

class HorizontalSliderPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@class='figure']//img"

    GROUP_USERS_MULTI_WEB_ELEMENT_LOC = "//*[@class='figure'][{}]"

    def __init__(self, browser):
        super().__init__(browser)
        self.name = "Horizontal Slider Page"

        self.unique_element = WebElement(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Horizontal Slider Page -> Page Header"
        )

        self.slider = MultiWebElement(
            self.browser,
            self.GROUP_USERS_MULTI_WEB_ELEMENT_LOC,
            description="Horizontal Slider Page -> Group users"
        )