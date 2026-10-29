from selenium import webdriver
from PY.POM_start.POM_homework.table_page import TablePage

def test_check_table_level():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        page = TablePage(driver)

        page.open()

        page.wait_for_table()

        page.wait_for_course_cell()

        level_text = page.get_level_text()
        print(f"Achieve a level: {level_text}")

        assert level_text == "Beginner", f"Expecting 'Beginner', receiver: '{level_text}'"
        print("✅ Level course is true!")

    finally:
        driver.quit()

if __name__ == "__main__":
    test_check_table_level()