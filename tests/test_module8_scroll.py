import pytest

from pages.infinity_scroll import InfinityScrollPage
from utils.config_reader import ConfigReader


@pytest.mark.parametrize("age", [28])
def test_case_10_scroll_to_paragraph(browser, age):
    browser.get(ConfigReader.get("urls.infinity_scroll"))

    scroll_page = InfinityScrollPage(browser)
    scroll_page.wait_for_open()

    while True:
        x = scroll_page.count_paragraph()
        if age <= x:
            break
        scroll_page.scroll_to_page_down(x)
