import time
from ui.pages.base_page import BasePage, BASE_URL
import os
from dotenv import load_dotenv
from playwright.sync_api import expect
from ui.pages.base_page import BasePage
from ui.pages.locators import LoginPageLocators, SignupPageLocators, BasePageLocators, ContactUsPageLocators, \
    CartPageLocators
from ui.pages.main_page import MainPage
from ui.tools.faker import fake
from config import settings


load_dotenv()


class CartPage(BasePage):
    ENDPOINT = os.getenv("CART_ENDPOINT")

    def should_be_empty_cart(self):
        self.elem_should_be_visible(selector=CartPageLocators.BREADCRUMB)
        self.elem_should_be_visible(selector=CartPageLocators.EMPTY_CART)
        self.check_url()

    def should_be_filled_cart(self):
        self.elem_should_be_visible(selector=CartPageLocators.TABLE_ITEMS)
        self.elem_should_be_visible(selector=CartPageLocators.CHECKOUT_BTN)
        self.check_url()