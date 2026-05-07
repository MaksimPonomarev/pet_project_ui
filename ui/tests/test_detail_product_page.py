


def test_check_all_product_detail_page(products_page, detail_products_page):
    products_page.open()
    products_page.should_be_product_page()
    products_page.check_product_card()
    products_page.check_product_card_view_product_btn()
    products_page.open_product_card_detail()
    detail_products_page.should_be_product_detail_page()
