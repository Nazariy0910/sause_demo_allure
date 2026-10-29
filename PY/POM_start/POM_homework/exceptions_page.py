from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ExceptionsPage:
    URL = "https://practicetestautomation.com/practice-test-exceptions/"
    
    ADD_BUTTON = (By.XPATH, "//button[@id='add_btn']")
    ROW_2_INPUT = (By.XPATH, "(//input[@class='input-field'])[2]")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self.driver.get(self.URL)

    def click_add_button(self):
        add_btn = self.wait.until(EC.element_to_be_clickable(self.ADD_BUTTON))
        add_btn.click()

    def fill_row_2(self, text):
        row_2_field = self.wait.until(EC.presence_of_element_located(self.ROW_2_INPUT))
        row_2_field.send_keys(text)