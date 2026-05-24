# ── shared / reusable ─────────────────────────────────────────────────────────

class NavLocators:
    HEADER = "#header"
    IMG_LOGO_SITE = "img[src='/static/images/home/logo.png']"

    HOME_LINK = "li a[href='/']"
    PRODUCTS_LINK = "li a[href='/products']"
    CART_LINK = "li a[href='/view_cart']"
    LOGIN_LINK = "li a[href='/login']"
    TEST_CASES_LINK = "li a[href='/test_cases']"
    API_LIST_LINK = "li a[href='/api_list']"
    VIDEO_TUTORIALS_LINK = "li a[href='https://www.youtube.com/c/AutomationExercise']"
    CONTACT_US_LINK = "li a[href='/contact_us']"

    LOGOUT_LINK = "li a[href='/logout']"
    DELETE_ACCOUNT_LINK = "li a[href='/delete_account']"


class FooterLocators:
    FOOTER = "#footer .single-widget"
    FOOTER_TITLE = "#footer .single-widget h2"
    FOOTER_EMAIL = "#susbscribe_email"
    FOOTER_SUBSCRIBE_BTN = "#subscribe"
    FOOTER_SUCCESS_SUBSCRIBE_MESSAGE = "#success-subscribe"


class ProductCardLocators:
    CARD_OF_ITEM = ".product-image-wrapper"
    IMAGE_OF_CARD = "img[src]"

    ADD_TO_CART_BTN = ".productinfo .add-to-cart"
    ADD_TO_CART_BTN_ON_HOVER = ".overlay-content .add-to-cart"
    CART_MODAL_AFTER_ADD_PRODUCT = "#cartModal"
    ITEM_PRICE = ".productinfo h2"
    ITEM_NAME = ".productinfo p"
    VIEW_PRODUCT_DETAILS_BTN = ".nav-pills.nav-justified a"
    TITLE = ".title.text-center"

    PRODUCT_OVERLAY = ".product-overlay"
    ID_CARD_LOCATOR = ".productinfo a"
    ID_CARD_ATTRIBUTE = "data-product-id"

    @staticmethod
    def select_card_by_id(product_id: int) -> str:
        return f"[data-product-id='{product_id}']"


class CartItemLocators:
    CART_INFO = "#cart_info"

    @staticmethod
    def id_card(product_id: str) -> str:
        return f"#product-{product_id}"

    @staticmethod
    def product_price(product_id: str) -> str:
        return f"#product-{product_id} .cart_price p"

    @staticmethod
    def product_total_price(product_id: str) -> str:
        return f"#product-{product_id} .cart_total_price"

    @staticmethod
    def product_quantity(product_id: str) -> str:
        return f"#product-{product_id} .cart_quantity"

    @staticmethod
    def product_name(product_id: str) -> str:
        return f"#product-{product_id} .cart_description h4"

    @staticmethod
    def product_category(product_id: str) -> str:
        return f"#product-{product_id} .cart_description p"


class LeftSidebarLocators:
    LEFT_SIDEBAR = ".left-sidebar"
    CATEGORY = ".category-products#accordian"
    BRANDS = ".brands_products"

    @staticmethod
    def category_group(category: str) -> str:
        return f"[data-parent='#accordian'][href='#{category}']"

    @staticmethod
    def opened_category_group(category) -> str:
        return f"#{category.value}.in"

    @staticmethod
    def brand_item(brand: str) -> str:
        return f"li a[href='/brand_products/{brand}']"

    @staticmethod
    def subcategory(subcategory: int) -> str:
        return f"li a[href='/category_products/{subcategory}']"


# ── base page ─────────────────────────────────────────────────────────────────

class BasePageLocators(NavLocators, FooterLocators, ProductCardLocators):
    BREADCRUMB = ".breadcrumb"
    CONTINUE_BTN = "[data-qa='continue-button']"
    CONTINUE_SHOPPING_BTN = ".modal.show .close-modal"
    SCROLL_UP_BTN = "#scrollUp"


# ── page-specific ─────────────────────────────────────────────────────────────

class MainPageLocators(BasePageLocators):
    CAROUSEL_SLIDER = "#slider-carousel.carousel.slide"
    COOKIE_BANNER = "div.fc-dialog.fc-choice-dialog"
    ACCEPT_COOKIE_BANNER_BTN = ".fc-cta-consent.fc-primary-button"
    RECOMMENDED_ITEMS_BLOCK = ".recommended_items"
    RECOMMENDED_ITEMS_LIST = ".item.active .col-sm-4"


class LoginPageLocators(BasePageLocators):
    LOGIN_FORM = ".login-form"
    LOGIN_EMAIL_AREA = "[data-qa=login-email]"
    LOGIN_PASSWORD_AREA = "[data-qa=login-password]"
    LOGIN_BTN = "[data-qa=login-button]"

    SIGNUP_FORM = ".signup-form"
    SIGNUP_NAME_AREA = "[data-qa=signup-name]"
    SIGNUP_EMAIL_AREA = "[data-qa=signup-email]"
    SIGNUP_BTN = "[data-qa=signup-button]"


class SignupPageLocators(BasePageLocators):
    TITLE_MR = "[data-qa=title] #id_gender1"
    TITLE_MRS = "[data-qa=title] #id_gender2"
    NAME = "[data-qa=name]"
    PASSWORD = "[data-qa=password]"
    DAYS = "[data-qa=days]"
    MONTHS = "[data-qa=months]"
    YEAR = "[data-qa=years]"

    FIRST_NAME = "[data-qa=first_name]"
    LAST_NAME = "[data-qa=last_name]"
    COMPANY = "[data-qa=company]"
    ADDRESS = "[data-qa=address]"
    ADDRESS2 = "[data-qa=address2]"
    COUNTRY = "[data-qa=country]"
    STATE = "[data-qa=state]"
    CITY = "[data-qa=city]"
    ZIPCODE = "[data-qa=zipcode]"
    MOBILE_NUMBER = "[data-qa=mobile_number]"
    CREATE_ACCOUNT_BTN = "[data-qa=create-account]"


class CreatedAccountPageLocators(BasePageLocators):
    ACCOUNT_CREATED_TITLE = "[data-qa=account-created]"
    SUCCESS_MESSAGE = "#form .col-sm-9.col-sm-offset-1"

class ContactUsPageLocators(BasePageLocators):
    NAME = "[data-qa=name]"
    EMAIL = "[data-qa=email]"
    SUBJECT = "[data-qa=subject]"
    MESSAGE = "[data-qa=message]"
    INPUT_FILE = "input[type=file]"
    SUBMIT_BTN = "[data-qa=submit-button]"
    SUCCESS_MESSAGE_LOCATOR = ".status.alert.alert-success"
    GO_TO_HOME_BTN = "#form-section .btn.btn-success"


class TestCasesLocators(BasePageLocators):
    FIRST_TEST_CASE = "a[data-toggle='collapse'][href]"


class ProductsPageLocators(BasePageLocators):
    ADVERTISEMENT = "#advertisement"
    SEARCH_PRODUCT = "#search_product"
    SUBMIT_SEARCH_BTN = "#submit_search[type='button']"


class DetailProductPageLocators(BasePageLocators):
    PRODUCT_DETAILS = ".product-details"
    IMAGE_OF_PRODUCT = "img[src*='get_product_picture']"

    PRODUCT_INFORMATION = ".product-information"
    PRODUCT_NAME = ".product-information h2"
    PRODUCT_ADD_TO_CART_BTN = ".product-information button"
    PRODUCT_PRICE = ".product-information span span"
    QUANTITY = "#quantity"

    REVIEW_WRITE_FORM = ".category-tab.shop-details-tab"
    REVIEW_NAME = "#name"
    REVIEW_EMAIL = "#email"
    REVIEW_TEXTAREA_REVIEW = "textarea#review"
    REVIEW_SUBMIT_BTN = "#button-review"

    ITEM_ID_LOCATOR = "#product_id"
    ITEM_ID_ATTRIBUTE = "value"

    SUCCESS_MESSAGE = "#review-section .alert-success"


class ApiPageLocators(BasePageLocators):
    PANEL_HEADING = ".panel-heading"


class CartPageLocators(BasePageLocators, CartItemLocators):
    EMPTY_CART = "#empty_cart"
    CHECKOUT_BTN = "#do_action .check_out"
    CHECKOUT_MODAL = "#checkoutModal"
    LOGIN_LINK_IN_CHECKOUT = "#checkoutModal [href='/login']"

    @staticmethod
    def delete_product_btn(product_id: int) -> str:
        return f"#product-{product_id} .cart_quantity_delete"


class CheckoutPageLocators(BasePageLocators, CartItemLocators):
    ADDRESS_DELIVERY = "#address_delivery"
    ADDRESS_INVOICE = "#address_invoice"
    NAME = ".address_firstname.address_lastname"

    ORDER_ADD_INFO = "#ordermsg"
    ORDER_ADD_INFO_PLACE = "#ordermsg [name='message']"
    PLACE_ORDER_BTN = "[href='/payment']"
    TOTAL_AMOUNT_CART = "[colspan] + td .cart_total_price"


class PaymentPageLocators(BasePageLocators):
    PAYMENT_INFO_BLOCK = ".payment-information"
    NAME_OF_CARD = "[data-qa='name-on-card']"
    CARD_NUMBER = "[data-qa='card-number']"
    CVC = "[data-qa='cvc']"
    EXPIRY_MONTH = "[data-qa='expiry-month']"
    EXPIRY_YEAR = "[data-qa='expiry-year']"
    PAY_AND_CONFIRM_ORDER_BTN = "[data-qa='pay-button']"


class PaymentDonePageLocators(BasePageLocators):
    ORDER_PLACED = ".col-sm-9.col-sm-offset-1"
    DOWNLOAD_INVOICE_BTN = ".btn-default.check_out"


class DeletedAccountPageLocators(BasePageLocators):
    ACCOUNT_DELETED_BLOCK = ".col-sm-9.col-sm-offset-1"