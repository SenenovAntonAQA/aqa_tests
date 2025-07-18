from bs4 import BeautifulSoup
from elements.web_element import WebElement
from .base_page import BasePage


class DynamicContentPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//h3"

    CENTARL_CONTENT_LOC = "//*[@class='large-10 columns large-centered']"

    def __init__(self, browser):
        super().__init__(browser)
        self.name = "Dynamic Content"

        self.unique_element = WebElement(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Dynamic Content -> Page header"
        )

        self.central_content = WebElement(
            self.browser,
            self.CENTARL_CONTENT_LOC,
            description="Dynamic Content -> Central content"
        )

    def get_all_avatars(self) -> list[str]:
        soup = BeautifulSoup(
            self.central_content.get_attribute("innerHTML"),
            "html.parser"
        )
        rows = soup.find_all("div", class_="large-2 columns")
        result = []

        for row in rows:
            img = row.find("img")
            if not img:
                continue
            result.append(img["src"])

        return result
