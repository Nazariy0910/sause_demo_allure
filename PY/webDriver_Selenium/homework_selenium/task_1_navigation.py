import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 5)

driver.get('https://the-internet.herokuapp.com')
driver.maximize_window()
time.sleep(1)

link = driver.find_element(By.XPATH, "//a[text()='Form Authentication']")
link.click()
time.sleep(1)

assert "The Internet" in driver.title, f"Unexpected header: {driver.title}"
print(f"Header page: {driver.title}")

driver.back()
time.sleep(1)
driver.quit()