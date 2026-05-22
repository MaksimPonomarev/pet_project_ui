import time

import pytest

from ui.fixtures.page_fixtures import main_page
from ui.test_data.data import SearchData


def test_check_product_page(products_page):
    products_page.open()
    products_page.should_be_product_page()



@pytest.mark.parametrize("name", SearchData.VALID_PRODUCTS)
def test_check_search_product(products_page, name):
    products_page.open()
    products_page.should_be_product_page()
    products_page.enter_and_submit_search(name_of_product=name)
    products_page.check_all_results_search_product(name_of_product=name)


def test_check_filled_cart_after_login(products_page, cart_page, login_page, main_page, user):
    user_data = user
    products_page.open()
    products_page.should_be_product_page()
    products_page.add_product_to_cart()
    products_page.header.go_to_cart()

    cart_page.should_be_added_products(products_page.cart_items)
    cart_page.header.go_to_login()

    login_page.should_be_login_page()
    login_page.login(
        email=user_data.email,
        password=user_data.password
    )

    main_page.should_be_main_page()
    main_page.header.should_be_logged_in()
    main_page.header.go_to_cart()

    cart_page.should_be_added_products(products_page.cart_items)