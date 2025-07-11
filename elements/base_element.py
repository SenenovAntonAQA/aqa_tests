from selenium.common import TimeoutException, WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from logger.logger import Logger


class BaseElement:
    DEFAULT_TIMEOUT = 10

    def __init__(
            self,
            browser: 'Browser',
            locator: str | tuple,
            description: str = None,
            timeout: int = DEFAULT_TIMEOUT
    ):
        self.browser = browser
        self.timeout = timeout

        if isinstance(locator, str):
            if "/" in locator:
                self.locator = (By.XPATH, locator)
            else:
                self.locator = (By.ID, locator)
        else:
            self.locator = locator

        self.description = description if description else str(locator)

        self._wait = WebDriverWait(self.browser.driver, timeout=self.timeout)
        self._actions = ActionChains(self.browser.driver)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}[{self.description}]"

    def __repr__(self) -> str:
        return str(self)

    def _wait_for(self, expected_conditions) -> WebElement:
        try:
            Logger.info(f"{self}: wait for {expected_conditions.__name__}")
            element = self._wait.until(method=expected_conditions(self.locator))
            return element
        except TimeoutException as err:
            Logger.error(f"{self}: {err}")
            raise

    def _wait_for_not(self, expected_conditions) -> None:
        try:
            Logger.info(f"{self}: wait for not {expected_conditions.__name__}")
            self._wait.until_not(method=expected_conditions(self.locator))
        except TimeoutException as err:
            Logger.error(f"{self}: {err}")
            raise

    def wait_for_presence(self) -> WebElement:
        return self._wait_for(
            expected_conditions=EC.presence_of_element_located
        )

    def wait_for_clickable(self) -> WebElement:
        return self._wait_for(
            expected_conditions=EC.element_to_be_clickable
        )

    def wait_for_visible(self) -> WebElement:
        return self._wait_for(
            expected_conditions=EC.visibility_of_element_located
        )

    def is_enabled(self) -> bool:
        element = self.wait_for_presence()
        Logger.info(f"{self}: Whether the '{element}' is enabled")
        try:
            is_enabled = element.is_enabled()
            status = "enabled" if is_enabled else "disabled"
        except WebDriverException as err:
            Logger.error(
                f"{self}: : failed to check enabled state - {str(err)}"
            )
            raise
        Logger.info(f"{self}: element is {status}")
        return is_enabled

    def is_exists(self) -> bool:
        try:
            self.wait_for_presence()
            return True
        except TimeoutException:
            return False

    def is_displayed(self) -> bool:
        element = self.wait_for_presence()
        Logger.info(f"{self}: Checking visibility of element '{element}'")
        try:
            is_visible = element.is_enabled()
            status = "visible" if is_visible else "hidden"
        except WebDriverException as err:
            Logger.error(
                f"{self}: : failed to check visibility state - {str(err)}"
            )
            raise
        Logger.info(f"{self}: element is {status}")
        return is_visible

    def get_text(self) -> str:
        element = self.wait_for_presence()
        Logger.info(f"{self}: get text")
        try:
            text = element.text
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise
        Logger.info(f"{self}: text = '{text}'")
        return text

    def get_attribute(self, name: str) -> str:
        element = self.wait_for_presence()
        Logger.info(f"{self}: get attribute '{name}'")
        try:
            value = element.get_attribute(name)
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise
        Logger.info(f"{self}: attribute '{name}' = '{value}'")
        return value

    def click(self) -> None:
        element = self.wait_for_clickable()
        Logger.info(f"{self}: click")
        try:
            element.click()
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def context_click(self) -> None:
        element = self.wait_for_clickable()
        Logger.info(f"{self}: right-click (context click)")
        try:
            self._actions.context_click(element).perform()
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def js_click(self):
        element = self.wait_for_presence()
        Logger.info(f"{self}: js click")
        self.browser.execute_script(
            "arguments[0].click();", element
        )

    def move_to_element(self):
        element = self.wait_for_visible()
        Logger.info(f"{self}: get the element '{element}' into focus")
        try:
            self._actions.move_to_element(element).click().perform()
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise
