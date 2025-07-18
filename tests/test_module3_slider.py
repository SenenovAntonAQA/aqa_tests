from utils.random_utils import RandomUtils

from logger.logger import Logger
from pages.horizontal_slider import HorizontalSliderPage, MovingDirection
from utils.config_reader import ConfigReader


def test_case_5_move_slider(browser):
    browser.get(ConfigReader.get("urls.horizontal_slider"))
    horizontal_slider = HorizontalSliderPage(browser)
    horizontal_slider.wait_for_open()

    min_val = horizontal_slider.get_slider_min()
    max_val = horizontal_slider.get_slider_max()
    step = horizontal_slider.get_slider_step()

    target = RandomUtils.get_random_value_in_range(
        min_val=min_val + step,
        max_val=max_val - step,
        step=step
    )

    Logger.info(
        f"### Устанавливаем значение слайдера: {target}"
    )

    horizontal_slider.take_slider_to_focus()
    current = float(horizontal_slider.get_range_counter())

    direction = MovingDirection.RIGHT if current < target else MovingDirection.LEFT
    horizontal_slider.set_slider_precise(
        value=int(abs(current - target) / step),
        type=direction
    )

    actual_value = float(horizontal_slider.get_range_counter())

    assert actual_value == target, (
        f"Ожидаемое значение: {target}, Фактическое: {actual_value}"
    )
