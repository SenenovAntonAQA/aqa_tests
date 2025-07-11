import random

from logger.logger import Logger
from pages.horizontal_slider import HorizontalSliderPage, MovingDirection
from utils.config_reader import ConfigReader


def get_random_value(start: int = 1, stop: int = 5):
    value = random.randrange(
        start=start,
        stop=stop
    )
    return value


def test_case_5_move_slider(browser):
    browser.get(ConfigReader.get("urls.horizontal_slider"))

    horizontal_slider = HorizontalSliderPage(browser)
    horizontal_slider.wait_for_open()

    Logger.info(
        "Установить случайное значение слайдера (отличное от граничных):"
    )

    horizontal_slider.take_slider_to_focus()

    value_to_right = get_random_value()
    horizontal_slider.set_slider_precise(value_to_right, MovingDirection.RIGHT)

    value_to_left = get_random_value(stop=4 + value_to_right)
    horizontal_slider.set_slider_precise(value_to_left, MovingDirection.LEFT)

    actual_value = 2.5 + 0.5 * (value_to_right - value_to_left)
    range_counter = float(horizontal_slider.get_range_counter())

    assert actual_value == range_counter, (
        f"Счётчик слайдера: {range_counter}, когда сдвиг был: {actual_value}"
    )
