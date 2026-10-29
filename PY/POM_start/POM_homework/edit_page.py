from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EditPage:
    URL = "https://practicetestautomation.com/practice-test-exceptions/"

    EDIT_BTN = (By.ID, "edit_btn")
    ROW_1_INPUT = (By.XPATH, "//div[@id='row1']/input")
    SAVE_BTN = (By.XPATH, "//button[@id='save_btn']")
    CONFIRMATION_MSG = (By.XPATH, "//*[contains(text(), 'Row 1 was saved')]")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self.driver.get(self.URL)

    def click_edit(self):
        self.wait.until(EC.element_to_be_clickable(self.EDIT_BTN)).click()

    def update_row_1(self, text):
        row1_field = self.wait.until(EC.element_to_be_clickable(self.ROW_1_INPUT))
        row1_field.clear()
        row1_field.send_keys(text)

    def click_save(self):
        self.driver.find_element(*self.SAVE_BTN).click()

    def get_confirmation_text(self):
        confirmation = self.wait.until(EC.visibility_of_element_located(self.CONFIRMATION_MSG))
        return confirmation.text