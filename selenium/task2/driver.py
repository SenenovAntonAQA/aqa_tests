from selenium.webdriver import Chrome


class Driver:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = Chrome(*args, **kwargs)
        return cls._instance

    @classmethod
    def quit(cls):
        if cls._instance:
            cls._instance.quit()
            cls._instance = None
