from components.left_sidebar_component import LeftSidebarComponent
from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    ENDPOINT = "/"

    def __init__(self, page):
        super().__init__(page)
        self.sidebar = LeftSidebarComponent(self)
    
    def should_be_main_page(self):
        self.check_url()
        self.elem_should_be_visible(selector=MainPageLocators.CAROUSEL_SLIDER)
        self.elem_should_be_visible(selector=MainPageLocators.CARD_OF_ITEM)
        self.elem_should_be_visible(selector=MainPageLocators.RECOMMENDED_ITEMS_BLOCK)
        self.elem_should_be_visible(selector=MainPageLocators.RECOMMENDED_ITEMS_LIST)
        self.sidebar.should_be_left_sidebar_visible()

    def should_be_cookie_banner(self):
        self.elem_should_be_visible(selector=MainPageLocators.COOKIE_BANNER)

    def should_not_be_cookie_banner(self):
        self.should_not_be_visible(selector=MainPageLocators.COOKIE_BANNER)

    def accept_cookie_banner(self):
        self.click_and_wait_network(selector=MainPageLocators.ACCEPT_COOKIE_BANNER_BTN)

    def add_recommended_product(self, cart_items):
        self.add_product_to_cart(selector=MainPageLocators.RECOMMENDED_ITEMS_LIST, is_hover=False, cart_items=cart_items)

    def should_be_redirect_on_youtube(self):
        self.check_url(expected_url="youtube")