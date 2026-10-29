import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/login")
    driver.maximize_window()
    time.sleep(1)

    password_field = driver.find_element(By.ID, "password")

    field_type = password_field.get_attribute("type")
    print(f"Type password: {field_type}")

    assert (
        field_type == "password"), "Criticall bug: "
    print(f"Validation successful. Field type {field_type}")

    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    button_class = login_button.get_attribute("class")
    print(f"Class of button Login: {button_class}")

finally:
    driver.quit()