import time

import pytest


@pytest.mark.with_cookie_banner
def test_check_accept_cookie_banner(main_page):
    main_page.open()
    main_page.should_be_cookie_banner()
    main_page.accept_cookie_banner()
    main_page.should_not_be_cookie_banner()
    main_page.should_be_main_page()



def test_add_recommended_product(main_page, cart_page):
    main_page.open()
    main_page.should_be_main_page()
    main_page.add_recommended_product()
    main_page.header.go_to_cart()

    cart_page.should_be_filled_cart()
    cart_page.should_be_added_products(cart_items=main_page.cart_items)