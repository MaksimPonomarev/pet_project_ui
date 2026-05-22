from ui.pages.locators import BasePageLocators
from ui.test_data.data import SuccessMessageText
from ui.tools.faker import fake


class FooterComponent:
    def __init__(self, base_page):
        self.base_page = base_page

    def should_be_footer(self):
        self.base_page.elem_should_be_visible(BasePageLocators.FOOTER)
        self.base_page.elem_should_be_visible(BasePageLocators.FOOTER_TITLE)
        self.base_page.elem_should_be_visible(BasePageLocators.FOOTER_EMAIL)
        self.base_page.elem_should_be_visible(BasePageLocators.FOOTER_SUBSCRIBE_BTN)

    def fill_and_submit_subscribe_form(self):
        self.base_page.enter_data(selector=BasePageLocators.FOOTER_EMAIL, text=fake.email())
        self.base_page.click(selector=BasePageLocators.FOOTER_SUBSCRIBE_BTN)

    def should_be_subscribe_success_message(self):
        self.base_page.should_be_success_message(BasePageLocators.FOOTER_SUCCESS_SUBSCRIBE_MESSAGE, text=SuccessMessageText.FOOTER_SUBSCRIBE)

    def scroll_to_footer(self):
        self.base_page.scroll_to_elem(selector=BasePageLocators.FOOTER)