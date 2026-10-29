from selenium import webdriver
from PY.POM_start.POM_homework.edit_page import EditPage

def test_edit_clear_save():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        page = EditPage(driver)

        page.open()

        page.click_edit()

        page.update_row_1("Sushi")

        page.click_save()

        msg_text = page.get_confirmation_text()
        print(f"Текст на сторінці: {msg_text}")

        print("✅ Files is saved!")

    finally:
        driver.quit()

if __name__ == "__main__":
    test_edit_clear_save()