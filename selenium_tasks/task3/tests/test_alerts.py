from selenium_tasks.task3.pages.javascript_alerts import JSAlertsPage
from selenium_tasks.task3.utils.config_reader import ConfigReader
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

    alert_page.click_js_alert()
    # Нажать на кнопку “Click for JS Alert“

    expected_alert_text = "I am a JS Alert"

    alert_text_verification(
        alert_text=alert_page.text_in_alert(),
        expect_text=expected_alert_text
    )
    # Проверяем отображение текста алёрта "I am a JS Alert“

    alert_page.alert_accept()
    # В Alert нажать кнопку “OK“

    expected_result_alert_text = "You successfully clicked an alert"
    check_text_in_result(
        actual_text=alert_page.text_in_result(),
        expected_text=expected_result_alert_text
    )
    # Alert закрылся. В секции “Result“ отображается текст “You subccessfuly
    # clicked an alert

    # специально некорректный текст в ОР ТК: subccessfuly -> successfully ?)))

    alert_page.click_js_confirm()
    # Нажать на кнопку “Click for JS Confirm“

    expected_confirm_text = "I am a JS Confirm"
    alert_text_verification(
        alert_text=alert_page.text_in_alert(),
        expect_text=expected_confirm_text
    )
    # Отображается Alert с текстом “I am a JS Confirm“

    alert_page.alert_accept()
    # В Alert нажать кнопку “OK“

    expected_result_confirm_text = "You clicked: Ok"
    check_text_in_result(
        actual_text=alert_page.text_in_result(),
        expected_text=expected_result_confirm_text
    )
    # Alert закрылся. В секции “Result“ отображается текст “You clicked: Ok“

    alert_page.click_js_prompt()
    # Нажать кнопку “Click for JS Prompt“

    expected_prompt_text = "I am a JS prompt"
    # специально некорректный текст в ОР ТК: Prompt -> prompt ???))

    alert_text_verification(
        alert_text=alert_page.text_in_alert(),
        expect_text=expected_prompt_text
    )
    # Отображается Alert с текстом “I am a JS Prompt“

    random_text = Faker().sentence(nb_words=2)

    alert_page.send_text_to_alert(text=random_text)
    alert_page.alert_accept()
    # Ввести в поле ввода случайно сгенерированный текст. Нажать кнопку “OK“.

    expected_result_prompt_text = "You entered: {}"

    check_text_in_result(
        actual_text=alert_page.text_in_result(),
        expected_text=expected_result_prompt_text.format(random_text)
    )
    # Alert закрылся. В секции “Result“ отображается текст “You entered:
    # %введенный случайно сгенерированный текст%“
