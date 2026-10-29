# lesson_ui.py

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# 1. SETUP — подготавливаем драйвер
# ChromeDriverManager().install() сам скачивает нужный chromedriver
service = Service(ChromeDriverManager().install())
driver  = webdriver.Chrome(service=service)

# 2. Управляем окном браузера

print ('open browser')
driver.get('https://the-internet.herokuapp.com/login')

driver.maximize_window()
time.sleep(3)


#search by id
print('enter id........')

username_field = driver.find_element(By.ID, 'username')
username_field.send_keys("tomsmith")
time.sleep(2)

#search by xpath
print('enter password........')
password_field = driver.find_element(By.XPATH, "//input[@id='password']")
password_field.send_keys('SuperSecretPassword!')
time.sleep(2)

#search by class
login_button = driver.find_element(By.XPATH, '//button[@class="radius"]')
login_button.click()
time.sleep(2)

# 
#  
# 3. TEARDOWN — закрываем браузер
# quit() закрывает ВЕСЬ браузер
# close() закрыл бы только одну вкладку
driver.quit()

print('it"s ready') 