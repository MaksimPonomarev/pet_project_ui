import time

import pytest


@pytest.fixture
def filled_cart(products_page):
    products_page.open()
    products_page.add_first_product_to_cart()
    products_page.go_to_home()

