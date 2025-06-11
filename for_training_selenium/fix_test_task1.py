import pytest
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker


# service = Service(executable_path=ChromeDriverManager().install())
# А если вообще не указывать путь - работает? Последние версии селениума вроде сами умеют устанавливать chromedriver и искать если уже установлен

@pytest.fixture(scope="session", autouse=True)
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
    # А что будет, если close вызвать при наличии одной вкладки? Почитай про разницу close с одной вкладкой и quit
    # Это нужно строго делать в фикстуре. Если тест упадет, то очистка не выполнится


@pytest.fixture
def fake_username():
    return Faker().user_name()


@pytest.fixture
def fake_password():
    return Faker().password(length=10, special_chars=True, digits=True, upper_case=True)


# Тестовые данные лучше генерировать на лету (для этого можешь воспользоваться faker, там есть отдельные методы для username и password)
# Тем самым ты бесплатно повышаешь тестовое покрытие прилжения

def test_try_login_to_steam(driver, fake_username, fake_password):
    # Как правило код теста объединяют в тестовые функции. Сейчас оно просто в модуле, я не уверен что pytest такое умеет запускать вообще
    URL_STEAM = "https://store.steampowered.com/"
    # Это константа, стоит именовать большими буквами

    LOGIN_HREF = (By.XPATH, "//a[contains(@class, 'global_action_link')]")

    USERNAME = (By.XPATH, "//input[@type='text']")  # поле ввода имени аккаунта
    PASS = (By.XPATH, "//input[@type='password']")  # поле ввода пароля
    SUBMIT_BUT = (By.XPATH, "//button[@type='submit']")  # кнопка войти

    WRONG_CREDENTIALS = (By.XPATH, "//form//div[contains(text(), 'проверьте')]")
    # А может хотя бы часть локатора получится написать получше?

    # Локаторы лучше вынести в виде констант повыше, чтобы легко их находить и исправлять
    # "xpath" уже есть константа для этого в selenium - By.XPATH, хардкодить строку не стоит. Мало ли оно поменяется, мало ли ты опечатаешься

    wait = WebDriverWait(driver, timeout=10, poll_frequency=1)

    driver.get(url=URL_STEAM)
    # Настройку драйвера, переход по ссылке и его закрытие нужно будет в фикстуре. Изучи, что это такое, ее скоупы и зачем они нужны
    # Можешь дополнительно изучить conftest.py ну или оставить это уже на следующее задание

    wait.until(EC.presence_of_element_located(LOGIN_HREF)).click()

    # А где ожидание открытия страницы?
    # А find_element точно подходит для клика? Какое условие он ждет?
    # А нормально ли он работает, если у тебя implicit wait нигде не устанавливается? Тогда он по умолчанию равен нулю (мы не ждем элементы, а моментально они не появляются)

    wait.until(EC.element_to_be_clickable(USERNAME)).send_keys(fake_username)
    # вводим текст в поле ввода

    wait.until(EC.element_to_be_clickable(PASS)).send_keys(fake_password)
    # вводим пароль

    wait.until(EC.element_to_be_clickable(SUBMIT_BUT)).click()
    # нажимаем на Войти

    assert wait.until(EC.visibility_of_element_located(WRONG_CREDENTIALS)).text == "Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова.", "Текст при ошибочных кредах после клика на 'Войти' не соответствует ТЗ"
    # assert message должен содержать actual & expected result, чтобы было легко по ошибке понять что пошло не так и сократить время на исследование падений