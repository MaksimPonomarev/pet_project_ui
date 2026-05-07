import os
from dotenv import load_dotenv
from ui.pages.base_page import BasePage
from ui.pages.locators import SignupPageLocators, TestCasesLocators
from ui.tools.faker import fake

load_dotenv()


class TestCasesPage(BasePage):
    ENDPOINT = os.getenv("TEST_CASES_ENDPOINT")

    def should_be_test_cases_page(self):
        self.first_elem_should_be_visible(selector=TestCasesLocators.first_TEST_CASE)
        self.check_url()