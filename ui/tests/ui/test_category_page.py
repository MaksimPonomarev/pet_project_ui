import time

from ui.test_data.data import CategoryGroup, WomenSubcategory, MenSubcategory


def test_open_category_products(main_page, category_product_page):
    main_page.open()
    main_page.should_be_main_page()
    main_page.should_be_visible_left_sidebar()
    main_page.sidebar.open_category_group(category=CategoryGroup.WOMEN)
    main_page.sidebar.should_be_category_group_with_subcategories_visible (category=CategoryGroup.WOMEN)
    main_page.sidebar.open_subcategory_page(subcategory=WomenSubcategory.DRESS)
    category_product_page.should_be_subcategory_products_page(subcategory=WomenSubcategory.DRESS)

    main_page.sidebar.open_category_group(category=CategoryGroup.MEN)
    main_page.sidebar.should_be_category_group_with_subcategories_visible (category=CategoryGroup.MEN)
    main_page.sidebar.open_subcategory_page(subcategory=MenSubcategory.TSHIRTS)
    category_product_page.should_be_subcategory_products_page(subcategory=MenSubcategory.TSHIRTS)