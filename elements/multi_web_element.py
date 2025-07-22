from typing_extensions import Self

from browser.browser import Browser
from elements.web_element import WebElement
from logger.logger import Logger


class MultiWebElement:
    DEFAULT_TIMEOUT = 10

    def __init__(
            self,
            browser: 'Browser',
            formattable_xpath: str,
            description: str = None,
            timeout: int = None
    ):
        self.index = 1

        self.browser = browser
        self.formattable_xpath = formattable_xpath
        self.timeout = timeout if timeout is not None else self.DEFAULT_TIMEOUT
        self.description = description if description else (
            self.formattable_xpath.format("'i'")
        )

    def __iter__(self) -> Self:
        self.index = 1
        return self

    def __next__(self) -> WebElement:
        current_element = WebElement(
            self.browser,
            self.formattable_xpath.format(self.index),
            f"{self.description}[{self.index}]",
            timeout=self.timeout
        )

        if not current_element.is_exists():
            raise StopIteration
        else:
            self.index += 1
            return current_element

    def __str__(self) -> str:
        return f"{self.__class__.__name__}[{self.index}]"

    def __repr__(self) -> str:
        return str(self)

    def get_element(self, index: int) -> WebElement:
        """Return select (index) WebElement."""
        return WebElement(
            self.browser,
            self.formattable_xpath.format(index),
            f"{self.description}[{index}]",
            timeout=self.timeout
        )

    def count_elements(self) -> int:
        """Return the number of all group elements."""
        count = 0
        index = 1  # Начинаем с первого элемента

        while True:
            element = WebElement(
                self.browser,
                self.formattable_xpath.format(index),
                f"{self.description}[{index}]",
                timeout=2
            )
            if not element.is_exists():
                break
            count += 1
            index += 1

        Logger.info(f"Count elements = '{count}'")
        return count
