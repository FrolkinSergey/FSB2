from page_object.admin_page import AdminPage
from page_object.alert_element import AlertElement
from page_object.header_and_footer_element import HeaderElement
from page_object.main_page import MainPage
from page_object.registration_page import RegistrationPage


def test_create_new_product_in_admin_page(browser):
    username = "user"
    password = "bitnami"
    product_name = "2 New Product"
    meta_title = "1234"
    model = "Unknown"
    default = "new-product1"
    al_el = AlertElement(browser)
    adm_p = AdminPage(browser)
    adm_p.open()
    adm_p.login(username, password)
    adm_p.open_products()
    adm_p.click_add_new_product()
    adm_p.input_required_field(product_name, meta_title, model, default)
    al_el.get_success_alert()


def test_delete_product_in_admin_page(browser):
    username = "user"
    password = "bitnami"
    al_el = AlertElement(browser)
    adm_p = AdminPage(browser)
    adm_p.open()
    adm_p.login(username, password)
    adm_p.open_products()
    adm_p.choice_checkbox_1()
    adm_p.click_delete()
    adm_p.accept_alert()
    al_el.get_success_alert()


def test_add_new_user(browser):
    first_name = "Winston"
    last_name = "Churchill"
    email = "test_125@gmail.com"
    password = "SuperPassword123"
    reg_p = RegistrationPage(browser)
    reg_p.open()
    reg_p.register_page_input_value(first_name, last_name, email, password)
    reg_p.enter_checkboxes()
    reg_p.click_continue()
    reg_p.check_registration()


def test_change_currency(browser):
    main_p = MainPage(browser)
    header_el = HeaderElement(browser)
    p_1 = main_p.get_price_of_any_product_main()
    header_el.click_change_euro()
    p1: str = p_1
    p_2 = main_p.get_price_of_any_product_main()
    header_el.click_change_pound()
    p2: str = p_2
    p_3 = main_p.get_price_of_any_product_main()
    header_el.click_change_dollar()
    p3: str = p_3
    assert p1 != p2 != p3
