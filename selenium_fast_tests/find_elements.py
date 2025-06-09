import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get(url="https://auth.wikimedia.org/ruwiki/wiki/%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%92%D1%85%D0%BE%D0%B4")  # открываем страницу

time.sleep(3)

driver.find_elements('class name', 'mw-authentication-popup-link')[0].click()

time.sleep(3)

driver.close()  # Closes the current window
driver.quit()  # Closes the browser and shuts down the ChromiumDriver executable
