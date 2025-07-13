import time
from logger.logger import Logger

import pyautogui

class PyAutoGUIUtilities:
    @staticmethod
    def upload_file(file_path: str) -> None:
        Logger.info("Handle File Dialog for uploading file")
        time.sleep(2)

        Logger.debug(f"Write '{file_path}' to search File Dialog field")
        pyautogui.typewrite(file_path)

        Logger.debug("Press enter")
        pyautogui.hotkey("enter")

        time.sleep(2)