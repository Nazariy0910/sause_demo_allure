# tests/test_navigation.py
from pages.home_page import HomePage
from pages.text_box_page import TextBoxPage


def test_navigate_to_text_box_and_submit(driver):
    text_box = HomePage(driver).open_page().go_to_elements().go_to_text_box()

    assert isinstance(text_box, TextBoxPage)
    assert 'text-box' in text_box.get_current_url()

    text_box.fill_form(full_name='Ivan Tester', email='ivan@test.com')
    text_box.submit()
    assert 'Ivan Tester' in text_box.get_output_name()