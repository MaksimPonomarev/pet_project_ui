

def test_check_accept_cookie_banner(main_page_without_context):
    main_page_without_context.open()
    main_page_without_context.should_be_cookie_banner()
    main_page_without_context.accept_cookie_banner()
    main_page_without_context.should_be_main_page()




