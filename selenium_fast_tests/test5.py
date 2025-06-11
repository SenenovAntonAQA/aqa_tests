from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("https://demoqa.com/dynamic-properties")
browser.implicitly_wait(5)

browser.find_element(By.XPATH, "//*[@id='visibleAfter']").click()

browser.refresh()
browser.find_element(By.XPATH, "//*[@id='visibleAfter']").click()