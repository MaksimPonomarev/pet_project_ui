from ui.pages.base_page import BasePage
from ui.pages.locators import DeleteAccountPageLocators, BasePageLocators
from ui.test_data.data import SuccessMessageText, Titles


class DeleteAccountPage(BasePage):
    ENDPOINT = "/delete_account"

    def should_be_deleted_account_page(self):
        
        self.check_url()
        self.should_be_visible_with_text(selector=DeleteAccountPageLocators.ACCOUNT_DELETED_BLOCK, text=Titles.DELETED_ACCOUNT)
        self.should_be_visible_with_text(selector=DeleteAccountPageLocators.ACCOUNT_DELETED_BLOCK, text=SuccessMessageText.DELETED_ACCOUNT)
        self.header.should_be_logged_out()


    def click_continue(self):
        self.click(selector=BasePageLocators.CONTINUE_BTN)
