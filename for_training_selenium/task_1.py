import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url_steam = 'https://store.steampowered.com/'

driver.get(url=url_steam)

time.sleep(1)

login_href = driver.find_element("xpath", "//a[contains(@class, 'global_action_link')]") # кнопка для открытия страницы авторизации
login_href.click()

time.sleep(1)

username_input = driver.find_element("xpath", "//input[@type='text']") # нашли поле ввода имени аккаунта
username_input.send_keys("usernameForSteamTest") # вводим текст в поле ввода

time.sleep(2)

pass_input = driver.find_element("xpath", "//input[@type='password']") # нашли поле ввода пароля
pass_input.send_keys("QWE123asd!@#") # вводим пароль

time.sleep(2)

button_submit = driver.find_element("xpath", "//button[@type='submit']") # ищем кнопку войти
button_submit.click() # нажимаем на неё

time.sleep(2)

wrong_login_or_pass = driver.find_element("xpath", "//form//div[5]")

assert wrong_login_or_pass.text == "Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова.", "Некорректный текст ошибки"

time.sleep(2)

driver.close() # Closes the current window
driver.quit() # Closes the browser and shuts down the ChromiumDriver executable
