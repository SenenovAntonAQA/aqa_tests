from logger.logger import Logger

from pages.hovers import HoversPage
from utils.config_reader import ConfigReader


def test_case_6_hovers(browser):
    browser.get(ConfigReader.get("urls.hovers"))

    hovers_page = HoversPage(browser)
    hovers_page.wait_for_open()

    count = hovers_page.get_count_group_users()
    for i in range(1, count + 1):
        Logger.info(f"Hover the cursor over the user # {i}")
        hovers_page.take_focus_avatar(i)

        name = hovers_page.get_user_names(i)
        exp_name = f"name: user{i}"
        assert name == exp_name, (
            f"The current '{name}' "
            f"does not match the expected '{exp_name}'"
        )

        Logger.info(f"View user profile # {i}")

        exp_url = hovers_page.get_user_links(i)
        hovers_page.click_user_link(i)

        actual_url = browser.get_current_url()

        assert actual_url == exp_url, (
            f"The current url: '{actual_url}' "
            f"does not match the expected url: '{exp_url}'"
        )

        browser.come_back()
        hovers_page.wait_for_open()

    Logger.info(f"All users have been viewed")
