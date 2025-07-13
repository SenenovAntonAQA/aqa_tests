from pages.infinity_scroll import InfinityScrollPage
from utils.config_reader import ConfigReader


def test_case_10_scroll_to_paragraph(browser):
    QA_AGE = 28

    browser.get(ConfigReader.get("urls.infinity_scroll"))

    scroll_page = InfinityScrollPage(browser)
    scroll_page.wait_for_open()

    while not scroll_page.verify_element_number(QA_AGE):
        scroll_page.scroll_to_last_par()
