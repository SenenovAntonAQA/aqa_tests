from elements.button import Button
from elements.input import Input
from elements.web_element import WebElement
from .base_page import BasePage


class UploadedPage(BasePage):
    UNIQUE_ELEMENT_LOC = "uploaded-files"

    LOAD_RESULT_TEXT_LOC = "//*[@id='content']//h3"
    PANEL_WITH_RESULT = "uploaded-files"

    def __init__(self, browser):
        super().__init__(browser)
        self.name = "File Uploaded"

        self.unique_element = WebElement(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="File Uploaded -> Upload button"
        )

        self.result_text = WebElement(
            self.browser,
            self.LOAD_RESULT_TEXT_LOC,
            description="File Uploaded -> Result load text"
        )
        self.result = WebElement(
            self.browser,
            self.PANEL_WITH_RESULT,
            description="File Uploaded -> Uploaded files"
        )

    def get_load_result(self) -> str:
        self.result_text.wait_for_visible()
        return self.result_text.get_text()

    def get_upload_file_name(self) -> str:
        self.result.wait_for_visible()
        return self.result.get_text()


class UploadPage(BasePage):
    UNIQUE_ELEMENT_LOC = "file-submit"

    UPLOAD_FILE_FIELD_LOC = "file-upload"
    SUBMIT_BUTTON_LOC = "file-submit"

    DRAG_N_DROP_FIELD_LOC = "drag-drop-upload"
    PREVIEW_UPLOAD_FILE_NAME_LOC = "//*[@class='dz-filename']//span"
    SUCCESS_MARK_LOC = "//*[@class='dz-success-mark']//span"

    def __init__(self, browser):
        super().__init__(browser)
        self.name = "File Uploader"

        self.unique_element = WebElement(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="File Uploader -> Upload button"
        )

        self.select_file = Input(
            self.browser,
            self.UPLOAD_FILE_FIELD_LOC,
            description="File Uploader -> Input for chose file"
        )
        self.upload_button = Button(
            self.browser,
            self.SUBMIT_BUTTON_LOC,
            description="File Uploader -> Button 'Upload'"
        )
        self.drag_n_drop = WebElement(
            self.browser,
            self.DRAG_N_DROP_FIELD_LOC,
            description="File Uploader -> Drag & Drop field"
        )
        self.text_in_drag_n_drop = WebElement(
            self.browser,
            self.PREVIEW_UPLOAD_FILE_NAME_LOC,
            description="Drag & Drop -> File name"
        )
        self.success_mark = WebElement(
            self.browser,
            self.SUCCESS_MARK_LOC,
            description="Drag & Drop -> Success mark"
        )

    def send_file(self, file_path):
        self.select_file.wait_for_visible()
        self.select_file.send_keys(file_path)

    def start_load_file(self):
        self.upload_button.wait_for_clickable()
        self.upload_button.click()

    def click_to_dnd_field(self) -> None:
        self.drag_n_drop.wait_for_visible()
        self.drag_n_drop.click()

    def get_text_on_dnd_field(self) -> str:
        self.text_in_drag_n_drop.wait_for_visible()
        return self.text_in_drag_n_drop.get_text()

    def get_mark_on_dnd_field(self) -> str:
        self.success_mark.wait_for_visible()
        return self.success_mark.get_text()
