import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get(url="https://www.wikipedia.org/")  # открываем страницу

# url = driver.current_url
# print(f'URL старницы {url}')
# assert url == "https://www.wikipedia.org/", "Ошибка в url"
#
# current_title = driver.title
# print(f'Текущий заголовок: {current_title}')
# assert current_title == 'Wikipedia', 'Некорректный заголовок страницы'

print(driver.page_source) # забираем исходный код html-страницы

driver.close() # Closes the current window
driver.quit() # Closes the browser and shuts down the ChromiumDriver executable
