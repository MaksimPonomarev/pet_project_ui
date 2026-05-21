from playwright.sync_api import expect

from ui.components.left_sidebar_component import LeftSidebarComponent
from ui.pages.base_page import BasePage
from ui.pages.locators import MainPageLocators, LeftSidebarLocators


class MainPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.sidebar = LeftSidebarComponent(self)

    ENDPOINT = "/"
    
    def should_be_main_page(self):
        
        self.check_url()
        self.elem_should_be_visible(selector=MainPageLocators.CAROUSEL_SLIDER)
        self.elem_should_be_visible(selector=LeftSidebarLocators.LEFT_SIDEBAR)
        self.elem_should_be_visible(selector=MainPageLocators.CARD_OF_ITEM)
        self.elem_should_be_visible(selector=MainPageLocators.RECOMMENDED_ITEMS_BLOCK)
        self.elem_should_be_visible(selector=MainPageLocators.RECOMMENDED_ITEMS_LIST)


    def should_be_cookie_banner(self):
        cookie_banner = self.page.locator(MainPageLocators.COOKIE_BANNER)
        cookie_banner.wait_for(state="attached")

    def accept_cookie_banner(self):
        cookie_banner = self.page.locator(MainPageLocators.COOKIE_BANNER)
        cookie_banner.wait_for(state="visible")
        self.click(selector=MainPageLocators.ACCEPT_COOKIE_BANNER_BTN)
        expect(cookie_banner).to_be_hidden()

    def add_recommended_product(self):
        self.add_product_to_cart(selector=MainPageLocators.RECOMMENDED_ITEMS_LIST, is_hover=False)

