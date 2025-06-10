import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

url = "https://portal.trueengineering.ru/"

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get(url=url)  # открываем страницу
time.sleep(2)
driver.back() # возвращаемся назад
time.sleep(2)
driver.forward() # навигация вперед
time.sleep(1)
driver.refresh() # обновление страницы
time.sleep(1)

driver.close() # Closes the current window
driver.quit() # Closes the browser and shuts down the ChromiumDriver executable


test = 0