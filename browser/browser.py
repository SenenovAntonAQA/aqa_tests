import os
import time
from datetime import datetime
import json

from selenium.common import WebDriverException, NoAlertPresentException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from elements.base_element import BaseElement
from logger.logger import Logger


class Browser:
    DEFAULT_TIMEOUT = 10  # Стандартное время ожидания элементов
    PAGE_LOAD_TIMEOUT = 120  # Максимальное время загрузки страницы

    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._driver.set_page_load_timeout(self.PAGE_LOAD_TIMEOUT)

        self.main_handle = None

        self._wait = WebDriverWait(self._driver, timeout=self.DEFAULT_TIMEOUT)
        self._actions = ActionChains(self._driver)

    @property
    def driver(self) -> WebDriver:
        return self._driver

    def get(self, url: str) -> None:
        Logger.info(f"{self}: get '{url}'")
        try:
            self._driver.get(url)
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise
        self.main_handle = self._driver.current_window_handle

    def quit(self) -> None:
        Logger.info(f"{self}: quit")
        try:
            self._driver.quit()
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def close(self) -> None:
        if self.check_count_handles() == 1:
            Logger.info(f"{self}: last window closing, quitting browser")
            self.quit()
        else:
            Logger.info(
                f"{self}: close window handle ="
                f" '{self._driver.current_window_handle}'"
            )
            self._driver.close()

    def check_count_handles(self) -> int:
        count = len(self._driver.window_handles)
        Logger.info(f"{self}: count handles = {count}")
        return count

    def execute_script(self, script: str, *args) -> None:
        Logger.info(f"{self}: execute script = '{script}' with args = '{args}'")
        try:
            self._driver.execute_script(script, *args)
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def refresh(self) -> None:
        Logger.info(f"{self}: refresh window handle")
        try:
            self._driver.refresh()
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def save_screenshot(self, filename: str) -> None:
        Logger.info(f"{self}: save screenshot in {filename}")
        self._driver.save_screenshot(filename=filename)

    def switch_to_default_window(self) -> None:
        Logger.info(f"{self}: switch to default window")
        try:
            self._driver.switch_to.window(self.main_handle)
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def switch_to_new_window(self):
        Logger.info(f"{self}: switch to new window after open")
        try:
            for handle in self._driver.window_handles:
                if handle != self.main_handle:
                    self._driver.switch_to.window(handle)
                    return
        except WebDriverException as err:
            Logger.error(f"{self}: failed to switch to new window - {err}")
            raise

    def switch_to_window(self, title: str) -> None:
        Logger.info(f"{self} switch to window with title '{title}'")
        end_time = time.time() + self.PAGE_LOAD_TIMEOUT

        while True:
            handles = self._driver.window_handles
            for handle in handles:
                self._driver.switch_to.window(handle)
                if self._driver.title == title:
                    Logger.info(
                        f"{self}: new window handle ="
                        f" '{self._driver.current_window_handle}'"
                    )
                    return
                if time.time() < end_time:
                    time.sleep(1)  # try again in 1 sec
                else:
                    Logger.error(
                        f"{self}: window with title '{title}' wasn't found"
                    )
                    raise ValueError(
                        f"{self}: window with title '{title}' wasn't found"
                    )

    def wait_alert_present(self):
        Logger.info(f"{self}: wait alert present")
        return self._wait.until(EC.alert_is_present())

    def switch_to_alert(self):
        Logger.info(f"{self}: switch to alert")
        self.wait_alert_present()
        return self._driver.switch_to.alert

    def check_close_alert(self) -> bool:
        Logger.info(f"{self}: check close alert")
        try:
            self._driver.switch_to.alert
            return False
        except NoAlertPresentException:
            return True

    def get_alert_text(self):
        Logger.info(f"{self}: get alert text")
        return self.switch_to_alert().text

    def accept_alert(self):
        Logger.info(f"{self}: accept alert")
        return self.switch_to_alert().accept()

    def dismiss_alert(self):
        Logger.info(f"{self}: dismiss alert")
        return self.switch_to_alert().dismiss()

    def send_keys_alert(self, text: str):
        Logger.info(f"{self}: send '{text}' to alert")
        return self.switch_to_alert().send_keys(text)

    def switch_to_frame(self, frame: BaseElement):
        Logger.info(f"{self}: switch to frame '{frame}'")
        return self._driver.switch_to.frame(frame.wait_for_presence())

    def switch_to_default_frame(self):
        Logger.info(f"{self}: switch witch focus to the default frame")
        return self._driver.switch_to.default_content()

    def make_dump(self, prefix: str = "dump") -> str:
        timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        dump_dir = f"{prefix}_{timestamp}"
        os.makedirs(dump_dir, exist_ok=True)

        try:
            screenshot_path = os.path.join(dump_dir, "screenshot.png")
            self.save_screenshot(screenshot_path)

            tabs_info = {
                "current_url": self._driver.current_url,
                "current_title": self._driver.title,
                "window_handles": self._driver.window_handles,
                "current_window_handle": self._driver.current_window_handle,
                "main_handle": self.main_handle
            }

            tabs_path = os.path.join(dump_dir, "tabs_info.txt")
            with open(tabs_path, "w") as file:
                json.dump(tabs_info, file, indent=2)

            Logger.info(f"{self}: created dump in dir '{dump_dir}'")

        except WebDriverException as err:
            Logger.error(f"{self}: failed to create dump - {err}")
            raise

        return dump_dir

    def get_current_url(self) -> str:
        url = self._driver.current_url
        Logger.info(f"{self}: current url on this page: '{url}'")
        return url

    def come_back(self):
        Logger.info(f"{self}: goes one step backward in the browser history")
        self._driver.back()

    def __str__(self) -> str:
        return f"{self.__class__.__name__}[{self._driver.session_id}]"

    def __repr__(self) -> str:
        return str(self)
