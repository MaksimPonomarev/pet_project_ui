from ui.pages.base_page import BasePage
from ui.pages.locators import CartPageLocators, CartItemLocators


class CartPage(BasePage):
    ENDPOINT = "/view_cart"

    def should_be_empty_cart(self):
        self.check_url()
        self.elem_should_be_visible(selector=CartPageLocators.BREADCRUMB)
        self.elem_should_be_visible(selector=CartPageLocators.EMPTY_CART)

    def should_be_filled_cart(self):
        self.check_url()
        self.elem_should_be_visible(selector=CartPageLocators.CART_INFO)
        self.elem_should_be_visible(selector=CartPageLocators.CHECKOUT_BTN)

    def _parse_price(self, price: str) -> float:
        return float(price.replace("Rs.", "").strip())

    def get_total_price(self, product_price: str, product_quantity: str) -> float:
        return self._parse_price(product_price) * int(product_quantity)

    def check_quantity(self, item_id: int, expect_quantity: int):
        actual_quantity = self.get_text_by_locator(selector=CartPageLocators.product_quantity(item_id))
        self.assert_equal(int(actual_quantity), expect_quantity)

    def should_be_added_products(self, cart_items: dict):
        assert cart_items, "cart_items пустой"
        for id_product, product_info in cart_items.items():
            self.elem_should_be_visible(selector=CartPageLocators.id_card(id_product))

            product_name = self.get_text_by_locator(selector=CartPageLocators.product_name(id_product))
            product_price = self.get_text_by_locator(selector=CartPageLocators.product_price(id_product))
            product_quantity = self.get_text_by_locator(selector=CartPageLocators.product_quantity(id_product))
            product_total = self.get_text_by_locator(selector=CartPageLocators.product_total_price(id_product))

            self.assert_equal(product_info["name"], product_name)
            self.assert_equal(self._parse_price(product_info["price"]), self._parse_price(product_price))
            self.assert_equal(product_info["count"], int(product_quantity))
            self.assert_equal(self.get_total_price(product_price, product_quantity), self._parse_price(product_total))

    def should_not_be_visible_elem_by_id(self, product_id: int):
        self.should_not_be_visible(selector=CartItemLocators.id_card(product_id))

    def go_to_login_page_from_checkout_form(self):
        self.click_checkout_btn()
        self.click(CartPageLocators.LOGIN_LINK_IN_CHECKOUT)

    def click_checkout_btn(self):
        self.click(CartPageLocators.CHECKOUT_BTN)

    def delete_product_by_id(self, product_id: int):
        self.click(selector=CartPageLocators.delete_product_btn(product_id))


