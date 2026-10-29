import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 5)

try:
    driver.get('https://the-internet.herokuapp.com/login')
    driver.maximize_window()

    username_field = driver.find_element(By.ID, 'username')
    username_field.send_keys("tomsmith")

    password_field = driver.find_element(By.XPATH, "//input[@id='password']")
    password_field.send_keys('SuperSecretPassword!')

    button = driver.find_element(By.XPATH, "//button[@class='radius']")
    button.click()
    time.sleep(2)

    green_flash = driver.find_element(By.ID, "flash")
    green_flash_text = green_flash.text
    print(f"Text flash: {green_flash_text}")

    assert "You logger into a secure areal!" in green_flash_text
    print('Test was passed') 

finally:
    driver.quit()