from pages.base_page import BasePage
from pages.locators import DeletedAccountPageLocators, BasePageLocators
from test_data.data import SuccessMessageText, Titles


class DeletedAccountPage(BasePage):
    ENDPOINT = "/delete_account"

    def should_be_deleted_account_page(self):
        self.check_url()
        self.should_be_visible_with_text(selector=DeletedAccountPageLocators.ACCOUNT_DELETED_BLOCK, text=Titles.DELETED_ACCOUNT)
        self.should_be_visible_with_text(selector=DeletedAccountPageLocators.ACCOUNT_DELETED_BLOCK, text=SuccessMessageText.DELETED_ACCOUNT)
        self.header.should_be_logged_out()

    def click_continue_on_deleted_account_page(self):
        self.click_and_wait_network(selector=BasePageLocators.CONTINUE_BTN)
