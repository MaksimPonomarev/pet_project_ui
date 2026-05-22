from ui.components.left_sidebar_component import LeftSidebarComponent
from ui.pages.base_page import BasePage
from ui.pages.locators import BasePageLocators
from ui.test_data.data import BaseSubcategory


class CategoryProductPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.sidebar = LeftSidebarComponent(self)

    @staticmethod
    def endpoint_category(category):
        return f"/category_products/{category}"

    @staticmethod
    def title_category(category):
        return f"{category} Products"

    def should_be_subcategory_products_page(self, subcategory: BaseSubcategory):
        self.check_url(endpoint=self.endpoint_category(subcategory.id))
        self.should_be_visible_with_text(selector=BasePageLocators.TITLE, text=self.title_category(subcategory.title), exact=True)

