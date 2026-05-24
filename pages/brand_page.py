from components.left_sidebar_component import LeftSidebarComponent
from pages.base_page import BasePage
from pages.locators import BasePageLocators
from test_data.data import Brands

class BrandProductPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.sidebar = LeftSidebarComponent(self)

    def should_be_brand_products_page(self, brand: Brands):
        self.check_url(endpoint=brand.url)
        self.should_be_visible_with_text(selector=BasePageLocators.TITLE, text=brand.title_brand, exact=True)