from ui.pages.base_page import BasePage
from ui.pages.locators import PaymentPageLocators
from ui.tools.faker import fake


class PaymentPage(BasePage):
    ENDPOINT = "/payment"

    def should_be_payment_page(self):
        self.check_url()
        self.should_be_payment_form()

    def should_be_payment_form(self):
        self.elem_should_be_visible(selector=PaymentPageLocators.PAYMENT_INFO_BLOCK)
        self.elem_should_be_visible(selector=PaymentPageLocators.NAME_OF_CARD)
        self.elem_should_be_visible(selector=PaymentPageLocators.CARD_NUMBER)
        self.elem_should_be_visible(selector=PaymentPageLocators.CVC)
        self.elem_should_be_visible(selector=PaymentPageLocators.EXPIRY_MONTH)
        self.elem_should_be_visible(selector=PaymentPageLocators.EXPIRY_YEAR)
        self.elem_should_be_visible(selector=PaymentPageLocators.PAY_AND_CONFIRM_ORDER_BTN)

    def fill_and_submit_payment_form(self):
        self.enter_data(selector=PaymentPageLocators.NAME_OF_CARD, text=fake.name())
        self.enter_data(selector=PaymentPageLocators.CARD_NUMBER, text=fake.credit_card_number())
        self.enter_data(selector=PaymentPageLocators.CVC, text=fake.credit_card_security_code())
        self.enter_data(selector=PaymentPageLocators.EXPIRY_MONTH, text=fake.credit_card_expire_month())
        self.enter_data(selector=PaymentPageLocators.EXPIRY_YEAR, text=fake.credit_card_expire_year())
        self.click(selector=PaymentPageLocators.PAY_AND_CONFIRM_ORDER_BTN)


