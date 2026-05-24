from models.cart_item import CartItem


def test_register_while_checkout(pages, account_user_info):
    expected: dict[str, CartItem] = {}
    pages.main.open()
    pages.main.should_be_main_page()
    pages.main.add_product_to_cart(cart_items=expected)
    
    pages.main.header.go_to_cart()

    pages.cart.should_be_added_products(cart_items=expected)
    pages.cart.header.go_to_login()

    pages.login.should_be_login_page()

    pages.login.go_to_signup()
    pages.signup.should_be_signup_page()

    pages.signup.fill_and_send_signup_form(user_data=account_user_info)
    pages.created_account.should_be_success_created_account()

    pages.created_account.click_continue_on_created_account_page()

    pages.main.should_be_main_page()
    pages.main.header.should_be_logged_in()
    pages.main.header.go_to_cart()

    pages.cart.click_checkout_btn()

    pages.checkout.should_be_checkout_page()
    pages.checkout.check_orders_details(user_data=account_user_info)
    pages.checkout.fill_comment()
    pages.checkout.click_place_order()

    pages.payment.should_be_payment_page()
    pages.payment.fill_and_submit_payment_form()

    pages.payment_done.should_be_payment_done_page()
    file_info = pages.payment_done.download_invoice()
    pages.payment_done.should_be_downloaded_file(file_info=file_info)
    pages.payment_done.click_continue_on_payment_done_page()

    pages.main.should_be_main_page()
    pages.main.header.delete_account()

    pages.deleted_account.should_be_deleted_account_page()
    pages.deleted_account.click_continue_on_deleted_account_page()

    pages.main.should_be_main_page()


def test_register_before_checkout(pages, account_user_info):
    expected: dict[str, CartItem] = {}
    pages.main.open()
    pages.main.should_be_main_page()

    pages.main.header.go_to_login()

    pages.login.should_be_login_page()
    pages.login.go_to_signup()

    pages.signup.should_be_signup_page()

    pages.signup.fill_and_send_signup_form(account_user_info)
    pages.created_account.should_be_success_created_account()
    pages.created_account.click_continue_on_created_account_page()

    pages.main.should_be_main_page()
    pages.main.header.should_be_logged_in()
    pages.main.add_product_to_cart(cart_items=expected)
    
    pages.main.header.go_to_cart()

    pages.cart.should_be_added_products(cart_items=expected)

    pages.cart.click_checkout_btn()

    pages.checkout.should_be_checkout_page()
    pages.checkout.check_orders_details(user_data=account_user_info)
    pages.checkout.fill_comment()
    pages.checkout.click_place_order()

    pages.payment.should_be_payment_page()
    pages.payment.fill_and_submit_payment_form()

    pages.payment_done.should_be_payment_done_page()
    pages.payment_done.header.delete_account()

    pages.deleted_account.should_be_deleted_account_page()
    pages.deleted_account.click_continue_on_deleted_account_page()

    pages.main.should_be_main_page()


def test_login_before_checkout(user, pages):
    expected: dict[str, CartItem] = {}
    user_data = user
    pages.main.open()
    pages.main.should_be_main_page()
    pages.main.header.go_to_login()

    pages.login.should_be_login_page()
    pages.login.login(
        email=user_data.email,
        password=user_data.password
    )
    pages.login.header.should_be_logged_in()
    pages.login.header.go_to_products()

    pages.products.should_be_product_page()
    pages.products.add_product_to_cart(cart_items=expected)
    
    pages.products.header.go_to_cart()

    pages.cart.should_be_added_products(cart_items=expected)
    pages.cart.click_checkout_btn()

    pages.checkout.should_be_checkout_page()
    pages.checkout.check_orders_details(user_data)
    pages.checkout.fill_comment()
    pages.checkout.click_place_order()

    pages.payment.should_be_payment_page()
    pages.payment.fill_and_submit_payment_form()

    pages.payment_done.should_be_payment_done_page()
    pages.payment_done.header.delete_account()

    pages.deleted_account.should_be_deleted_account_page()
    pages.deleted_account.click_continue_on_deleted_account_page()

    pages.main.should_be_main_page()

