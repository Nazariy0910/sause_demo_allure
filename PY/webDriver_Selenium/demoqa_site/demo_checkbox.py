import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://demoqa.com/automation-practice-form")
    driver.maximize_window()
    time.sleep(1)

    sport_checkbox = wait.until(EC.presence_of_element_located((By.ID, "hobbies-checkbox-1")))
    reading_checkbox = driver.find_element(By.ID, "hobbies-checkbox-2")
    music_checkbox = driver.find_element(By.ID, "hobbies-checkbox-3")

    sport_label = driver.find_element(By.XPATH, '//label[@for="hobbies-checkbox-1"]')
    reading_label = driver.find_element(By.XPATH, '//label[@for="hobbies-checkbox-2"]')
    music_label = driver.find_element(By.XPATH, '//label[@for="hobbies-checkbox-3"]')

    print(f"Sport subscribe: {sport_checkbox.is_selected()}")
    print(f"Reading subscribe: {reading_checkbox.is_selected()}")
    print(f"Music subscribe: {music_checkbox.is_selected()}")

    if sport_checkbox.is_selected():
        print("Sport subsc! Does nothing")
    else:
        print("Sport not subsc. Click")
        sport_label.click()

    # if not sport_checkbox.is_selected():
    #     sport_label.click()

    if reading_checkbox.is_selected():
            print("Reading subsc! Does nothing")
    else:
        print("Reading not subsc. Click")
        reading_label.click()

    print(f"Sport subscribe: {sport_checkbox.is_selected()}")
    print(f"Reading subscribe: {reading_checkbox.is_selected()}")
    print(f"Music subscribe: {music_checkbox.is_selected()}")
    
    time.sleep(4)
finally:
    driver.quit()