
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait          
from selenium.webdriver.support import expected_conditions as EC 

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://practicetestautomation.com/practice-test-login/')

wait = WebDriverWait(driver, 6)

wait.until(EC.visibility_of_element_located((By.ID, 'username'))).send_keys("incorrectUser")
wait.until(EC.visibility_of_element_located((By.ID, 'password'))).send_keys("incorrectPassword")
wait.until(EC.element_to_be_clickable((By.ID, 'submit'))).click()

red_block_field = wait.until(EC.visibility_of_element_located((By.ID, 'error')))
red_block_field_text = red_block_field.text

assert "Your username is invalid!" in red_block_field_text
print('Negative test is completed')

driver.close()