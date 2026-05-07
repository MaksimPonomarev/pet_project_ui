import os
from dotenv import load_dotenv
from ui.pages.base_page import BasePage
from ui.pages.locators import ApiPageLocators

load_dotenv()


class ApiListPage(BasePage):
    ENDPOINT = os.getenv("API_ENDPOINT")

    def should_be_api_list_page(self):
        self.first_elem_should_be_visible(selector=ApiPageLocators.PANEL_HEADING)
        self.check_url()