from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import re

from website.base_page import BasePage


class SteamSearchPage(BasePage):
    SEARCH_SORT_MENU = (By.ID, "sort_by_trigger")
    PRICE_ASC_LOCATOR = (By.ID, "Price_ASC")
    PRICE_DESC_LOCATOR = (By.ID, "Price_DESC")

    PRICE_GAMES = (
        By.XPATH,
        "//*[contains(@class, 'discount_final_price')]//text()[last()]")

    def verify_search(self, name_game):
        element_text = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, f"//*[@data-tag_value='{name_game}']/span"))
        ).text
        return name_game in element_text

    def sort_by_price(self, direction="DESC"):
        # если по убыванию цены, то указываем "DESC", иначе (умолчательно) ASC
        self.wait.until(
            EC.element_to_be_clickable(self.SEARCH_SORT_MENU)).click()

        if direction == "ASC":
            self.wait.until(EC.visibility_of_element_located(
                self.PRICE_ASC_LOCATOR)).click()
        elif direction == "DESC":
            self.wait.until(EC.visibility_of_element_located(
                self.PRICE_DESC_LOCATOR)).click()

    def get_price_results(self, number):
        # возвращаем отсортированный по цене список из N игр
        prices = self.wait.until(EC.presence_of_all_elements_located(
            self.PRICE_GAMES))

        price_values = []
        for element in prices[:number]:
            price_text = element.text.strip()
            if "free" in price_text.lower():
                price_values.append(0.0)
                continue

            price_match = re.search(r'(\d[\d\s,.]*\d)', price_text)
            if price_match:
                price_str = price_match.group(1)
                price = float(price_str.replace(' ', '').replace(',', '.'))
                price_values.append(price)

        return price_values

    @staticmethod
    def verify_price_desc(prices):
        return all(prices[i] >= prices[i+1] for i in range(len(prices)-1))
