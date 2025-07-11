from elements.multi_web_element import MultiWebElement
from elements.web_element import WebElement
from .base_page import BasePage

class HoversPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@class='figure']//img"

    USERS_MULTI_WEB_ELEMENT_LOC = "//*[@class='figure'][{}]"
    USERS_NAME_MULTI_WEB_ELEMENT_LOC = "//*[@class='figure'][{}]//h5"
    USERS_HREF_MULTI_WEB_ELEMENT_LOC = "//*[@class='figure'][{}]//a"

    def __init__(self, browser):
        super().__init__(browser)
        self.name = "Hovers Page"

        self.unique_element = WebElement(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Hovers Page -> User's avatar"
        )

        self.group_users = MultiWebElement(
            self.browser,
            self.USERS_MULTI_WEB_ELEMENT_LOC,
            description="Hovers Page -> Group of users"
        )
        self.users_name = MultiWebElement(
            self.browser,
            self.USERS_NAME_MULTI_WEB_ELEMENT_LOC,
            description="Hovers Page -> User names on hover"
        )
        self.users_href = MultiWebElement(
            self.browser,
            self.USERS_HREF_MULTI_WEB_ELEMENT_LOC,
            description="Hovers Page -> User links on hover"
        )

    def get_count_group_users(self):
        count = self.group_users.count_elements()
        if not count == 0:
            return count
        else:
            raise ValueError("There are no users on the page")

    def take_focus_avatar(self, index):
        self.group_users.get_element(index).move_to_element()

    def get_user_names(self, index) -> str:
        name = self.users_name.get_element(index)
        name.wait_for_visible()
        return  name.get_text()

    def get_user_links(self, index) -> str:
        return  self.users_href.get_element(index).get_attribute("href")

    def click_user_link(self, index):
        link = self.users_href.get_element(index)
        link.wait_for_visible()
        link.click()
