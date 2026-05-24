import pytest


def test_check_site_header(main_page):
    main_page.open()
    main_page.header.should_be_header ()


def test_logout(login_page, main_page, user_with_cleanup):
    user_data = user_with_cleanup
    login_page.open()
    login_page.login(
        email=user_data.email,
        password=user_data.password
    )
    login_page.header.should_be_logged_in()
    login_page.header.logout()
    main_page.header.should_be_logged_out()

def test_user_can_delete_account(main_page, logged_in_user, deleted_account_page):
    main_page.header.should_be_logged_in()
    main_page.header.delete_account()
    deleted_account_page.should_be_deleted_account_page()


def test_go_to_products_page(main_page, products_page):
    main_page.open()
    main_page.should_be_main_page()
    main_page.header.go_to_products()

    products_page.should_be_product_page()


def test_go_to_cart_page(main_page, cart_page):
    main_page.open()
    main_page.should_be_main_page()
    main_page.header.go_to_cart()

    cart_page.should_be_empty_cart()


def test_go_to_filled_cart_page(main_page,cart_page):
    main_page.open()
    main_page.should_be_main_page()
    main_page.add_product_to_cart()
    main_page.header.go_to_cart()

    cart_page.should_be_added_products(cart_items=main_page.cart_items)


def test_go_to_login_page(main_page, login_page):
    main_page.open()
    main_page.should_be_main_page()
    main_page.header.go_to_login()

    login_page.should_be_login_page()


def test_go_to_test_cases_page(main_page, cases_of_test_page):
    main_page.open()
    main_page.should_be_main_page()
    main_page.header.go_to_test_cases()

    cases_of_test_page.should_be_test_cases_page()


def test_go_to_api_page(main_page, api_list_page):
    main_page.open()
    main_page.should_be_main_page()
    main_page.header.go_to_api_list()

    api_list_page.should_be_api_list_page()


def test_go_to_contact_us(main_page, contact_us_page):
    main_page.open()
    main_page.should_be_main_page()
    main_page.header.go_to_contact_us()

    contact_us_page.should_be_contact_us_page()


def test_go_to_video_tutorials(main_page):
    main_page.open()
    main_page.should_be_main_page()
    main_page.header.go_to_video_tutorials()
    main_page.should_be_redirect_on_youtube()



def test_go_to_details_product_from_main_page(main_page, detail_products_page):
    main_page.open()
    main_page.should_be_main_page()
    product_id = main_page.get_product_id_from_card()
    main_page.open_product_card_detail(product_id=product_id)

    detail_products_page.should_be_product_detail_page(product_id=product_id)


@pytest.mark.parametrize("page_fixture", ["main_page", "cart_page"])
def test_check_footer(page_fixture, request):
    page = request.getfixturevalue(page_fixture)
    page.open()
    page.footer.should_be_footer()
    page.footer.fill_and_submit_subscribe_form()
    page.footer.should_be_subscribe_success_message ()


def test_scroll_button(main_page):
    main_page.open()
    main_page.should_be_main_page()
    main_page.header.should_be_header_visible(visible=True)
    main_page.footer.scroll_to_footer()
    main_page.header.should_be_header_visible(visible=False)
    main_page.click_scroll_up_btn()
    main_page.header.should_be_header_visible(visible=True)