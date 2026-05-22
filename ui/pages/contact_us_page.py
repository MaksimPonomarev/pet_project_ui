from ui.pages.base_page import BasePage
from ui.pages.locators import ContactUsPageLocators
from ui.test_data.data import SuccessMessageText
from ui.tools.faker import fake
from config import settings


class ContactUsPage(BasePage):
    ENDPOINT = "/contact_us"

    def should_be_contact_us_page(self):
        self.check_url()
        self.elem_should_be_visible(selector=ContactUsPageLocators.NAME)
        self.elem_should_be_visible(selector=ContactUsPageLocators.EMAIL)
        self.elem_should_be_visible(selector=ContactUsPageLocators.SUBJECT)
        self.elem_should_be_visible(selector=ContactUsPageLocators.MESSAGE)
        self.elem_should_be_visible(selector=ContactUsPageLocators.INPUT_FILE)
        self.elem_should_be_visible(selector=ContactUsPageLocators.SUBMIT_BTN)

    def should_be_success_message_send_feedback(self):
        self.should_be_visible_with_text(text=SuccessMessageText.ADD_PRODUCT, selector=ContactUsPageLocators.SUCCESS_MESSAGE_LOCATOR)

    def submit_contact_form(self):
        self.enter_data(selector=ContactUsPageLocators.NAME,text=fake.name())
        self.enter_data(selector=ContactUsPageLocators.EMAIL, text=fake.email())
        self.enter_data(selector=ContactUsPageLocators.SUBJECT, text=fake.subject())
        self.enter_data(selector=ContactUsPageLocators.MESSAGE, text=fake.paragraph())
        self.enter_file(selector=ContactUsPageLocators.INPUT_FILE, path_to_file=settings.test_data.image_png_file)
        self.accept_alert()
        self.click(selector=ContactUsPageLocators.SUBMIT_BTN)

    def click_home_btn_after_submit(self):
        self.click(selector=ContactUsPageLocators.GO_TO_HOME_BTN)
