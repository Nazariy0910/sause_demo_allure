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

#username_field = driver.find_element("username").send_keys("student")
element = wait.until(EC.visibility_of_element_located((By.ID, 'username'))).send_keys("student")
element = wait.until(EC.visibility_of_element_located((By.ID, 'password'))).send_keys("Password123")
element = wait.until(EC.element_to_be_clickable((By.ID, 'submit'))).click()

# #username_field = driver.find_element(By.ID, 'username')
# username_field = wait.until(EC.presence_of_all_elements_located((By.ID, 'username')))
# element = wait.until(EC.visibility_of_element_located((By.ID, 'error')))чи видно елемент
# button = wait.until(EC.element_to_be_clickable((By.ID, 'submit')))чи він клікабельний
