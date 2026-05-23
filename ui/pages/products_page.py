from ui.pages.base_page import BasePage
from ui.pages.locators import ProductsPageLocators


class ProductsPage(BasePage):
    ENDPOINT = "/products"

    def should_be_product_page(self):
        self.check_url()
        self.elem_should_be_visible(selector=ProductsPageLocators.ADVERTISEMENT)
        self.elem_should_be_visible(selector=ProductsPageLocators.SEARCH_PRODUCT)
        self.elem_should_be_visible(selector=ProductsPageLocators.CARD_OF_ITEM)

    def check_all_results_search_product(self, product_name: str):
        cards = self.page.locator(selector=ProductsPageLocators.CARD_OF_ITEM)
        for i in range(cards.count()):
            card = cards.nth(i)
            self.should_be_visible_with_text(selector=ProductsPageLocators.ITEM_NAME, text=product_name, root=card)

    def enter_and_submit_search(self, product_name: str):
        self.enter_data(selector=ProductsPageLocators.SEARCH_PRODUCT, text=product_name)
        self.click(selector=ProductsPageLocators.SUBMIT_SEARCH_BTN)
