import pytest
from website.steam_main_page import SteamMainPage
from website.steam_search_page import SteamSearchPage
from tests.enums import URL, Language, Game


@pytest.mark.parametrize('game_name, N', [
    (Game.WITCHER, 10),
    (Game.FALLOUT, 20)
])
@pytest.mark.parametrize("language", [Language.RU, Language.EN])
def test_search_game(browser, game_name, N, language):
    main_page = SteamMainPage(browser)
    search_page = SteamSearchPage(browser)

    # Шаг 1: Перейти на домашнюю страницу сайта
    browser.get(URL.STEAM_TEST_URL)
    assert main_page.is_main_page_loaded(), (
        "Домашняя страница не была открыта"
    )

    # Шаг 2: Ввести в строку поиска название игры
    main_page.search_smth(game_name)
    main_page.submit_search()

    # Шаг 3: Перейти на страницу с результатами поиска
    tags = search_page.get_search_result_tags()
    tag_text = [tag.text for tag in tags]
    
    assert any(game_name.value in text for text in tag_text), (
        f"Тег поиска не соответствует {game_name}"
    )

    # Шаг 4: Установить фильтр отображения в значение “По убыванию цены”
    search_page.sort_by_price()

    # Шаг 5: Получить список из N игр
    prices = search_page.get_price_results(number=N)
    assert all(
        prices[i] >= prices[i + 1] for i in range(len(prices) - 1)
    ), "Цены не отсортированы по убыванию"
