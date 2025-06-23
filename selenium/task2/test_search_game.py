import pytest
from website.steam_main_page import SteamMainPage
from website.steam_search_page import SteamSearchPage
from selenium.webdriver.chrome.options import Options


@pytest.mark.parametrize('name_game, N', [
    ('The Witcher', 10),
    ('Fallout', 20)
])
@pytest.mark.parametrize("language", ["ru", "en"])
def test_search_game(browser, name_game, N, language):
    # Устанавливаем язык для текущего теста
    options = Options()
    options.add_argument(f"--lang={language}")
    browser.driver.options = options

    main_page = SteamMainPage(browser.driver)
    search_page = SteamSearchPage(browser.driver)

    # Шаг 1: Открыть главную страницу
    main_page.open()
    assert main_page.verify_open(lang=language), ('Локализация не соответствует '
                                               'выставленной в браузере')

    # Шаг 2: Поиск игры
    main_page.search_smth(name_game)
    main_page.search_tap_enter()

    # Шаг 3: Проверка страницы результатов
    assert search_page.verify_search(name_game), ("Тег поиска не "
                                                  f"соответствует {
                                                  name_game}")

    # Шаг 4: Сортировка по убыванию цены
    search_page.sort_by_price(direction='DESC')

    # Шаг 5: Проверка цен
    prices = search_page.get_price_results(number=N)
    assert search_page.verify_price_desc(prices), ("Цены не отсортированы"
                                                   " по убыванию")
