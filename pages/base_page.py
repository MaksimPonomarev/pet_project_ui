import os
import re
from typing import Any
from playwright.sync_api import expect, Locator
from config import settings
from components.footer_component import FooterComponent
from components.header_component import HeaderComponent
from pages.locators import BasePageLocators, LeftSidebarLocators


class BasePage:
    ENDPOINT = ""
    BASE_URL = settings.base_url
    def __init__(self, page):
        self.page = page
        self.header = HeaderComponent(self)
        self.footer = FooterComponent(self)
        self.cart_items = {}

    def click(self, selector: str, root: Locator | None = None, force: bool = False):
        locator = root or self.page
        el = locator.locator(selector)
        el.click(force=force)

    def click_and_wait_network(self, selector: str, root: Locator | None = None, force: bool = False) :
        self.click(selector, root=root, force=force)
        self.wait_for_load_state()

    def open(self):
        self.page.goto(f"{self.BASE_URL}{self.ENDPOINT}", timeout=settings.navigation_timeout, wait_until="commit")
        self.wait_for_load_state()

    def check_url(self, endpoint: str = None, timeout: int = None, expected_url: str = None):
        expected_url = expected_url or f"{self.BASE_URL}{endpoint or self.ENDPOINT}"
        expect(self.page).to_have_url(re.compile(rf"{re.escape(expected_url)}(?:#.*)?"),  timeout=timeout or settings.default_timeout)


    def should_be_visible_with_text(self, text: str, selector: str = None, root: Locator | None = None, exact: bool = False):
        locator = root or self.page
        if selector:
            if exact:
                expect(locator.locator(selector)).to_have_text(text)
            else:
                expect(locator.locator(selector).filter(has_text=text)).to_be_visible()

    def get_inner_text(self, selector: str = None, root: Locator | None= None) -> str:
        locator = root or self.page
        if selector:
            return locator.locator(selector).inner_text()
        return locator.inner_text()

    def scroll_to_elem(self, selector: str):
        self.page.locator(selector=selector).scroll_into_view_if_needed()

    def accept_alert(self):
        self.page.once("dialog", lambda dialog: dialog.accept())

    def enter_data(self, selector: str, text: str) -> str:
        self.page.locator(selector=selector).fill(value=text)
        return text

    def enter_file(self, selector: str, path_to_file: str | os.PathLike):
        self.page.locator(selector=selector).set_input_files(path_to_file)

    def not_to_have_url(self, endpoint: str | None = None, timeout: int | None =None):
        expected_url = f"{self.BASE_URL}{endpoint or self.ENDPOINT}"
        expect(self.page).not_to_have_url(re.compile(rf"{re.escape(expected_url)}(?:#.*)?"), timeout=timeout or settings.default_timeout)

    def wait_for_load_state(self, state: str = "networkidle"):
        self.page.wait_for_load_state(state)

    def wait_for_selector_state(self, selector: str):
        self.page.locator(selector=selector).wait_for()

    def elem_should_be_visible(self, selector: str, timeout: int | None = None, root: Locator | None = None) -> Locator:
        locator = root or self.page
        elem = locator.locator(selector).first
        expect(elem).to_be_visible(timeout=timeout or settings.default_timeout)
        return elem

    def select_elem_in_dropdown(self, selector: str, value: Any) -> str | None:
        result = self.page.locator(selector=selector).select_option(value=value)
        return result[0] if result else None

    def get_text_by_locator(self, selector: str, root: Locator | None = None) -> str:
        locator = root or self.page
        return locator.locator(selector).text_content()

    def get_text_by_attribute_for_locator(self, selector: str, attribute: str, root: Locator | None = None) -> str:
        locator = root or self.page
        return locator.locator(selector).get_attribute(attribute)

    def hover(self, selector: str, root: Locator | None = None):
        locator = root or self.page
        locator.locator(selector).hover()

    def _click_and_check_response(self, selector: str, product_id: str, root: Locator | None = None):
        with self.page.expect_response(re.compile(rf"/add_to_cart/{product_id}")) as response_info:
            self.click(selector=selector, root=root)
        assert response_info.value.ok, f"Сервер отвалился при добавлении в корзину! Статус: {response_info.value.status}"

    def add_product_to_cart(self, index: int = 0, selector: str | None = None, is_hover: bool = True) -> int:
        card = self.page.locator(selector=selector or BasePageLocators.CARD_OF_ITEM).nth(index)
        name = self.get_text_by_locator(selector=BasePageLocators.ITEM_NAME, root=card)
        price = self.get_text_by_locator(selector=BasePageLocators.ITEM_PRICE, root=card)
        product_id = self.get_text_by_attribute_for_locator(selector=BasePageLocators.ID_CARD_LOCATOR, root=card, attribute=BasePageLocators.ID_CARD_ATTRIBUTE)

        if is_hover:
            self.hover(selector=BasePageLocators.ADD_TO_CART_BTN, root=card)
            self.elem_should_be_visible(selector=BasePageLocators.PRODUCT_OVERLAY, root=card)
            self._click_and_check_response(BasePageLocators.ADD_TO_CART_BTN_ON_HOVER, product_id, root=card)
        else:
            self._click_and_check_response(BasePageLocators.ADD_TO_CART_BTN, product_id, root=card)

        self.elem_should_be_visible(BasePageLocators.CART_MODAL_AFTER_ADD_PRODUCT)

        self.click(selector=BasePageLocators.CONTINUE_SHOPPING_BTN)
        if product_id in self.cart_items:
            self.cart_items[product_id]["count"] += 1
        else:
            self.cart_items[product_id] = {"name": name, "price": price, "count": 1, "product_id": product_id}
        return int(product_id)

    def get_product_id_from_card(self, index: int = 0, selector: str = None) -> int:
        card = self.page.locator(selector=selector or BasePageLocators.CARD_OF_ITEM).nth(index)
        product_id = self.get_text_by_attribute_for_locator(selector=BasePageLocators.ID_CARD_LOCATOR, root=card, attribute=BasePageLocators.ID_CARD_ATTRIBUTE)
        return int(product_id)

    def assert_equal(self, actual: Any, expected: Any):
        assert actual == expected, f"actual = {actual}, expected = {expected}, actual_type = {type(actual)}, expected = {type(expected)}"

    def assert_contains(self, needle: Any , haystack: Any):
        assert needle in haystack, f"'{needle}' not found in '{haystack}'"

    def should_not_be_visible(self, selector: str):
        expect(self.page.locator(selector)).to_have_count(0)

    def should_be_success_message(self, selector: str, text: str):
        self.should_be_visible_with_text(selector=selector, text=text)

    def open_product_card_detail(self, product_id: int):
        card = self.page.locator(BasePageLocators.CARD_OF_ITEM).filter(has=self.page.locator(BasePageLocators.select_card_by_id(product_id=product_id)))
        self.click_and_wait_network(selector=BasePageLocators.VIEW_PRODUCT_DETAILS_BTN, root=card)


    def click_scroll_up_btn(self):
        self.click(selector=BasePageLocators.SCROLL_UP_BTN)

    def should_be_elem_in_viewport(self, selector: str, visible=True):
        locator = self.page.locator(selector)
        if visible:
            expect(locator).to_be_in_viewport()
        else:
            expect(locator).not_to_be_in_viewport()

    def should_be_visible_left_sidebar(self):
        self.elem_should_be_visible(selector=LeftSidebarLocators.LEFT_SIDEBAR)
        self.elem_should_be_visible(selector=LeftSidebarLocators.CATEGORY)
        self.elem_should_be_visible(selector=LeftSidebarLocators.BRANDS)





