import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait          # ← НОВОЕ
from selenium.webdriver.support import expected_conditions as EC # ← НОВОЕ

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://practicetestautomation.com/practice-test-login/")

#створюється об'єкт очікування чекати максимум 10 с.
wait = WebDriverWait(driver, 10)

header = wait.until(EC.visibility_of_element_located((By.XPATH, '//h2')))
actual_title = header.text
print(f'============{actual_title}++++++++++++')

assert 'login' in actual_title.lower(), f'error text in not correct {actual_title}'

username_field = wait.until(EC.visibility_of_element_located((By.ID, 'username')))
username_field.send_keys("student")
username_field_type = username_field.get_attribute('type')

print(f' == {username_field.get_attribute('value')}')

password_field = wait.until(EC.visibility_of_element_located((By.ID, 'password')))
field_type = password_field.get_attribute("type")

assert field_type == 'password', 'type password not correct'
assert username_field_type == 'text', f'type login not correct: {username_field_type}'