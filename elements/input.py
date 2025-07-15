from selenium.common import WebDriverException
from selenium.webdriver import Keys

from elements.base_element import BaseElement
from logger.logger import Logger


class Input(BaseElement):
    def clear(self) -> None:
        element = self.wait_for_visible()
        Logger.info(f"{self}: clear input")
        try:
            element.clear()
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def js_clear(self):
        input_element = self.wait_for_presence()
        Logger.info(f"{self}: js clear input")
        self.browser.execute_script(
            "arguments[0].value = '';",
            input_element
        )

    def send_keys(self, keys: str, clear: bool = True) -> None:
        if clear:
            self.clear()

        element = self.wait_for_visible()
        Logger.info(f"{self}: send keys = '{keys}'")

        try:
            element.send_keys(keys)
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def js_send_keys(self, keys: str, clear: bool = True) -> None:
        if clear:
            self.js_clear()

        input_element = self.wait_for_presence()
        Logger.info(f"{self}: js send keys = '{keys}'")
        self.browser.execute_script(
            "arguments[0].value = 'arguments[1]';",
            input_element,
            keys
        )

    def move_to_right(self, x):
        Logger.info(f"{self}: press right-keys '{x}' times")
        try:
            for _ in range(x):
                self._actions.send_keys(Keys.ARROW_RIGHT).perform()
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def move_to_left(self, x):
        Logger.info(f"{self}: press left-keys '{x}' times")
        try:
            for _ in range(x):
                self._actions.send_keys(Keys.ARROW_LEFT).perform()
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise
