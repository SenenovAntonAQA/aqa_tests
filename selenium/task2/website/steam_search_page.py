from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import re
from website.base_page import BasePage


class SteamSearchPage(BasePage):
    SEARCH_SORT_MENU = (By.ID, "sort_by_trigger")
    PRICE_DESC_LOCATOR = (By.ID, "Price_DESC")

    SEARCH_RESULTS = (
        By.XPATH,
        "//*[@id='search_result_container' and contains(@style, 'opacity')]"
    )

    GAME_PRICE_LOCATOR = (
        By.XPATH,
        "//*[contains(@class, 'discount_final_price')]"
    )

    SEARCH_RESULT_BY_NAME_TEMPLATE = (
        By.XPATH,
        "//*[@id='searchtag_tmpl']/span"
    )

    def get_search_result_tags(self):
        tags = self.wait.until(
            EC.presence_of_all_elements_located(
                self.SEARCH_RESULT_BY_NAME_TEMPLATE
            )
        )
        return tags

    def _wait_for_price_reload(self):
        self.wait.until_not(
            EC.presence_of_element_located(self.SEARCH_RESULTS)
        )

    def sort_by_price(self):
        # Сортировка по убыванию цены (с обновлением элементов)
        self.wait.until(
            EC.element_to_be_clickable(self.SEARCH_SORT_MENU)
        ).click()
        self.wait.until(
            EC.visibility_of_element_located(self.PRICE_DESC_LOCATOR)
        ).click()
        self._wait_for_price_reload()

    def get_price_results(self, number: int) -> list[float]:
        # Возвращает отсортированный по цене список из N игр
        self._wait_for_price_reload()
        prices = self.wait.until(
            EC.presence_of_all_elements_located(self.GAME_PRICE_LOCATOR)
        )
        return [self._parse_price(p.text) for p in prices[:number]]

    @staticmethod
    def _parse_price(price_text: str) -> float:
        if "free" in price_text.lower():
            return 0.0

        price_match = re.search(r'(\d[\d\s,.]*\d)', price_text)

        return (
            float(price_match.group(1).replace(' ', '').replace(',', '.'))
            if price_match
            else 0.0
        )