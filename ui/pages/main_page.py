
import os
from dotenv import load_dotenv
from playwright.sync_api import expect
from ui.pages.base_page import BasePage
from ui.pages.locators import MainPageLocators


load_dotenv()


class MainPage(BasePage):
    ENDPOINT = os.getenv("MAIN_ENDPOINT")
    
    def should_be_main_page(self):
        self.elem_should_be_visible(selector=MainPageLocators.CAROUSEL_SLIDER)

        self.elem_should_be_visible(selector=MainPageLocators.LEFT_SIDEBAR)
        self.elem_should_be_visible(selector=MainPageLocators.LEFT_SIDEBAR)
        self.first_elem_should_be_visible(selector=MainPageLocators.CARD_OF_ITEM)
        self.check_url()


    def should_be_cookie_banner(self):
        cookie_banner = self.page.locator(MainPageLocators.COOKIE_BANNER)
        cookie_banner.wait_for(state="attached")

    def accept_cookie_banner(self):
        cookie_banner = self.page.locator(MainPageLocators.COOKIE_BANNER)
        cookie_banner.wait_for(state="visible")
        self.click(selector=MainPageLocators.ACCEPT_COOKIE_BANNER_BTN)
        expect(cookie_banner).to_be_hidden()

    