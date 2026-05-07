class BasePageLocators:
    IMG_LOGO_SITE = "img[src='/static/images/home/logo.png']"
    PANEL_OF_TABS = ".shop-menu"

    HOME_LINK = "li a[href='/']"
    PRODUCTS_LINK = "li a[href='/products']"
    CART_LINK = "li a[href='/view_cart']"
    LOGIN_LINK = "li a[href='/login']"
    TEST_CASES_LINK = "li a[href='/test_cases']"
    API_LIST_LINK = "li a[href='/api_list']"
    VIDEO_TUTORIALS_LINK = "li a[href='https://www.youtube.com/c/AutomationExercise']"
    CONTACT_US_LINK = "li a[href='/contact_us']"

    #если залогинен появится\изменятся
    LOGOUT_LINK = "li a[href='/logout']"
    DELETE_ACCOUNT_LINK = "li a[href='/delete_account']"

    LEFT_SIDEBAR = ".left-sidebar"
    CONTINUE_SHOPPING_BTN = ".close-modal"

    CARD_OF_ITEM = ".single-products"
    IMAGE_OF_CARD = "img[src]"
    ADD_TO_CART_BTN = ".add-to-cart"
    ITEM_PRICE = ".productinfo h2"
    ITEM_NAME = ".productinfo p"
    VIEW_PRODUCT_DETAILS_BTN = ".nav-pills.nav-justified a"


class MainPageLocators(BasePageLocators):
    CAROUSEL_SLIDER = "#slider-carousel.carousel.slide"
    COOKIE_BANNER = "div.fc-dialog.fc-choice-dialog"
    ACCEPT_COOKIE_BANNER_BTN = ".fc-cta-consent.fc-primary-button"


class LoginPageLocators(BasePageLocators):
    LOGIN_FORM = ".login-form"
    LOGIN_EMAIL_AREA= "[data-qa=login-email]"
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
    ACCOUNT_CREATED_MESSAGE = "[data-qa=account-created]"
    CONTINUE_BTN = "[data-qa=continue-button]"

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
    first_TEST_CASE = "a[data-toggle='collapse'][href]"


class ProductsPageLocators(BasePageLocators):
    ADVERTISEMENT = "#advertisement"
    SEARCH_PRODUCT = "#search_product"

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
    REVIEW_TEXTAREA_REVIEW= "textarea#review"
    REVIEW_SUBMIT_BTN = "#button-review"

class CartPageLocators(BasePageLocators):
    BREADCRUMB = ".breadcrumb"
    EMPTY_CART = "#empty_cart"

    CHECKOUT_BTN = ".btn-default.check_out"
    TABLE_ITEMS = ".table-responsive"


class ApiPageLocators(BasePageLocators):
    PANEL_HEADING = ".panel-heading"