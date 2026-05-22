import time

from ui.fixtures.page_fixtures import created_account_page


def test_register_while_checkout(account_user_info, products_page, main_page, cart_page, login_page, signup_page, checkout_page, payment_page, payment_done_page, deleted_account_page, created_account_page):
    main_page.open()
    main_page.should_be_main_page()
    main_page.add_product_to_cart()
    main_page.header.go_to_cart()

    cart_page.should_be_filled_cart()
    cart_page.should_be_added_products(cart_items=main_page.cart_items)
    cart_page.go_to_login_page_from_checkout_form()

    login_page.should_be_login_page()

    login_page.go_to_signup()
    signup_page.should_be_signup_page()

    signup_page.fill_signup_form(user_data=account_user_info)
    created_account_page.should_be_success_created_account()

    created_account_page.click_continue()

    main_page.should_be_main_page()
    main_page.header.should_be_logged_in()
    main_page.header.go_to_cart()

    cart_page.click_checkout_btn()

    checkout_page.should_be_checkout_page()
    checkout_page.check_orders_details(user_data=account_user_info)
    checkout_page.fill_comment()
    checkout_page.click_place_order()

    payment_page.should_be_payment_page()
    payment_page.fill_and_submit_payment_form()

    payment_done_page.should_be_payment_done_page()
    file_info = payment_done_page.download_invoice()
    payment_done_page.should_be_downloaded_file(file_info=file_info)
    payment_done_page.header.delete_account()

    deleted_account_page.should_be_deleted_account_page()
    deleted_account_page.click_continue()

    main_page.should_be_main_page()


def test_register_before_checkout(account_user_info, products_page, main_page, created_account_page, cart_page, login_page, signup_page, checkout_page, payment_page, payment_done_page, deleted_account_page):
    main_page.open()
    main_page.should_be_main_page()

    main_page.header.go_to_login()

    login_page.should_be_login_page()
    login_page.go_to_signup()

    signup_page.should_be_signup_page()

    signup_page.fill_signup_form(account_user_info)
    created_account_page.should_be_success_created_account()
    created_account_page.click_continue()

    main_page.should_be_main_page()
    main_page.header.should_be_logged_in()
    main_page.add_product_to_cart()
    main_page.header.go_to_cart()

    cart_page.should_be_filled_cart()
    cart_page.should_be_added_products(cart_items=main_page.cart_items)

    cart_page.click_checkout_btn()

    checkout_page.should_be_checkout_page()
    checkout_page.check_orders_details(user_data=account_user_info)
    checkout_page.fill_comment()
    checkout_page.click_place_order()

    payment_page.should_be_payment_page()
    payment_page.fill_and_submit_payment_form()

    payment_done_page.should_be_payment_done_page()
    payment_done_page.header.delete_account()

    deleted_account_page.should_be_deleted_account_page()
    deleted_account_page.click_continue()

    main_page.should_be_main_page()


def test_login_before_checkout(user,  deleted_account_page, payment_done_page, payment_page, checkout_page, main_page, login_page, products_page, cart_page):
    user_data = user
    main_page.open()
    main_page.should_be_main_page()
    main_page.header.go_to_login()

    login_page.should_be_login_page()
    login_page.login(
        email=user_data.email,
        password=user_data.password
    )
    login_page.header.should_be_logged_in()
    login_page.header.go_to_products()

    products_page.should_be_product_page()
    products_page.add_product_to_cart()
    products_page.header.go_to_cart()

    cart_page.should_be_filled_cart()
    cart_page.should_be_added_products(cart_items=products_page.cart_items)
    cart_page.click_checkout_btn()

    checkout_page.should_be_checkout_page()
    checkout_page.check_orders_details(user_data)
    checkout_page.fill_comment()
    checkout_page.click_place_order()

    payment_page.should_be_payment_page()
    payment_page.fill_and_submit_payment_form()

    payment_done_page.should_be_payment_done_page()
    payment_done_page.header.delete_account()

    deleted_account_page.should_be_deleted_account_page()
    deleted_account_page.click_continue()

    main_page.should_be_main_page()

