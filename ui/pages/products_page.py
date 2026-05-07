import os
from dotenv import load_dotenv
from ui.pages.base_page import BasePage
from ui.pages.locators import ProductsPageLocators

load_dotenv()


class ProductsPage(BasePage):
    ENDPOINT = os.getenv("PRODUCTS_ENDPOINT")

    def should_be_product_page(self):
        self.elem_should_be_visible(selector=ProductsPageLocators.ADVERTISEMENT)
        self.elem_should_be_visible(selector=ProductsPageLocators.SEARCH_PRODUCT)
        self.elem_should_be_visible(selector=ProductsPageLocators.LEFT_SIDEBAR)
        self.first_elem_should_be_visible(selector=ProductsPageLocators.CARD_OF_ITEM)
        self.check_url()




