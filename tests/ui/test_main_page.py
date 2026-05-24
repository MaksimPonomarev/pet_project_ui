import pytest

from models.cart_item import CartItem


@pytest.mark.with_cookie_banner
def test_check_accept_cookie_banner(main_page):
    main_page.open()
    main_page.should_be_cookie_banner()
    main_page.accept_cookie_banner()
    main_page.should_not_be_cookie_banner()
    main_page.should_be_main_page()


def test_add_recommended_product(main_page, cart_page):
    expected: dict[str, CartItem] = {}
    main_page.open()
    main_page.should_be_main_page()
    main_page.add_recommended_product(cart_items=expected)
    main_page.header.go_to_cart()

    cart_page.should_be_added_products(expected)