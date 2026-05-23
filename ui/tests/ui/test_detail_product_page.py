

def test_check_product_detail_page(products_page, detail_products_page):
    products_page.open()
    products_page.should_be_product_page()
    product_id = products_page.get_product_id_from_card()
    products_page.open_product_card_detail(product_id=product_id)

    detail_products_page.should_be_product_detail_page(product_id=product_id)


def test_send_review_on_product(products_page, detail_products_page, account_user_info):
    products_page.open()
    products_page.should_be_product_page()
    product_id = products_page.get_product_id_from_card()
    products_page.open_product_card_detail(product_id=product_id)
    detail_products_page.should_be_product_detail_page(product_id=product_id)
    detail_products_page.fill_and_send_review_form(user_info=account_user_info)
    detail_products_page.should_be_success_message_after_send_review_product()