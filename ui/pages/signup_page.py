from ui.pages.base_page import BasePage
from ui.pages.locators import SignupPageLocators
from ui.test_data.factories import UserData

class SignupPage(BasePage):
    ENDPOINT = "/signup"

    def should_be_signup_page(self):
        self.check_url()
        self.elem_should_be_visible(selector=SignupPageLocators.TITLE_MR)
        self.elem_should_be_visible(selector=SignupPageLocators.TITLE_MRS)
        self.elem_should_be_visible(selector=SignupPageLocators.NAME)
        self.elem_should_be_visible(selector=SignupPageLocators.PASSWORD)
        self.elem_should_be_visible(selector=SignupPageLocators.DAYS)
        self.elem_should_be_visible(selector=SignupPageLocators.MONTHS)
        self.elem_should_be_visible(selector=SignupPageLocators.YEAR)
        self.elem_should_be_visible(selector=SignupPageLocators.FIRST_NAME)
        self.elem_should_be_visible(selector=SignupPageLocators.LAST_NAME)
        self.elem_should_be_visible(selector=SignupPageLocators.COMPANY)
        self.elem_should_be_visible(selector=SignupPageLocators.ADDRESS)
        self.elem_should_be_visible(selector=SignupPageLocators.ADDRESS2)
        self.elem_should_be_visible(selector=SignupPageLocators.COUNTRY)
        self.elem_should_be_visible(selector=SignupPageLocators.STATE)
        self.elem_should_be_visible(selector=SignupPageLocators.CITY)
        self.elem_should_be_visible(selector=SignupPageLocators.ZIPCODE)
        self.elem_should_be_visible(selector=SignupPageLocators.MOBILE_NUMBER)
        self.elem_should_be_visible(selector=SignupPageLocators.CREATE_ACCOUNT_BTN)


    def fill_and_send_signup_form(self, user_data: UserData):
        self.click(selector=SignupPageLocators.TITLE_MR if user_data.title == "mr" else SignupPageLocators.TITLE_MRS)
        self.enter_data(selector=SignupPageLocators.NAME, text=user_data.name)
        self.enter_data(selector=SignupPageLocators.PASSWORD, text=user_data.password)
        self.select_elem_in_dropdown(selector=SignupPageLocators.DAYS, value=user_data.day)
        self.select_elem_in_dropdown(selector=SignupPageLocators.MONTHS, value=user_data.month)
        self.select_elem_in_dropdown(selector=SignupPageLocators.YEAR, value=user_data.year)
        self.enter_data(selector=SignupPageLocators.FIRST_NAME, text=user_data.first_name)
        self.enter_data(selector=SignupPageLocators.LAST_NAME, text=user_data.last_name)
        self.enter_data(selector=SignupPageLocators.COMPANY, text=user_data.company)
        self.enter_data(selector=SignupPageLocators.ADDRESS, text=user_data.address)
        self.enter_data(selector=SignupPageLocators.ADDRESS2, text=user_data.address2)
        self.select_elem_in_dropdown(selector=SignupPageLocators.COUNTRY, value=user_data.country)
        self.enter_data(selector=SignupPageLocators.STATE, text=user_data.state)
        self.enter_data(selector=SignupPageLocators.CITY, text=user_data.city)
        self.enter_data(selector=SignupPageLocators.ZIPCODE, text=user_data.zipcode)
        self.enter_data(selector=SignupPageLocators.MOBILE_NUMBER, text=user_data.mobile_number)
        self.click(selector=SignupPageLocators.CREATE_ACCOUNT_BTN)

    def click_continue_on_signup_page(self):
        self.click_and_wait_network(selector=SignupPageLocators.CONTINUE_BTN)

