from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from website.base_page import BasePage


class SteamMainPage(BasePage):
    START_URL = "https://store.steampowered.com/"
    INPUT_SEARCH_LOCATOR = (By.ID, "store_nav_search_term")
    SEARCH_LOUPE_LOCATOR = (By.ID, "store_search_link")

    def open(self):
        self.driver.get(self.START_URL)

    def verify_open(self, lang):
        if lang == 'en':
            self.wait.until(EC.title_is('Welcome to Steam'))
        elif lang == 'ru':
            self.wait.until(EC.title_is('Добро пожаловать в Steam'))
        return True

    def search_smth(self, smth):
        self.wait.until(EC.visibility_of_element_located(
            self.INPUT_SEARCH_LOCATOR)).send_keys(smth)

    def search_tap_enter(self):
        self.wait.until(EC.visibility_of_element_located(
            self.INPUT_SEARCH_LOCATOR)).send_keys(Keys.RETURN)

    def search_click_loupe(self):
        self.wait.until(EC.element_to_be_clickable(
            self.SEARCH_LOUPE_LOCATOR)).click()