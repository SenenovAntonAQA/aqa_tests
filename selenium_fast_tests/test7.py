from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
wait = WebDriverWait(driver=browser, timeout=15, poll_frequency=1)

browser.get("https://the-internet.herokuapp.com/dynamic_controls")

# REMOVE_BUT = (By.XPATH, "//button[text()='Remove']")
#
# browser.find_element(*REMOVE_BUT).click()
#
# wait.until(EC.invisibility_of_element_located(REMOVE_BUT))
#
# print("Кнопка исчезла")

ENABLE_BUT = (By.XPATH, "//button[text()='Enable']")
TEXT_FIELD = (By.XPATH, "//form[@id='input-example']/input[@type='text']")

wait.until(EC.element_to_be_clickable(ENABLE_BUT)).click()
wait.until(EC.element_to_be_clickable(TEXT_FIELD)).send_keys("Hello")

wait.until(EC.text_to_be_present_in_element_value(TEXT_FIELD, text_="Hello"))

print('Всё ок')