from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class HeaderElement(BasePage):
    LOGO = By.XPATH, '//*[title="Your Store"]'
    SEARCH_FIELD = By.CSS_SELECTOR, '[name="search"]'
    CART_HIDDEN = By.XPATH, '//*[@class="btn btn-lg btn-inverse btn-block dropdown-toggle"]'
    CART_SHOW = By.XPATH, '//*[@class="btn btn-lg btn-inverse btn-block dropdown-toggle show"]'
    EMPTY_CART_TEXT = By.XPATH, '//*[@class="text-center p-4"]'
    DESKTOPS = By.XPATH, '//*[@class="nav-link dropdown-toggle"]'
    SHOW_ALL = By.XPATH, '//*[@class="see-all"]'
    PRODUCT_CARD_IN_CART = By.XPATH, '//*[@class="table table-striped mb-2"]'
    CARD_TABLE_IN_CART = By.XPATH, '//*[@class="table table-sm table-bordered mb-2"]'
    DELETE_BUTTON_IN_CART = By.XPATH, '//*[@class="btn btn-danger"]'
    CURRENCY_DROPDOWN = By.XPATH, '//*[@class="dropdown-toggle"]'
    CURRENCY_EURO = By.XPATH, '//*[@href="EUR"]'
    CURRENCY_POUND_STERLING = By.XPATH, '//*[@href="GBP"]'
    CURRENCY_US_DOLLAR = By.XPATH, '//*[@href="USD"]'

    def get_logo(self):
        return self.get_element(self.LOGO)

    def get_search_field(self):
        return self.get_element(self.SEARCH_FIELD)

    def click_cart_hidden(self):
        self.click(self.CART_HIDDEN)

    def click_cart_show(self):
        self.click(self.CART_SHOW)

    def check_empty_cart(self):
        return self.get_element(self.EMPTY_CART_TEXT)

    def click_any_dropdown(self):
        self.click(self.DESKTOPS)

    def click_show_all(self):
        self.click(self.SHOW_ALL)

    def get_elements_in_cart_with_added_product(self):
        self.get_element(self.PRODUCT_CARD_IN_CART)
        self.get_element(self.CARD_TABLE_IN_CART)
        self.get_element(self.DELETE_BUTTON_IN_CART)
        return self

    def click_change_euro(self):
        self.click(self.CURRENCY_DROPDOWN)
        self.click(self.CURRENCY_EURO)
        return self

    def click_change_pound(self):
        self.click(self.CURRENCY_DROPDOWN)
        self.click(self.CURRENCY_POUND_STERLING)
        return self

    def click_change_dollar(self):
        self.click(self.CURRENCY_DROPDOWN)
        self.click(self.CURRENCY_US_DOLLAR)
        return self


class FooterElement(BasePage):
    FOOTER = By.XPATH, '//*[@class ="container"]'

    def get_footer(self):
        return self.get_element(self.FOOTER)
