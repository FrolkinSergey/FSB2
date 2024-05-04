from page_object.alert_element import AlertElement
from page_object.catalog_page import CatalogPage
from page_object.header_and_footer_element import HeaderElement
from page_object.admin_page import AdminPage
from page_object.main_page import MainPage


def test_login_and_check_and_logout(browser):
    username = "user"
    password = "bitnami"
    admin_page = AdminPage(browser)
    admin_page.open()
    admin_page.login(username, password)
    admin_page.get_logout_button()
    admin_page.logout()
    admin_page.get_username_input_field()
    admin_page.get_password_input_field()


def test_add_to_cart(browser):
    main_p = MainPage(browser)
    header_el = HeaderElement(browser)
    alert_el = AlertElement(browser)
    header_el.click_cart_hidden()
    header_el.check_empty_cart()
    header_el.click_cart_show()
    main_p.add_to_cart_first_product_of_featured()
    alert_el.get_success_alert()
    header_el.click_cart_hidden()
    header_el.get_elements_in_cart_with_added_product()


def test_price_on_main_page(browser):
    main_p = MainPage(browser)
    header_el = HeaderElement(browser)
    p_new1 = main_p.get_price_of_any_product_main()
    header_el.click_change_euro()
    p: str = p_new1
    p_new2 = main_p.get_price_of_any_product_main()
    assert p != p_new2.text


def test_price_on_catalog_page(browser):
    header_el = HeaderElement(browser)
    cat_p = CatalogPage(browser)
    header_el.click_any_dropdown()
    header_el.click_show_all()
    p_new3 = cat_p.get_price_of_any_product_catalog()
    header_el.click_change_euro()
    p: str = p_new3
    p_new4 = cat_p.get_price_of_any_product_catalog()
    assert p != p_new4.text
