

def test_guest_can_create_account(login_page, signup_page,main_page, created_account_page, account_user_info):
    login_page.open()
    login_page.should_be_login_page()
    login_page.go_to_signup()
    signup_page.should_be_signup_page()
    signup_page.fill_and_send_signup_form(user_data=account_user_info)
    created_account_page.should_be_success_created_account()
    signup_page.click_continue_on_signup_page()
    main_page.should_be_main_page()
    main_page.header.should_be_logged_in()


def test_login_user_with_correct_email_and_password(login_page, user_with_cleanup):
    login_page.open()
    login_page.should_be_login_page()
    login_page.login(
        email=user_with_cleanup.email,
        password=user_with_cleanup.password
    )
    login_page.header.should_be_logged_in()


def test_login_user_with_incorrect_email_and_password(login_page):
    login_page.open()
    login_page.login(
        email="wrong@email.com",
        password="wrongpassword123"
    )
    login_page.should_be_incorrect_login_error()


def test_register_user_with_existing_email(login_page, user_with_cleanup):
    login_page.open()
    login_page.should_be_login_page()
    login_page.go_to_signup(
        email=user_with_cleanup.email,
        name=user_with_cleanup.email)
    login_page.should_be_incorrect_signup_error()


