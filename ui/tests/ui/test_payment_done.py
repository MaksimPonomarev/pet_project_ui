

def test_download_invoice(logged_in_user, main_page, cart_page, checkout_page, payment_page, payment_done_page):
    main_page.should_be_main_page()
    main_page.add_product_to_cart()
    main_page.header.go_to_cart()

    cart_page.should_be_added_products(cart_items=main_page.cart_items)
    cart_page.click_checkout_btn()

    checkout_page.should_be_checkout_page()
    checkout_page.check_orders_details(user_data=logged_in_user)
    checkout_page.click_place_order()

    payment_page.should_be_payment_page()
    payment_page.fill_and_submit_payment_form()

    payment_done_page.should_be_payment_done_page()
    file_info = payment_done_page.download_invoice()
    payment_done_page.should_be_downloaded_file(file_info=file_info)