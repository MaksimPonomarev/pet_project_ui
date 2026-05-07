import os
from dotenv import load_dotenv
from ui.pages.base_page import BasePage
from ui.pages.locators import DetailProductPageLocators
from ui.test_data.data import ProductDetailData

load_dotenv()


class DetailProductsPage(BasePage):
    ENDPOINT = os.getenv("PRODUCTS_DETAIL_ENDPOINT")

    def check_detail_product_info(self):
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



    def check_review_form(self):
        self.elem_should_be_visible(selector=DetailProductPageLocators.REVIEW_WRITE_FORM)
        self.elem_should_be_visible(selector=DetailProductPageLocators.REVIEW_NAME)
        self.elem_should_be_visible(selector=DetailProductPageLocators.REVIEW_EMAIL)
        self.elem_should_be_visible(selector=DetailProductPageLocators.REVIEW_TEXTAREA_REVIEW)
        self.elem_should_be_visible(selector=DetailProductPageLocators.REVIEW_SUBMIT_BTN)


    def should_be_product_detail_page(self, index=0):
        self.check_url(endpoint=f"{self.ENDPOINT}/{index + 1}")
        self.check_detail_product_info()
        self.check_review_form()