import pytest
from pages.account_created_page import CreatedAccountPage
from pages.api_page import ApiListPage
from pages.brand_page import BrandProductPage
from pages.cart_page import CartPage
from pages.category_products_page import CategoryProductPage
from pages.checkout_page import CheckoutPage
from pages.contact_us_page import ContactUsPage
from pages.delete_account_page import DeletedAccountPage
from pages.detail_product_page import DetailProductsPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.payment_done_page import PaymentDonePage
from pages.payment_page import PaymentPage
from pages.products_page import ProductsPage
from pages.signup_page import SignupPage
from pages.testcases_page import TestCasesPage


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
    return DeletedAccountPage(page)
    

@pytest.fixture
def created_account_page(page):
    return CreatedAccountPage(page)
    

@pytest.fixture
def category_product_page(page):
    return CategoryProductPage(page)
    

@pytest.fixture
def brand_product_page(page):
    return BrandProductPage(page)
    
