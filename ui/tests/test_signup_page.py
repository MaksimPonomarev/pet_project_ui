import time

from ui.fixtures.page_fixtures import main_page


def test_guest_can_create_account(login_page, signup_page,main_page):
    login_page.open()
    login_page.go_to_signup()
    signup_page.should_be_signup_page()
    signup_page.create_user()
    signup_page.checking_successful_account_creation()
    signup_page.click_continue()
    main_page.should_be_main_page()
    main_page.should_be_logged_in()

def test_login_user_with_correct_email_and_password(login_page, create_account):
    login_page.logout()
    login_page.should_be_logged_out()
    login_page.login(
        email=create_account["email"],
        password=create_account["password"]
    )
    login_page.should_be_logged_in()


def test_login_user_with_incorrect_email_and_password(login_page):
    login_page.open()
    login_page.login(
        email="wrong@email.com",
        password="wrongpassword123"
    )
    login_page.should_be_incorrect_login_error()
    time.sleep(200)

def test_register_user_with_existing_email(login_page, create_account):
    login_page.open()
    login_page.logout()
    login_page.should_be_logged_out()
    login_page.go_to_signup(email=create_account["email"], name=create_account["name"])
    login_page.should_be_incorrect_signup_error()
