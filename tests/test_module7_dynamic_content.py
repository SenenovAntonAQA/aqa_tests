from pages.dynamic_content import DynamicContentPage
from utils.config_reader import ConfigReader

def comparing_values(lst: list) -> bool:
    return lst[0] == lst[1] or lst[0] == lst[2] or lst[1] == lst[2]

def test_case_9_dynamic_content(browser):
    browser.get(ConfigReader.get("urls.dynamic_content"))

    dynamic_content = DynamicContentPage(browser)
    dynamic_content.wait_for_open()

    while True:
        avatars = dynamic_content.get_all_avatars()

        if not comparing_values(avatars):
            browser.refresh()
            dynamic_content.wait_for_open()
        else:
            break

    browser.save_screenshot("screenshot_test_case_9.png")