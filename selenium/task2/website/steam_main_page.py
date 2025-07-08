from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from website.base_page import BasePage


class SteamMainPage(BasePage):
    INPUT_SEARCH_LOCATOR = (By.ID, "store_nav_search_term")
    SEARCH_LOUPE_LOCATOR = (By.ID, "store_search_link")
    UNIC_MAIN_PAGE_ELEMENT = (
        By.XPATH, "//*[@id='home_featured_and_recommended']")

    def is_main_page_loaded(self) -> bool:
        try:
            self.wait.until(
                EC.visibility_of_element_located(self.UNIC_MAIN_PAGE_ELEMENT))
            return True
        except TimeoutException:
            return False

    def search_smth(self, smth):
        self.wait.until(EC.visibility_of_element_located(
            self.INPUT_SEARCH_LOCATOR)).send_keys(smth)

    def submit_search(self):
        self.wait.until(EC.visibility_of_element_located(
            self.INPUT_SEARCH_LOCATOR)).send_keys(Keys.RETURN)
