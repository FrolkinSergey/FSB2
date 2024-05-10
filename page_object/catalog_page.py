from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class CatalogPage(BasePage):
    NAME = By.XPATH, '//*[text()="Desktops"]'
    BLOCKS = By.XPATH, '//*[@class="product-thumb"]'
    PRODUCT_PRICE = By.XPATH, '//div[@class="price"]'
    SORT = By.XPATH, '//label[@for="input-sort"]'
    SORT_INPUT_FIELD = By.CSS_SELECTOR, "#input-sort"
    LIMIT = By.XPATH, '//label[@for="input-limit"]'
    LIMIT_INPUT_FIELD = By.CSS_SELECTOR, "#input-limit"
    PAGINATION_BUTTONS = By.XPATH, '//div[@class="col-sm-6 text-end"]'
    PRICE_OF_ANY_PRODUCT_CATALOG = By.CSS_SELECTOR, "span.price-new"

    def get_name(self):
        return self.get_element(self.NAME)

    def get_blocks_of_products(self):
        return self.get_elements(self.BLOCKS)

    def get_blocks_of_price(self):
        return self.get_elements(self.PRODUCT_PRICE)

    def get_sort(self):
        return self.get_element(self.SORT)

    def get_sort_input_field(self):
        return self.get_element(self.SORT_INPUT_FIELD)

    def get_limit(self):
        return self.get_element(self.LIMIT)

    def get_limit_input_field(self):
        return self.get_element(self.LIMIT_INPUT_FIELD)

    def get_pagination_buttons(self):
        return self.get_element(self.PAGINATION_BUTTONS)

    def get_price_of_any_product_catalog(self):
        return self.get_element(self.PRICE_OF_ANY_PRODUCT_CATALOG)