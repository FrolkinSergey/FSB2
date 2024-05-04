from page_object.catalog_page import CatalogPage
from page_object.header_and_footer_element import HeaderElement, FooterElement
from page_object.admin_page import AdminPage
from page_object.main_page import MainPage
from page_object.product_page import ProductPage
from page_object.registration_page import RegistrationPage


def test_find_elements_on_main_page(browser):
    header_el = HeaderElement(browser)
    main_page = MainPage(browser)
    footer_el = FooterElement(browser)
    header_el.get_logo()
    header_el.get_search_field()
    header_el.click_cart_hidden()
    header_el.check_empty_cart()
    main_page.get_carousel()
    footer_el.get_footer()


def test_find_elements_on_catalog_page(browser):
    header_el = HeaderElement(browser)
    catalog_page = CatalogPage(browser)
    header_el.click_any_dropdown()
    header_el.click_show_all()
    catalog_page.get_name()
    pr = catalog_page.get_blocks_of_products()
    price = catalog_page.get_blocks_of_price()
    assert len(pr) == len(price)  # Сравнение количеств блоков
    catalog_page.get_sort()
    catalog_page.get_sort_input_field()
    catalog_page.get_limit()
    catalog_page.get_limit_input_field()
    catalog_page.get_pagination_buttons()


def test_find_elements_on_product_page(browser):
    product_page = ProductPage(browser)
    product_page.open()
    product_page.get_pr_name()
    product_page.get_characteristics()
    product_page.get_price_old()
    product_page.get_price_act()
    product_page.get_like_button()
    product_page.get_add_to_cart_button()
    product_page.get_description()
    product_page.get_reviews()


def test_find_elements_on_login_page(browser):
    admin_page = AdminPage(browser)
    admin_page.open()
    admin_page.get_log_title()
    admin_page.get_username_input_field()
    admin_page.get_password_input_field()
    admin_page.get_submit_button()
    admin_page.get_ap_footer()


def test_find_elements_on_registration_page(browser):
    reg_page = RegistrationPage(browser)
    reg_page.open()
    reg_page.get_reg_title()
    reg_page.get_firstname_input_field()
    reg_page.get_lastname_input_field()
    reg_page.get_email_input_field()
    reg_page.get_password_input_field()
    reg_page.get_newsletter_checkbox()
    reg_page.get_agree_checkbox()
    reg_page.get_continue_button()
