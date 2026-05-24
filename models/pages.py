from dataclasses import dataclass
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


@dataclass
class Pages:
    main: MainPage
    signup: SignupPage
    login: LoginPage
    contact_us: ContactUsPage
    cases_of_test: TestCasesPage
    products: ProductsPage
    detail_products: DetailProductsPage
    cart: CartPage
    api_list: ApiListPage
    checkout: CheckoutPage
    payment: PaymentPage
    payment_done: PaymentDonePage
    deleted_account: DeletedAccountPage
    created_account: CreatedAccountPage
    category_product: CategoryProductPage
    brand_product: BrandProductPage