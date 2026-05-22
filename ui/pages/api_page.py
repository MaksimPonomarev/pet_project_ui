from ui.pages.base_page import BasePage
from ui.pages.locators import ApiPageLocators


class ApiListPage(BasePage):
    ENDPOINT = "/api_list"

    def should_be_api_list_page(self):
        self.check_url()
        self.elem_should_be_visible(selector=ApiPageLocators.PANEL_HEADING)
