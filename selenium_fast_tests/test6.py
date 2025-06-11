from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
wait = WebDriverWait(driver=browser, timeout=15, poll_frequency=1)
# создаём объект wait, который будет отвечать за явные ожидания. Он будет экземпляром WebDriverWait

VISIBLE_AFTER_BUT = (By.XPATH, "//*[@id='visibleAfter']")

ENABLE_BUT = (By.XPATH, "/*[@id='enableAfter']")

browser.get("https://demoqa.com/dynamic-properties")

# BUTTON = wait.until(EC.visibility_of_element_located(VISIBLE_AFTER_BUT))
# BUTTON.click()

wait.until(EC.element_to_be_clickable(ENABLE_BUT)).click()