import time

from ui.pages.locators import LeftSidebarLocators
from ui.test_data.data import Brands, CategoryGroup, BaseSubcategory, CATEGORY_SUBCATEGORIES


class LeftSidebarComponent:
    def __init__(self, base_page):
        self.base_page = base_page

    def open_category_group(self, category: CategoryGroup):
        self.base_page.click_and_wait_network(selector=LeftSidebarLocators.category_group(category.value))

    def should_be_category_group_opened(self, category: CategoryGroup):

        self.base_page.wait_for_selector_state(selector=LeftSidebarLocators.opened_category_group(category=category))
        subcategory = CATEGORY_SUBCATEGORIES[category]

        for elem in subcategory:
            self.base_page.elem_should_be_visible(selector=LeftSidebarLocators.subcategory(subcategory=elem.id))

    def open_subcategory_page(self, subcategory: BaseSubcategory):
        self.base_page.click_and_wait_network(selector=LeftSidebarLocators.subcategory(subcategory.id))

    def open_brand_page(self, brand: Brands):
        self.base_page.click_and_wait_network(selector=LeftSidebarLocators.brand_item(brand.value))


    def should_be_brands_on_left_sidebar(self):
        """
        Check all brands on left sidebar presence
        """
        self.base_page.elem_should_be_visible(selector=LeftSidebarLocators.BRANDS)
        for elem in Brands:
            self.base_page.elem_should_be_visible(selector=LeftSidebarLocators.brand_item(elem.value))