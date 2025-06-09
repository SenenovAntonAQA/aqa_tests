import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

url = "https://portal.trueengineering.ru/"

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get(url=url)
    time.sleep(5)
except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
