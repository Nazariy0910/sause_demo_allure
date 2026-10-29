# pages/elements_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from POM_project.pages.text_box_page import TextBoxPage
from pages.radio_button_page import RadioButtonPage

class ElementsPage(BasePage):
    TEXT_BOX_ITEM = (By.XPATH, '//span[text()="Text Box"]')
    RADIO_BUTTON_ITEM = (By.XPATH_BOX_ITEM)

    def go_to_text_box(self):
        self.click(self.TEXT_BOX_ITEM)
        self.wait_url_contains('text-box')
        self.remove_ads()
        return TextBoxPage(self.driver)

    # def go_to_radio_button(self):
    #     self.click(self.TEXT_BOX_ITEM)
    #     self.wait_url_contains('radio-button')
    #     self.remove_ads()
    #     return RadioButtonPage(self.driver)

    