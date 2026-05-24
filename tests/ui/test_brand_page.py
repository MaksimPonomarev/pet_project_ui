from test_data.data import Brands


def test_open_brand_products(main_page, brand_product_page):
    main_page.open()
    main_page.should_be_main_page()
    main_page.should_be_visible_left_sidebar()
    main_page.sidebar.should_be_brands_on_left_sidebar()
    main_page.sidebar.open_brand_page(brand=Brands.POLO)

    brand_product_page.should_be_brand_products_page(brand=Brands.POLO)

    main_page.sidebar.open_brand_page(brand=Brands.ALLEN_SOLLY_JUNIOR)

    brand_product_page.should_be_brand_products_page(brand=Brands.ALLEN_SOLLY_JUNIOR)