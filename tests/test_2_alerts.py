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
    alert_page = JSAlertsPage(browser)

    browser.get(ConfigReader.get("urls.alerts"))

    alert_page.click_alert()
    # Нажать на кнопку “Click for JS Alert“

    expected_alert_text = "I am a JS Alert"

    alert_text_verification(
        alert_text=browser.get_alert_text(),
        expect_text=expected_alert_text
    )
    # Проверяем отображение текста алёрта "I am a JS Alert“

    browser.accept_alert()
    # В Alert нажать кнопку “OK“

    expected_result_alert_text = "You successfully clicked an alert"
    # специально некорректный текст в ОР ТК: subccessfuly -> successfully ?)))

    check_text_in_result(
        actual_text=alert_page.text_in_result(),
        expected_text=expected_result_alert_text
    )
    # Alert закрылся. В секции “Result“ отображается текст “You subccessfuly
    # clicked an alert

    alert_page.click_confirm()
    # Нажать на кнопку “Click for JS Confirm“

    expected_confirm_text = "I am a JS Confirm"
    alert_text_verification(
        alert_text=browser.get_alert_text(),
        expect_text=expected_confirm_text
    )
    # Отображается Alert с текстом “I am a JS Confirm“

    browser.accept_alert()
    # В Alert нажать кнопку “OK“

    expected_result_confirm_text = "You clicked: Ok"
    check_text_in_result(
        actual_text=alert_page.text_in_result(),
        expected_text=expected_result_confirm_text
    )
    # Alert закрылся. В секции “Result“ отображается текст “You clicked: Ok“

    alert_page.click_prompt()
    # Нажать кнопку “Click for JS Prompt“

    expected_prompt_text = "I am a JS prompt"
    # специально некорректный текст в ОР ТК: Prompt -> prompt ???))

    alert_text_verification(
        alert_text=browser.get_alert_text(),
        expect_text=expected_prompt_text
    )
    # Отображается Alert с текстом “I am a JS Prompt“

    random_text = Faker().sentence(nb_words=2)

    browser.send_keys_alert(text=random_text)
    browser.accept_alert()
    # Ввести в поле ввода случайно сгенерированный текст. Нажать кнопку “OK“.

    expected_result_prompt_text = "You entered: {}"

    check_text_in_result(
        actual_text=alert_page.text_in_result(),
        expected_text=expected_result_prompt_text.format(random_text)
    )
    # Alert закрылся. В секции “Result“ отображается текст “You entered:
    # %введенный случайно сгенерированный текст%“


def test_3_alerts_with_js(browser):
    alert_page = JSAlertsPage(browser)

    browser.get(ConfigReader.get("urls.alerts"))

    alert_page.click_js_alert()
    # Нажать на кнопку “Click for JS Alert“ с помощью вызова соответствующего
    # JavaScript метода

    expected_alert_text = "I am a JS Alert"

    alert_text_verification(
        alert_text=browser.get_alert_text(),
        expect_text=expected_alert_text
    )
    # Проверяем отображение текста алёрта "I am a JS Alert“

    browser.accept_alert()
    # В Alert нажать кнопку “OK“

    expected_result_alert_text = "You successfully clicked an alert"
    check_text_in_result(
        actual_text=alert_page.text_in_result(),
        expected_text=expected_result_alert_text
    )
    # Alert закрылся. В секции “Result“ отображается текст “You subccessfuly
    # clicked an alert

    alert_page.click_js_confirm()
    # Нажать на кнопку “Click for JS Confirm“ с помощью вызова соответствующего
    #     # JavaScript метода

    expected_confirm_text = "I am a JS Confirm"
    alert_text_verification(
        alert_text=browser.get_alert_text(),
        expect_text=expected_confirm_text
    )
    # Отображается Alert с текстом “I am a JS Confirm“

    browser.accept_alert()
    # В Alert нажать кнопку “OK“

    expected_result_confirm_text = "You clicked: Ok"
    check_text_in_result(
        actual_text=alert_page.text_in_result(),
        expected_text=expected_result_confirm_text
    )
    # Alert закрылся. В секции “Result“ отображается текст “You clicked: Ok“

    alert_page.click_js_prompt()
    # Нажать кнопку “Click for JS Prompt“ с помощью вызова соответствующего
    #     # JavaScript метода

    expected_prompt_text = "I am a JS prompt"

    alert_text_verification(
        alert_text=browser.get_alert_text(),
        expect_text=expected_prompt_text
    )
    # Отображается Alert с текстом “I am a JS Prompt“

    random_text = Faker().sentence(nb_words=2)

    browser.send_keys_alert(text=random_text)
    browser.accept_alert()
    # Ввести в поле ввода случайно сгенерированный текст. Нажать кнопку “OK“.

    expected_result_prompt_text = "You entered: {}"

    check_text_in_result(
        actual_text=alert_page.text_in_result(),
        expected_text=expected_result_prompt_text.format(random_text)
    )
    # Alert закрылся. В секции “Result“ отображается текст “You entered:
    # %введенный случайно сгенерированный текст%“