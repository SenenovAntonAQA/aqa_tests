import sys
import pytest

if sys.platform == "linux":
    pytest.skip("Тесты upload не выполняются на Linux", allow_module_level=True)

from pathlib import Path
from pages.upload import UploadPage, UploadedPage
from utils.config_reader import ConfigReader
from utils.pyautogui_utils import PyAutoGUIUtilities


def verify_text(actual, expected):
    assert actual == expected, (
        f"The current text on page '{actual}' "
        f"does not match the expected '{expected}'"
    )


def verify_mark(actual_mark):
    assert actual_mark == '✔', (
        f"The current mark on page '{actual_mark}' "
        f"does not match the expected '✔'"
    )


def test_case_11_upload_image(browser):
    image = "screenshot_test_case_9.png"
    image_path = (Path(__file__).parent / image).resolve()

    browser.get(ConfigReader.get("urls.upload"))

    load_page = UploadPage(browser)
    load_page.wait_for_open()

    load_page.send_file(str(image_path))

    load_page.start_load_file()

    uploaded_page = UploadedPage(browser)

    uploaded_page.wait_for_open()

    verify_text(
        actual=uploaded_page.get_load_result(),
        expected="File Uploaded!"
    )

    verify_text(
        actual=uploaded_page.get_upload_file_name(),
        expected=image
    )


def test_case_12_dialog_window(browser):
    image = "screenshot_test_case_9.png"
    image_path = (Path(__file__).parent / image).resolve()

    browser.get(ConfigReader.get("urls.upload"))

    load_page = UploadPage(browser)
    load_page.wait_for_open()

    load_page.click_to_dnd_field()
    PyAutoGUIUtilities.upload_file(str(image_path))

    verify_text(
        actual=load_page.get_text_on_dnd_field(),
        expected=image
    )

    verify_mark(
        actual_mark=load_page.get_mark_on_dnd_field()
    )


def test_case_13_drag_n_drop(browser):
    image = "screenshot_test_case_9.png"
    image_path = Path(__file__).parent

    browser.get(ConfigReader.get("urls.upload"))

    load_page = UploadPage(browser)
    load_page.wait_for_open()

    PyAutoGUIUtilities.drag_and_drop_from_explorer(
        file_path=str(image_path)
    )

    verify_text(
        actual=load_page.get_text_on_dnd_field(),
        expected=image
    )

    verify_mark(
        actual_mark=load_page.get_mark_on_dnd_field()
    )
