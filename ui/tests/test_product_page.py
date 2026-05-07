import time


def test_check_product_page(products_page):
    products_page.open()
    products_page.should_be_product_page()
    products_page.check_product_card()


