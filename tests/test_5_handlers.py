from logger.logger import Logger
from pages.windows import WindowsPage, NewWindowPage
from utils.config_reader import ConfigReader

def verify_text_on_window(actual, expected):
    assert actual == expected, (
        f"The current text on page '{actual}' "
        f"does not match the expected '{expected}'"
    )

def test_7_open_and_close_handlers(browser):
    browser.get(ConfigReader.get("urls.windows"))

    window_page = WindowsPage(browser)
    window_page.wait_for_open()

    Logger.info("# 1: Clicking link to open first new window")
    window_page.open_new_window()

    browser.switch_to_new_window()

    first_window_page = NewWindowPage(browser)
    first_window_page.wait_for_open()

    text_window_1 = first_window_page.get_text_new_page()
    verify_text_on_window(text_window_1, "New Window")

    Logger.info("# 2: Return to main window")
    browser.switch_to_default_window()
    window_page.wait_for_open()

    Logger.info("# 3: Clicking link to open second new window")
    window_page.open_new_window()

    browser.switch_to_new_window()

    second_window_page = NewWindowPage(browser)
    second_window_page.wait_for_open()

    text_window_2 = second_window_page.get_text_new_page()
    verify_text_on_window(text_window_2, "New Window")

    Logger.info("# 4: Return to main window")
    browser.switch_to_default_window()
    window_page.wait_for_open()

    Logger.info("# 5: Close handle from # 1 step")
    browser.switch_to_window(title='New Window')
    browser.close()

    Logger.info("# 6: Close handle from # 3 step")
    browser.switch_to_window(title='New Window')
    browser.close()