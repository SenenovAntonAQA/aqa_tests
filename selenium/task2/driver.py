from selenium.webdriver import Chrome

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Driver(metaclass=Singleton):
    def __init__(self, *args, **kwargs):
        self.driver = Chrome(*args, **kwargs)  # Создаём экземпляр Chrome внутри Driver

    def __getattr__(self, name):
        """Делегируем вызовы методов к драйверу Chrome"""
        return getattr(self.driver, name)