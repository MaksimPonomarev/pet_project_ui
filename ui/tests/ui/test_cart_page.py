import time


def test_add_product_in_cart(products_page, cart_page):
    products_page.open()
    products_page.should_be_product_page()
    products_page.add_product_to_cart(index=1)
    products_page.add_product_to_cart(index=2)
    products_page.header.go_to_cart()
    cart_page.should_be_added_products(cart_items=products_page.cart_items)

def test_add_same_product_twice(products_page, cart_page):
    products_page.open()
    products_page.should_be_product_page()
    products_page.add_product_to_cart(index=1)
    products_page.add_product_to_cart(index=1)
    products_page.header.go_to_cart()
    cart_page.should_be_added_products(cart_items=products_page.cart_items)


def test_check_product_quantity_in_cart(products_page, detail_products_page, cart_page):
    products_page.open()
    products_page.should_be_product_page()
    product_id = products_page.get_product_id_from_card()
    products_page.open_product_card_detail(product_id=product_id)

    detail_products_page.should_be_product_detail_page(product_id=product_id)
    detail_products_page.enter_quantity_for_product(quantity=4)
    detail_products_page.add_detail_product_to_cart()
    detail_products_page.header.go_to_cart()

    cart_page.should_be_filled_cart()
    cart_page.check_quantity(item_id=product_id, expect_quantity=4)


def test_remove_product_from_cart(products_page, cart_page):
    products_page.open()
    products_page.should_be_product_page()
    first_product_id = products_page.add_product_to_cart()
    products_page.header.go_to_cart()

    cart_page.should_be_filled_cart()
    cart_page.should_be_added_products(cart_items=products_page.cart_items)
    cart_page.delete_product_by_id(product_id=first_product_id)
    cart_page.should_be_empty_cart()
    cart_page.should_not_be_visible_elem_by_id(product_id=first_product_id)