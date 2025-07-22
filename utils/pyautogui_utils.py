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

    @staticmethod
    def drag_and_drop_from_explorer(file_path: str) -> None:
        Logger.debug("Open win explorer max size")
        pyautogui.hotkey('winleft', 'e')
        time.sleep(2)
        pyautogui.hotkey('winleft', 'up')
        time.sleep(1)
        pyautogui.hotkey('winleft', 'right')
        time.sleep(1)

        Logger.debug(f"Navigate to folder: {file_path}")
        pyautogui.hotkey('f4')
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('backspace')
        time.sleep(1)
        pyautogui.write(file_path)
        pyautogui.press('enter')
        time.sleep(1)

        Logger.debug(f"Select file")
        pyautogui.click(1350, 305)
        time.sleep(0.5)

        Logger.debug(f"Drag and drop file to drop area")
        pyautogui.mouseDown()
        time.sleep(0.5)
        pyautogui.moveTo(750, 410, 2)
        pyautogui.mouseUp()

        Logger.info(f"Wait to load")
        time.sleep(1)
