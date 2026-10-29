# lesson_ui.py

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 1. SETUP — подготавливаем драйвер
# ChromeDriverManager().install() сам скачивает нужный chromedriver
service = Service(ChromeDriverManager().install())
driver  = webdriver.Chrome(service=service)

# 2. Управляем окном браузера

print ('open browser')
driver.get('https://google.com')

driver.maximize_window()
time.sleep(3)

print ('links on wiki')
driver.get('https://wikipedia.org')
time.sleep(3)

print('comin back ')
driver.back()
time.sleep(3)

print('update site')
driver.refresh()

# 3. TEARDOWN — закрываем браузер
# quit() закрывает ВЕСЬ браузер
# close() закрыл бы только одну вкладку
driver.quit()

print('it"s ready')