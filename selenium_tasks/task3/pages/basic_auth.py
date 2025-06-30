from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class StartPage(BasePage):
    CONGRATULATION_XPATH = (By.XPATH, "//*[@id='content']//p")

    def get_congratulation_text(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.CONGRATULATION_XPATH)
        ).text