from logger.logger import Logger
from pages.frames import FramesPage, NestedFramesPage
from utils.config_reader import ConfigReader


def verify_frame_text(act, exp):
    assert act == exp, (
        f"The current text on frame '{act}' "
        f"does not match the expected '{exp}'"
    )

def test_case_8_work_with_frames(browser):
    Logger.info(
        "# Step 1: Перейти на главную страницу 'https://demoqa.com/frames'"
    )
    browser.get(ConfigReader.get("urls.frames"))

    frames_page = FramesPage(browser)
    frames_page.wait_for_open()

    upper_frame = frames_page.upper_frame
    lower_frame = frames_page.lower_frame

    Logger.info(
        "# Step 2: Кликнуть на кнопку Alerts, Frame & Windows. На открывшейся "
                "странице в левом меню кликнуть пункт Nested Frames"
    )
    frames_page.click_to_nested_frames()

    nested_page = NestedFramesPage(browser)
    nested_page.wait_for_open()

    parent_frame = nested_page.parent_frame
    child_frame = nested_page.child_frame

    browser.switch_to_frame(frame=parent_frame)

    text_parent_frame = nested_page.get_text_in_frame(is_parent=True)
    verify_frame_text(text_parent_frame, "Parent frame")

    browser.switch_to_frame(frame=child_frame)

    text_child_frame = nested_page.get_text_in_frame(is_parent=False)
    verify_frame_text(text_child_frame, "Child Iframe")

    browser.switch_to_default_frame()

    Logger.info("# Step 3: В левом меню выбрать пункт Frames")
    nested_page.click_to_frames()
    frames_page.wait_for_open()

    browser.switch_to_frame(frame=upper_frame)
    text_upper_frame = nested_page.get_text_in_frame()

    browser.switch_to_default_frame()

    browser.switch_to_frame(frame=lower_frame)
    text_lower_frame = nested_page.get_text_in_frame()

    assert text_upper_frame == text_lower_frame, (
        f"Надпись из верхнего фрейма '{text_upper_frame}' "
        f"не метчится с нижним фреймом '{text_lower_frame}'"
    )