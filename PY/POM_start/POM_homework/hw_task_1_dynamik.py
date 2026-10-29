from selenium import webdriver
from PY.POM_start.POM_homework.exceptions_page import ExceptionsPage  

def test_dynamic_element():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        page = ExceptionsPage(driver)

        page.open()

        page.click_add_button()

        page.fill_row_2("Pizza")

        print("✅ Row 2 Is completed!")

    finally:
        driver.quit()

if __name__ == "__main__":
    test_dynamic_element()