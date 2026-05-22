from ui.components.left_sidebar_component import LeftSidebarComponent
from ui.pages.base_page import BasePage
from ui.pages.locators import BasePageLocators
from ui.test_data.data import Brands

class BrandProductPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.sidebar = LeftSidebarComponent(self)

    def should_be_brand_products_page(self, brand: Brands):
        self.check_url(endpoint=brand.url)
        self.should_be_visible_with_text(selector=BasePageLocators.TITLE, text=brand.title_brand, exact=True)