import time


def test_contact_us_form(contact_us_page, main_page):
    contact_us_page.open()
    contact_us_page.should_be_contact_us_page()

    contact_us_page.submit_contact_form()
    contact_us_page.should_be_success_message_send_feedback()
    contact_us_page.click_home_btn_after_submit()
    main_page.should_be_main_page()
