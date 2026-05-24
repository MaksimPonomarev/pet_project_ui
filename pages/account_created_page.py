from pages.base_page import BasePage
from pages.locators import CreatedAccountPageLocators
from test_data.data import SuccessMessageText, Titles


class CreatedAccountPage(BasePage):
    ENDPOINT = "/account_created"

    def should_be_success_created_account(self):
        self.check_url()
        self.should_be_visible_with_text(selector=CreatedAccountPageLocators.ACCOUNT_CREATED_TITLE, text=Titles.CREATED_ACCOUNT)
        self.should_be_visible_with_text(selector=CreatedAccountPageLocators.SUCCESS_MESSAGE, text=SuccessMessageText.CREATED_ACCOUNT)

    def click_continue_on_created_account_page(self):
        self.click_and_wait_network(selector=CreatedAccountPageLocators.CONTINUE_BTN)

