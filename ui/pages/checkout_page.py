from ui.pages.base_page import BasePage
from ui.pages.locators import CheckoutPageLocators
from ui.test_data.factories import UserData
from ui.tools.faker import fake


class CheckoutPage(BasePage):
    ENDPOINT = "/checkout"

    def should_be_checkout_page(self):
        self.check_url()
        self.elem_should_be_visible(selector=CheckoutPageLocators.ADDRESS_DELIVERY)
        self.elem_should_be_visible(selector=CheckoutPageLocators.ADDRESS_INVOICE)
        self.elem_should_be_visible(selector=CheckoutPageLocators.ORDER_ADD_INFO)
        self.elem_should_be_visible(selector=CheckoutPageLocators.PLACE_ORDER_BTN)

    def check_orders_details(self, user_data: UserData):
        address_delivery = self.page.locator(CheckoutPageLocators.ADDRESS_DELIVERY)
        address_invoice = self.page.locator(CheckoutPageLocators.ADDRESS_INVOICE)

        delivery_text = self.get_inner_text(root=address_delivery)
        invoice_text = self.get_inner_text(root=address_invoice)
        for value in user_data.address_fields().values():
            self.assert_contains(needle=value, haystack=delivery_text)
            self.assert_contains(needle=value, haystack=invoice_text)

    def fill_comment(self):
        self.enter_data(selector=CheckoutPageLocators.ORDER_ADD_INFO_PLACE, text=fake.paragraph())

    def click_place_order(self):
        self.click(CheckoutPageLocators.PLACE_ORDER_BTN)