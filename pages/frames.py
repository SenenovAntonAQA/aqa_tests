from elements.label import Label
from elements.web_element import WebElement
from pages.base_page import BasePage


class FramesPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='framesWrapper']//h1"

    DROPDOWN_FRAME_LOC = "//*[@class='header-text' and contains(text(), 'Frame')]"
    NESTED_FRAME_OPT_LOC = "//*[@class='text' and contains(text(), 'Nested')]"

    UPPER_FRAME_LOC = "//*[@id='frame1Wrapper']//iframe"
    LOWER_FRAME_LOC = "//*[@id='frame2Wrapper']//iframe"
    TEXT_IN_FRAME = "/html//*[@id='sampleHeading']"

    def __init__(self, browser):
        super().__init__(browser)
        self.name = "Frames page"

        self.unique_element = WebElement(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Frames page -> Head of the central content"
        )

        self.dropdown_frames_list = Label(
            self.browser,
            self.DROPDOWN_FRAME_LOC,
            description="Frames page -> DropDown list 'Alerts, Frame & Windows'"
        )
        self.to_nested_frame = Label(
            self.browser,
            self.NESTED_FRAME_OPT_LOC,
            description="DropDown list -> 'Nested Frames' option"
        )
        self.upper_frame = WebElement(
            self.browser,
            self.UPPER_FRAME_LOC,
            description="Frames page -> Upper frame"
        )
        self.lower_frame = WebElement(
            self.browser,
            self.LOWER_FRAME_LOC,
            description="Frames page -> Lower frame"
        )
        self.text_in_frame = WebElement(
            self.browser,
            self.TEXT_IN_FRAME,
            description="Frame -> Text in frame"
        )

    def click_to_nested_frames(self):
        nested = self.to_nested_frame
        if not nested.is_displayed():
            self.dropdown_frames_list.click()
            nested.click()
        else:
            nested.click()

    def get_text_in_frame(self) -> str:
        self.text_in_frame.wait_for_visible()
        return self.text_in_frame.get_text()


class NestedFramesPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='framesWrapper']//h1"

    PARENT_FRAME_LOC = "//iframe[@id='frame1']"
    TEXT_IN_PARENT_FRAME_LOC = "//html/body"
    CHILD_FRAME_LOC = "//html/body/iframe[contains(@srcdoc, 'Child')]"
    TEXT_IN_CHILD_FRAME_LOC = "//html//p"

    DROPDOWN_FRAME_LOC = "//*[@class='header-text' and contains(text(), 'Frame')]"
    FRAME_OPT_LOC = "//*[@class='text' and text()='Frames']"

    def __init__(self, browser):
        super().__init__(browser)
        self.name = "Nested Frames page"

        self.unique_element = WebElement(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Nested Frames page -> Head of the central content"
        )

        self.parent_frame = WebElement(
            self.browser,
            self.PARENT_FRAME_LOC,
            description="Nested Frames page -> Parent frame"
        )
        self.text_in_parent_frame = WebElement(
            self.browser,
            self.TEXT_IN_PARENT_FRAME_LOC,
            description="Parent frame -> Text in frame"
        )
        self.child_frame = WebElement(
            self.browser,
            self.CHILD_FRAME_LOC,
            description="Parent frame -> Child frame"
        )
        self.text_in_child_frame = WebElement(
            self.browser,
            self.TEXT_IN_CHILD_FRAME_LOC,
            description="Child frame -> Text in frame"
        )
        self.dropdown_frames_list = Label(
            self.browser,
            self.DROPDOWN_FRAME_LOC,
            description="Frames page -> DropDown list 'Alerts, Frame & Windows'"
        )
        self.to_frame = Label(
            self.browser,
            self.FRAME_OPT_LOC,
            description="DropDown list -> 'Frames' option"
        )

    def get_text_in_parent_frame(self) -> str:
        self.text_in_parent_frame.wait_for_visible()
        return self.text_in_parent_frame.get_text()

    def get_text_in_child_frame(self) -> str:
        self.text_in_child_frame.wait_for_visible()
        return self.text_in_child_frame.get_text()

    def click_to_frames(self):
        frames = self.to_frame
        if not frames.is_displayed():
            self.dropdown_frames_list.click()
        frames.click()
