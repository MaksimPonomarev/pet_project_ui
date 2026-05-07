import os
from dotenv import load_dotenv
from ui.pages.base_page import BasePage
from ui.pages.locators import SignupPageLocators
from ui.tools.faker import fake

load_dotenv()


class SignupPage(BasePage):
    ENDPOINT = os.getenv("SIGNUP_ENDPOINT")

    def should_be_signup_page(self):
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
        self.check_url()


    def create_user(self):
        data = fake.date_of_birth()

        self.click(selector=SignupPageLocators.TITLE_MR if fake.title() == 1 else SignupPageLocators.TITLE_MRS)
        name = self.enter_data(selector=SignupPageLocators.NAME, text=fake.name())
        password = self.enter_data(selector=SignupPageLocators.PASSWORD, text=fake.password())
        self.select_elem_in_dropdown(selector=SignupPageLocators.DAYS, value=data["day"])
        self.select_elem_in_dropdown(selector=SignupPageLocators.MONTHS, value=data["month"])
        self.select_elem_in_dropdown(selector=SignupPageLocators.YEAR, value=data["year"])
        self.enter_data(selector=SignupPageLocators.FIRST_NAME, text=fake.first_name())
        self.enter_data(selector=SignupPageLocators.LAST_NAME, text=fake.last_name())
        self.enter_data(selector=SignupPageLocators.COMPANY, text=fake.company())
        self.enter_data(selector=SignupPageLocators.ADDRESS, text=fake.address())
        self.enter_data(selector=SignupPageLocators.ADDRESS2, text=fake.address2())
        self.select_elem_in_dropdown(selector=SignupPageLocators.COUNTRY, value=fake.country())
        self.enter_data(selector=SignupPageLocators.STATE, text=fake.state())
        self.enter_data(selector=SignupPageLocators.CITY, text=fake.city())
        self.enter_data(selector=SignupPageLocators.ZIPCODE, text=fake.zipcode())
        self.enter_data(selector=SignupPageLocators.MOBILE_NUMBER, text=fake.mobile_number())
        self.click(selector=SignupPageLocators.CREATE_ACCOUNT_BTN)
        return {"password": password, "name": name}

    def checking_successful_account_creation(self):
        self.check_url(endpoint="/account_created")
        self.elem_should_be_visible(selector=SignupPageLocators.ACCOUNT_CREATED_MESSAGE)

    def click_continue(self):
        self.click(selector=SignupPageLocators.CONTINUE_BTN)



