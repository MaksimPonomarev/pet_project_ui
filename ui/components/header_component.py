from playwright.sync_api import expect
from ui.pages.locators import BasePageLocators
from ui.test_data.data import HeaderSite


class HeaderComponent:
    def __init__(self, base_page):
        self.base_page = base_page

    def should_be_header(self):
        self.base_page.elem_should_be_visible(BasePageLocators.HEADER)

        nav_items = [
            (BasePageLocators.HOME_LINK, HeaderSite.HOME),
            (BasePageLocators.PRODUCTS_LINK, HeaderSite.PRODUCTS),
            (BasePageLocators.CART_LINK, HeaderSite.CART),
            (BasePageLocators.LOGIN_LINK, HeaderSite.SIGNUP_LOGIN),
            (BasePageLocators.TEST_CASES_LINK, HeaderSite.TEST_CASES),
            (BasePageLocators.API_LIST_LINK, HeaderSite.API_TESTING),
            (BasePageLocators.VIDEO_TUTORIALS_LINK, HeaderSite.VIDEO_TUTORIALS),
            (BasePageLocators.CONTACT_US_LINK, HeaderSite.CONTACT_US),
        ]

        for selector, text in nav_items:
            self.base_page.should_be_visible_with_text(selector=selector, text=text)

    def should_be_logged_in(self):
        self.base_page.elem_should_be_visible(selector=BasePageLocators.LOGOUT_LINK)
        self.base_page.elem_should_be_visible(selector=BasePageLocators.DELETE_ACCOUNT_LINK)
        self.base_page.should_be_visible_with_text(selector=BasePageLocators.HEADER, text=HeaderSite.LOGGED_IN_TEXT)

    def delete_account(self):
        self.base_page.click_and_wait_network(selector=BasePageLocators.DELETE_ACCOUNT_LINK)

    def should_be_logged_out(self):
        self.base_page.elem_should_be_visible(selector=BasePageLocators.LOGIN_LINK)

    def logout(self):
        self.base_page.click_and_wait_network(selector=BasePageLocators.LOGOUT_LINK)

    def should_be_header_visible(self, visible=True):
        self.base_page.should_be_elem_in_viewport(selector=BasePageLocators.HEADER, visible=visible)

    def go_to_home(self):
        self.base_page.click_and_wait_network(selector=BasePageLocators.HOME_LINK)

    def go_to_products(self):
        self.base_page.click_and_wait_network(selector=BasePageLocators.PRODUCTS_LINK)

    def go_to_cart(self):
        self.base_page.click_and_wait_network(selector=BasePageLocators.CART_LINK)

    def go_to_login(self):
        self.base_page.click_and_wait_network(selector=BasePageLocators.LOGIN_LINK)

    def go_to_test_cases(self):
        self.base_page.click_and_wait_network(selector=BasePageLocators.TEST_CASES_LINK)

    def go_to_api_list(self):
        self.base_page.click_and_wait_network(selector=BasePageLocators.API_LIST_LINK)

    def go_to_video_tutorials(self):
        self.base_page.click_and_wait_network(selector=BasePageLocators.VIDEO_TUTORIALS_LINK)

    def go_to_contact_us(self):
        self.base_page.click_and_wait_network(selector=BasePageLocators.CONTACT_US_LINK)
