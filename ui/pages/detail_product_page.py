from ui.pages.base_page import BasePage
from ui.pages.locators import DetailProductPageLocators, BasePageLocators
from ui.test_data.data import ProductDetailData, SuccessMessageText
from ui.test_data.factories import UserData
from ui.tools.faker import fake


class DetailProductsPage(BasePage):
    ENDPOINT = "/product_details"

    def should_be_product_detail_page(self, product_id):
        self.check_url(endpoint=f"{self.ENDPOINT}/{product_id}")
        self._check_detail_product_info()
        self._check_review_form()

    def _check_detail_product_info(self):
        self.elem_should_be_visible(selector=DetailProductPageLocators.PRODUCT_DETAILS)
        self.elem_should_be_visible(selector=DetailProductPageLocators.PRODUCT_INFORMATION)
        self.elem_should_be_visible(selector=DetailProductPageLocators.PRODUCT_NAME)
        self.elem_should_be_visible(selector=DetailProductPageLocators.PRODUCT_ADD_TO_CART_BTN)
        self.elem_should_be_visible(selector=DetailProductPageLocators.PRODUCT_PRICE)
        self.elem_should_be_visible(selector=DetailProductPageLocators.QUANTITY)
        self.should_be_visible_with_text(selector=DetailProductPageLocators.PRODUCT_INFORMATION, text=ProductDetailData.CATEGORY)
        self.should_be_visible_with_text(selector=DetailProductPageLocators.PRODUCT_INFORMATION,text=ProductDetailData.CONDITION)
        self.should_be_visible_with_text(selector=DetailProductPageLocators.PRODUCT_INFORMATION, text=ProductDetailData.BRAND)
        self.should_be_visible_with_text(selector=DetailProductPageLocators.PRODUCT_INFORMATION,text=ProductDetailData.AVAILABILITY)

    def _check_review_form(self):
        self.elem_should_be_visible(selector=DetailProductPageLocators.REVIEW_WRITE_FORM)
        self.elem_should_be_visible(selector=DetailProductPageLocators.REVIEW_NAME)
        self.elem_should_be_visible(selector=DetailProductPageLocators.REVIEW_EMAIL)
        self.elem_should_be_visible(selector=DetailProductPageLocators.REVIEW_TEXTAREA_REVIEW)
        self.elem_should_be_visible(selector=DetailProductPageLocators.REVIEW_SUBMIT_BTN)

    def enter_quantity_for_product(self, quantity: int):
        self.enter_data(selector=DetailProductPageLocators.QUANTITY, text=str(quantity))

    def click_continue_on_detail_product_page(self):
        self.click_and_wait_network(selector=BasePageLocators.CONTINUE_SHOPPING_BTN)

    def add_detail_product_to_cart(self):
        self.click(selector=DetailProductPageLocators.PRODUCT_ADD_TO_CART_BTN)
        self.click_continue_on_detail_product_page()

    def fill_and_send_review_form(self, user_info: UserData):
        self.enter_data(selector=DetailProductPageLocators.REVIEW_NAME, text=user_info.name)
        self.enter_data(selector=DetailProductPageLocators.REVIEW_EMAIL, text=user_info.email)
        self.enter_data(selector=DetailProductPageLocators.REVIEW_TEXTAREA_REVIEW, text=fake.paragraph())
        self.click(selector=DetailProductPageLocators.REVIEW_SUBMIT_BTN)

    def should_be_success_message_after_send_review_product(self):
        self.should_be_success_message(selector=DetailProductPageLocators.SUCCESS_MESSAGE, text=SuccessMessageText.PRODUCT_REVIEW)