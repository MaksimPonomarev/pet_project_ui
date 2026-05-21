from ui.pages.base_page import BasePage
from ui.pages.locators import TestCasesLocators


class TestCasesPage(BasePage):
    ENDPOINT = "/test_cases"

    def should_be_test_cases_page(self):
        
        self.check_url()
        self.elem_should_be_visible(selector=TestCasesLocators.first_TEST_CASE)
