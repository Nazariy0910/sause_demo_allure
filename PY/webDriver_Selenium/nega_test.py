import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver  = webdriver.Chrome(service=service)


print ('open browser')
driver.get('https://the-internet.herokuapp.com/login')

driver.maximize_window()
time.sleep(3)

username_field = driver.find_element(By.ID, 'username')
username_field.send_keys("qa_ninja")
time.sleep(2)

#search by xpath
print('enter password........')
password_field = driver.find_element(By.ID, 'password')
password_field.send_keys('12345 !')
time.sleep(2)

#search by class
login_button = driver.find_element(By.XPATH, '//button[@class="radius"]')
login_button.click()
time.sleep(2)

error_field = driver.find_element(By.ID, "flash")
error_field_text=error_field.text

assert "Your username is invalid!" in error_field_text, 'все херня'
