from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TablePage:
    URL = "https://practicetestautomation.com/practice-test-table/"
    
    TABLE = (By.XPATH, "//table")
    COURSE_CELL = (By.XPATH, "//td[text()='Selenium with Python']")
    LEVEL_CELL = (By.XPATH, "//td[text()='Selenium with Python']/following-sibling::td[2]")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self.driver.get(self.URL)

    def wait_for_table(self):
        return self.wait.until(EC.visibility_of_element_located(self.TABLE))

    def wait_for_course_cell(self):
        return self.wait.until(EC.visibility_of_element_located(self.COURSE_CELL))

    def get_level_text(self):
        level_cell = self.driver.find_element(*self.LEVEL_CELL)
        return level_cell.text