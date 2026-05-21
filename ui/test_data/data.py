from enum import Enum
from urllib.parse import quote

class HeaderSite:
    LOGGEN_IN_TEXT = "Logged in"

class ErrorMessageText:
    INCORRECT_LOGIN_ERROR = "Your email or password is incorrect!"
    INCORRECT_SIGNUP_ERROR = "Email Address already exist!"


class Titles:
    SEARCHED_PRODUCTS = "Searched Products"
    FOOTER = "Subscription"
    DELETED_ACCOUNT = "Account Deleted!"
    CREATED_ACCOUNT = "Account Created!"


class ProductDetailData:
    CATEGORY = "Category:"
    AVAILABILITY = "Availability:"
    CONDITION = "Condition:"
    BRAND = "Brand:"


class SuccessMessageText:
    CREATED_ACCOUNT = "Congratulations! Your new account has been successfully created!"
    ADD_PRODUCT = "Success! Your details have been submitted successfully."
    FOOTER_SUBSCRIBE = "You have been successfully subscribed!"
    PLACE_ORDER = "Congratulations! Your order has been confirmed!"
    DELETED_ACCOUNT = "Your account has been permanently deleted!"

class SearchData:
    VALID_PRODUCTS = ["Sleeveless Dress", "Men Tshirt", "Sleeves Top and Short - Blue & Pink"]




class CategoryGroup(Enum):
    WOMEN = "Women"
    MEN = "Men"
    KIDS = "Kids"



class BaseSubcategory(Enum):
    @property
    def id(self):
        return self.value[0]

    @property
    def title(self):
        return self.value[1]

class WomenSubcategory(BaseSubcategory):
    DRESS = (1, "Women - Dress")
    TOPS = (2, "Women - Tops")
    SAREE = (7, "Women - Saree")


class MenSubcategory(BaseSubcategory):
    TSHIRTS = (3, "Men - Tshirts")
    JEANS = (6, "Men - Jeans")


class KidsSubcategory(BaseSubcategory):
    DRESS = (4, "Kids - Dress")
    TOPS_AND_TSHIRT = (5, "Kids - Tops & Shirts")

CATEGORY_SUBCATEGORIES = {
    CategoryGroup.WOMEN: WomenSubcategory,
    CategoryGroup.MEN: MenSubcategory,
    CategoryGroup.KIDS: KidsSubcategory,
}

class Brands(Enum):
    POLO = "Polo"
    H_M = "H&M"
    MADAME = "Madame"
    MAST_HARBOUR = "Mast & Harbour"
    BABYHUG = "Babyhug"
    ALLEN_SOLLY_JUNIOR = "Allen Solly Junior"
    KOOKIE_KIDS = "Kookie Kids"
    BIBA = "Biba"

    @property
    def url(self):
        return f"/brand_products/{quote(self.value, safe="")}"

    @property
    def title_brand(self):
        return f"Brand - {self.value} Products"