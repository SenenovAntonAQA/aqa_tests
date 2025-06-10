import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
# А если вообще не указывать путь - работает? Последние версии селениума вроде сами умеют устанавливать chromedriver и искать если уже установлен
driver = webdriver.Chrome(service=service)

URL = 'https://store.steampowered.com/'
# Это константа, стоит именовать большими буквами

driver.get(url=URL)
# Настройку драйвера, переход по ссылке и его закрытие нужно будет в фикстуре. Изучи, что это такое, ее скоупы и зачем они нужны
# Можешь дополнительно изучить conftest.py ну или оставить это уже на следующее задание

login_href = driver.find_element("xpath", "//a[contains(@class, 'global_action_link')]") # кнопка для открытия страницы авторизации
# А где ожидание открытия страницы?
# А find_element точно подходит для клика? Какое условие он ждет?
# А нормально ли он работает, если у тебя implicit wait нигде не устанавливается? Тогда он по умолчанию равен нулю (мы не ждем элементы, а моментально они не появляются)

# Локаторы лучше вынести в виде констант повыше, чтобы легко их находить и исправлять
# "xpath" уже есть константа для этого в selenium - By.XPATH, хардкодить строку не стоит. Мало ли оно поменяется, мало ли ты опечатаешься
login_href.click()

username_input = driver.find_element("xpath", "//input[@type='text']") # нашли поле ввода имени аккаунта
username_input.send_keys("usernameForSteamTest") # вводим текст в поле ввода
# Тестовые данные лучше генерировать на лету (для этого можешь воспользоваться faker, там есть отдельные методы для username и password)
# Тем самым ты бесплатно повышаешь тестовое покрытие прилжения

pass_input = driver.find_element("xpath", "//input[@type='password']") # нашли поле ввода пароля
pass_input.send_keys("QWE123asd!@#") # вводим пароль

button_submit = driver.find_element("xpath", "//button[@type='submit']") # ищем кнопку войти
button_submit.click() # нажимаем на неё

wrong_login_or_pass = driver.find_element("xpath", "//form//div[5]")
# А может хотя бы часть локатора получится написать получше?

assert wrong_login_or_pass.text == "Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова.", "Некорректный текст ошибки"
# assert message должен содержать actual & expected result, чтобы было легко по ошибке понять что пошло не так и сократить время на исследование падений

driver.close() # Closes the current window
# А что будет, если close вызвать при наличии одной вкладки? Почитай про разницу close с одной вкладкой и quit
driver.quit() # Closes the browser and shuts down the ChromiumDriver executable
# Это нужно строго делать в фикстуре. Если тест упадет, то очистка не выполнится

# Как правило код теста объединяют в тестовые функции. Сейчас оно просто в модуле, я не уверен что pytest такое умеет запускать вообще