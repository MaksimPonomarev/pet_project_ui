import pytest
from ui.pages.account_created_page import CreatedAccountPage
from ui.pages.api_page import ApiListPage
from ui.pages.brand_page import BrandProductPage
from ui.pages.cart_page import CartPage
from ui.pages.category_products_page import CategoryProductPage
from ui.pages.checkout_page import CheckoutPage
from ui.pages.contact_us_page import ContactUsPage
from ui.pages.delete_account_page import DeleteAccountPage
from ui.pages.detail_product_page import DetailProductsPage
from ui.pages.login_page import LoginPage
from ui.pages.main_page import MainPage
from ui.pages.payment_done_page import PaymentDonePage
from ui.pages.payment_page import PaymentPage
from ui.pages.products_page import ProductsPage
from ui.pages.signup_page import SignupPage
from ui.pages.testcases_page import TestCasesPage


@pytest.fixture
def main_page(page):
    return MainPage(page)


@pytest.fixture
def signup_page(page):
    return SignupPage(page)


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def contact_us_page(page):
    return ContactUsPage(page)
    

@pytest.fixture
def cases_of_test_page(page):
    return TestCasesPage(page)
    

@pytest.fixture
def products_page(page):
    return ProductsPage(page)
    

@pytest.fixture
def detail_products_page(page):
    return DetailProductsPage(page)
    

@pytest.fixture
def cart_page(page):
    return CartPage(page)
    

@pytest.fixture
def api_list_page(page):
    return ApiListPage(page)
    

@pytest.fixture
def checkout_page(page):
    return CheckoutPage(page)
    

@pytest.fixture
def payment_page(page):
    return PaymentPage(page)
    

@pytest.fixture
def payment_done_page(page):
    return PaymentDonePage(page)
    

@pytest.fixture
def deleted_account_page(page):
    return DeleteAccountPage(page)
    

@pytest.fixture
def created_account_page(page):
    return CreatedAccountPage(page)
    

@pytest.fixture
def category_product_page(page):
    return CategoryProductPage(page)
    

@pytest.fixture
def brand_product_page(page):
    return BrandProductPage(page)
    
