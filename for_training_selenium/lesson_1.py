import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get(url="https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")

time.sleep(1)

login_href = driver.find_element("xpath", "//*[@id='pt-login']/a") # нашли ссылку для авторизации
login_href.click()

time.sleep(1)

username_input = driver.find_element("xpath", "//*[@id='wpName1']") # нашли поле ввода

time.sleep(1)

username_input.send_keys("testUsername@gmail.com") # вводим текст в поле ввода
print(username_input.get_attribute("value")) # найти то, что ввели в поле ввода

time.sleep(2)

username_input.clear() # очистить поле ввода
username_input.send_keys("aaaaaa")

time.sleep(1)


driver.close() # Closes the current window
driver.quit() # Closes the browser and shuts down the ChromiumDriver executable
