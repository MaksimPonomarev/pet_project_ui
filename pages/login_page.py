from pages.base_page import BasePage
from pages.locators import LoginPageLocators
from test_data.data import ErrorMessageText
from tools.faker import fake


class LoginPage(BasePage):
    ENDPOINT = "/login"

    def should_be_login_page(self):
        self.check_url()
        self._should_be_login_form_visible()
        self._should_be_signup_form_visible()

    def _should_be_login_form_visible(self):
        self.elem_should_be_visible(selector=LoginPageLocators.LOGIN_FORM)
        self.elem_should_be_visible(selector=LoginPageLocators.LOGIN_EMAIL_AREA)
        self.elem_should_be_visible(selector=LoginPageLocators.LOGIN_PASSWORD_AREA)
        self.elem_should_be_visible(selector=LoginPageLocators.LOGIN_BTN)

    def _should_be_signup_form_visible(self):
        self.elem_should_be_visible(selector=LoginPageLocators.SIGNUP_FORM)
        self.elem_should_be_visible(selector=LoginPageLocators.SIGNUP_NAME_AREA)
        self.elem_should_be_visible(selector=LoginPageLocators.SIGNUP_EMAIL_AREA)
        self.elem_should_be_visible(selector=LoginPageLocators.SIGNUP_BTN)

    def go_to_signup(self, email: str = None, name: str = None):
        email = email or fake.email()
        name = name or fake.name()
        self.enter_data(selector=LoginPageLocators.SIGNUP_EMAIL_AREA, text=email)
        self.enter_data(selector=LoginPageLocators.SIGNUP_NAME_AREA, text=name)
        self.click(selector=LoginPageLocators.SIGNUP_BTN)

    def login(self, email: str, password: str):
        self.enter_data(selector=LoginPageLocators.LOGIN_EMAIL_AREA, text=email)
        self.enter_data(selector=LoginPageLocators.LOGIN_PASSWORD_AREA, text=password)
        self.click(selector=LoginPageLocators.LOGIN_BTN)

    def should_be_incorrect_login_error(self):
        self.should_be_visible_with_text(ErrorMessageText.INCORRECT_LOGIN_ERROR)

    def should_be_incorrect_signup_error(self):
        self.should_be_visible_with_text(ErrorMessageText.INCORRECT_SIGNUP_ERROR)