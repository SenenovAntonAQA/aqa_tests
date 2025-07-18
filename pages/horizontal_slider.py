from strenum import StrEnum

from elements.input import Input
from elements.web_element import WebElement
from .base_page import BasePage


class MovingDirection(StrEnum):
    LEFT = "left"
    RIGHT = "right"


class HorizontalSliderPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//input[@type='range']"

    SLIDER_INPUT_LOC = "//input[@type='range']"
    RANGE_COUNTER_LOC = "range"

    def __init__(self, browser):
        super().__init__(browser)
        self.name = "Horizontal Slider Page"

        self.unique_element = Input(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Horizontal Slider Page -> Slider"
        )

        self.slider = Input(
            self.browser,
            self.SLIDER_INPUT_LOC,
            description="Horizontal Slider Page -> Slider"
        )

        self.counter = WebElement(
            self.browser,
            self.RANGE_COUNTER_LOC,
            description="Horizontal Slider Page -> Range Counter"
        )

    def get_range_counter(self):
        return self.counter.get_text()

    def take_slider_to_focus(self):
        self.slider.move_to_element()

    def set_slider_precise(self, value, type: MovingDirection):
        if type == MovingDirection.RIGHT:
            self.slider.move_to_right(value)
        else:
            self.slider.move_to_left(value)

    def get_slider_min(self):
        return float(self.slider.get_attribute("min"))

    def get_slider_max(self):
        return float(self.slider.get_attribute("max"))

    def get_slider_step(self):
        return float(self.slider.get_attribute("step"))