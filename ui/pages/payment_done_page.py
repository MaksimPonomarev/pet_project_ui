from ui.pages.base_page import BasePage
from ui.pages.locators import PaymentDonePageLocators, BasePageLocators
from ui.test_data.data import SuccessMessageText
from pathlib import Path


class PaymentDonePage(BasePage):
    ENDPOINT = "/payment_done"

    def should_be_payment_done_page(self):
        
        self.check_url()
        self.should_be_success_message(selector=PaymentDonePageLocators.ORDER_PLACED, text=SuccessMessageText.PLACE_ORDER)
        self.elem_should_be_visible(selector=PaymentDonePageLocators.DOWNLOAD_INVOICE_BTN)
        self.elem_should_be_visible(selector=BasePageLocators.CONTINUE_BTN)

    def download_invoice(self):
        with self.page.expect_download() as download_info:
            self.click(selector=PaymentDonePageLocators.DOWNLOAD_INVOICE_BTN)

        return download_info.value.path()

    def should_be_downloaded_file(self, file_info: Path):
        assert file_info is not None
        assert file_info.stat().st_size > 0
