from logger.logger import Logger
from pages.context_menu import ContextMenuPage
from pages.javascript_alert import JSAlertsPage
from utils.config_reader import ConfigReader
from faker import Faker


def alert_text_verification(alert_text, expect_text):
    assert alert_text == expect_text, (
        f"Текст алерта ({alert_text}) не соответствует {expect_text}"
    )


def check_text_in_result(actual_text, expected_text):
    assert actual_text == expected_text, (
        f"В секции 'Result' отображается некорректный текст: '{actual_text}'. "
        f"Ожидалось: '{expected_text}'"
    )


def test_2_alerts(browser):
    browser.get(ConfigReader.get("urls.alerts"))

    alert_page = JSAlertsPage(browser)
    alert_page.wait_for_open()

    Logger.info("Нажать на кнопку “Click for JS Alert“")
    alert_page.click_alert()

    expected_alert_text = "I am a JS Alert"
    alert_text_verification(
        alert_text=browser.get_alert_text(),
        expect_text=expected_alert_text
    )

    Logger.info("В Alert нажать кнопку “OK“")
    browser.accept_alert()

    expected_result_alert_text = "You successfully clicked an alert"
    check_text_in_result(
        actual_text=alert_page.get_result_text(),
        expected_text=expected_result_alert_text
    )

    Logger.info("Нажать на кнопку “Click for JS Confirm“")
    alert_page.click_confirm()

    expected_confirm_text = "I am a JS Confirm"
    alert_text_verification(
        alert_text=browser.get_alert_text(),
        expect_text=expected_confirm_text
    )

    Logger.info("В Alert нажать кнопку “OK“")
    browser.accept_alert()

    expected_result_confirm_text = "You clicked: Ok"
    check_text_in_result(
        actual_text=alert_page.get_result_text(),
        expected_text=expected_result_confirm_text
    )

    Logger.info("Нажать на кнопку “Click for JS Prompt“")
    alert_page.click_prompt()

    expected_prompt_text = "I am a JS prompt"
    alert_text_verification(
        alert_text=browser.get_alert_text(),
        expect_text=expected_prompt_text
    )

    Logger.info(
        "Ввести в поле ввода случайно сгенерированный текст. Нажать кнопку “OK“"
    )
    random_text = Faker().sentence(nb_words=2)
    browser.send_keys_alert(text=random_text)
    browser.accept_alert()

    expected_result_prompt_text = "You entered: {}"
    check_text_in_result(
        actual_text=alert_page.get_result_text(),
        expected_text=expected_result_prompt_text.format(random_text)
    )


def test_3_alerts_with_js(browser):
    browser.get(ConfigReader.get("urls.alerts"))

    alert_page = JSAlertsPage(browser)
    alert_page.wait_for_open()

    Logger.info(
        "Нажать на кнопку “Click for JS Alert“ с помощью JavaScript метода"
    )
    alert_page.click_js_alert()

    expected_alert_text = "I am a JS Alert"
    alert_text_verification(
        alert_text=browser.get_alert_text(),
        expect_text=expected_alert_text
    )

    Logger.info("В Alert нажать кнопку “OK“")
    browser.accept_alert()

    expected_result_alert_text = "You successfully clicked an alert"
    check_text_in_result(
        actual_text=alert_page.get_result_text(),
        expected_text=expected_result_alert_text
    )

    Logger.info(
        "Нажать на кнопку “Click for JS Confirm“ с помощью JavaScript метода"
    )
    alert_page.click_js_confirm()

    expected_confirm_text = "I am a JS Confirm"
    alert_text_verification(
        alert_text=browser.get_alert_text(),
        expect_text=expected_confirm_text
    )

    Logger.info("В Alert нажать кнопку “OK“")
    browser.accept_alert()

    expected_result_confirm_text = "You clicked: Ok"
    check_text_in_result(
        actual_text=alert_page.get_result_text(),
        expected_text=expected_result_confirm_text
    )

    Logger.info(
        "Нажать на кнопку “Click for JS Prompt“ с помощью JavaScript метода"
    )
    alert_page.click_js_prompt()

    expected_prompt_text = "I am a JS prompt"
    alert_text_verification(
        alert_text=browser.get_alert_text(),
        expect_text=expected_prompt_text
    )

    Logger.info(
        "Ввести в поле ввода случайно сгенерированный текст. Нажать кнопку “OK“"
    )
    random_text = Faker().sentence(nb_words=2)
    browser.send_keys_alert(text=random_text)
    browser.accept_alert()

    expected_result_prompt_text = "You entered: {}"
    check_text_in_result(
        actual_text=alert_page.get_result_text(),
        expected_text=expected_result_prompt_text.format(random_text)
    )

def test_4_alerts_context_click(browser):
    browser.get(ConfigReader.get("urls.context_menu"))

    context_menu_page = ContextMenuPage(browser)
    context_menu_page.wait_for_open()

    Logger.info("Кликнуть ПКМ на выделенную область")
    context_menu_page.right_click_box()

    expected_text = "You selected a context menu"
    alert_text_verification(
        alert_text=browser.get_alert_text(),
        expect_text=expected_text
    )

    Logger.info("В Alert нажать кнопку “OK“")
    browser.accept_alert()

    assert browser.check_close_alert(), "The alert was not closed"
