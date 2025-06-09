import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

url = "https://portal.trueengineering.ru/"

service = Service(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

try:
    driver.get(url=url)
    time.sleep(5)
except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
