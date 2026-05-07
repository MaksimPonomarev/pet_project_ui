import os
from dotenv import load_dotenv
from playwright.sync_api import expect

from config import settings
from ui.pages.locators import BasePageLocators, LoginPageLocators, ContactUsPageLocators

load_dotenv()
BASE_URL = os.getenv("BASE_URL")

class BasePage:
    ENDPOINT = ""
    def __init__(self, page):
        self.page = page

    def should_be_visible_with_text(self, text, selector=None):
        if selector:
            expect(self.page.locator(selector).filter(has_text=text)).to_be_visible()
        else:
            expect(self.page.get_by_text(text)).to_be_visible()

    def should_be_logged_in(self):
        self.elem_should_be_visible(selector=BasePageLocators.LOGOUT_LINK)
        self.elem_should_be_visible(selector=BasePageLocators.DELETE_ACCOUNT_LINK)
        expect(self.page.get_by_text("Logged in")).to_be_visible()

    def accept_alert(self):
        self.page.on("dialog", lambda dialog: dialog.accept())

    def dismiss_alert(self):
        self.page.on("dialog", lambda dialog: dialog.dismiss())

    def enter_data(self, selector, text):
        self.page.locator(selector=selector).fill(value=text)
        return text

    def enter_file(self, selector, path_to_file):
        self.page.locator(selector=selector).set_input_files(path_to_file)

    def check_url(self, endpoint=None):
        expected_url = f"{BASE_URL}{endpoint or self.ENDPOINT}"
        expect(self.page).to_have_url(expected_url)

    def click(self, selector, index=0):
        el = self.page.locator(selector=selector).nth(index)
        expect(el).to_be_enabled()
        el.click()

    def elem_should_be_visible(self, selector):
        elem = self.page.locator(selector=selector)
        expect(elem).to_be_visible()
        return elem
    
    def first_elem_should_be_visible(self, selector, root=None):
        locator = root or self.page
        elem = locator.locator(selector).first
        expect(elem).to_be_visible()
        return elem

    def first_elem_should_be_attached(self, selector, root=None):
        locator = root or self.page
        elem = locator.locator(selector).first
        expect(elem).to_be_attached()
        return elem

    def should_be_login_link_enable(self):
        login_button = self.elem_should_be_visible(BasePageLocators.LOGIN_LINK)
        expect(login_button).to_have_attribute("href", "/login")

    def should_be_head_of_site(self):
        expect(self.page.locator(BasePageLocators.PANEL_OF_TABS)).to_be_visible()

        nav_items = [
            (BasePageLocators.HOME_LINK, "Home"),
            (BasePageLocators.PRODUCTS_LINK, "Products"),
            (BasePageLocators.CART_LINK, "Cart"),
            (BasePageLocators.LOGIN_LINK, "Signup / Login"),
            (BasePageLocators.TEST_CASES_LINK, "Test Cases"),
            (BasePageLocators.API_LIST_LINK, "API Testing"),
            (BasePageLocators.VIDEO_TUTORIALS_LINK, "Video Tutorials"),
            (BasePageLocators.CONTACT_US_LINK, "Contact us"),
        ]

        for selector, text in nav_items:
            expect(self.page.locator(selector=selector, has_text=text)).to_be_visible()



    def should_be_logged_out(self):
        expect(self.page.locator(BasePageLocators.LOGIN_LINK)).to_be_visible()

    def logout(self):
        self.click(selector=BasePageLocators.LOGOUT_LINK)

    def select_elem_in_dropdown(self, selector, value):
        self.page.locator(selector=selector).select_option(value=value)

    def open(self):
        self.page.goto(f"{BASE_URL}{self.ENDPOINT}", timeout=settings.navigation_timeout)


    def add_first_product_to_cart(self):
        self.page.locator(selector=BasePageLocators.ADD_TO_CART_BTN).first.hover()
        self.page.locator(selector=BasePageLocators.ADD_TO_CART_BTN).nth(0).click()
        self.click(selector=BasePageLocators.CONTINUE_SHOPPING_BTN)

    def check_product_card(self, index=0):
        card = self.page.locator(selector=BasePageLocators.CARD_OF_ITEM).nth(index)

        self.first_elem_should_be_visible(selector=BasePageLocators.IMAGE_OF_CARD, root=card)
        self.first_elem_should_be_visible(selector=BasePageLocators.ITEM_PRICE, root=card)
        self.first_elem_should_be_visible(selector=BasePageLocators.ITEM_NAME, root=card)
        self.first_elem_should_be_visible(selector=BasePageLocators.ADD_TO_CART_BTN, root=card)

    def check_product_card_view_product_btn(self):
        self.first_elem_should_be_visible(selector=BasePageLocators.VIEW_PRODUCT_DETAILS_BTN)


    def open_product_card_detail(self):
        self.click(selector=BasePageLocators.VIEW_PRODUCT_DETAILS_BTN)


    def go_to_home(self):
        self.click(selector=BasePageLocators.HOME_LINK)

    def go_to_products(self):
        self.click(selector=BasePageLocators.PRODUCTS_LINK)

    def go_to_cart(self):
        self.click(selector=BasePageLocators.CART_LINK)

    def go_to_login(self):
        self.click(selector=BasePageLocators.LOGIN_LINK)

    def go_to_test_cases(self):
        self.click(selector=BasePageLocators.TEST_CASES_LINK)

    def go_to_api_list(self):
        self.click(selector=BasePageLocators.API_LIST_LINK)

    def go_to_video_tutorials(self):
        self.click(selector=BasePageLocators.VIDEO_TUTORIALS_LINK)

    def go_to_contact_us(self):
        self.click(selector=BasePageLocators.CONTACT_US_LINK)