from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class ProductPage(BasePage):
    PATH = "/en-gb/product/desktops/canon-eos-5d"
    PRODUCT_NAME = By.XPATH, '//*[text()="Canon EOS 5D"]'
    CHARACTERISTICS = By.XPATH, '//*[@class="list-unstyled"]'
    PRICE_OLD = By.XPATH, '//*[@class="price-old"]'
    PRICE_ACT = By.XPATH, '//*[@class="price-new"]'
    LIKE_BUT = By.XPATH, '//*[@class="fa-solid fa-heart"]'
    ADD_TO_CART_BUT = By.CSS_SELECTOR, "button[type='submit']"
    DESCRIPTION = By.XPATH, '//*[text()="Description"]'
    REVIEWS = By.XPATH, '//*[text()="Reviews (0)"]'

    def open(self):
        url = self.browser.current_url
        self.browser.get(url + self.PATH)

    def get_pr_name(self):
        return self.get_element(self.PRODUCT_NAME)

    def get_characteristics(self):
        return self.get_element(self.CHARACTERISTICS)

    def get_price_old(self):
        return self.get_element(self.PRICE_OLD)

    def get_price_act(self):
        return self.get_element(self.PRICE_ACT)

    def get_like_button(self):
        return self.get_element(self.LIKE_BUT)

    def get_add_to_cart_button(self):
        return self.get_element(self.ADD_TO_CART_BUT)

    def get_description(self):
        return self.get_element(self.DESCRIPTION)

    def get_reviews(self):
        return self.get_element(self.REVIEWS)
