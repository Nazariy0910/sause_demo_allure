# pages/elements_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from POM_project.pages.text_box_page import TextBoxPage
from pages.radio_button_page import PracticeFormPage

class FormsPage(BasePage):
    PRACTICE_FORM_ITEM = (By.XPATH, '//span[text()="Practice Form"]')


    def go_to_practice_form(self):
        self.click(self.PRACTICE_FORM_ITEM)
        self.wait_url_contains('automation-practice-form')
        self.remove_ads()
        return PracticeFormPage(self.driver)


    