import time

import faker
from faker import Faker
from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class RegistrationPage(BasePage):
    PATH = "/index.php?route=account/register"
    REG_TITLE = By.XPATH, '//*[text()="Register Account"]'
    FIRSTNAME_FIELD = By.CSS_SELECTOR, "#input-firstname"
    LASTNAME_FIELD = By.CSS_SELECTOR, '[name="lastname"]'
    EMAIL_FIELD = By.CSS_SELECTOR, "#input-email"
    PASSWORD_FIELD = By.CSS_SELECTOR, "#input-password"
    NEWSLETTER_CHECKBOX = By.CSS_SELECTOR, "#input-newsletter"
    AGREE_CHECKBOX = By.CSS_SELECTOR, '[name="agree"]'
    CONTINUE_BUTTON = By.CSS_SELECTOR, "button[type='submit']"
    COMPLETED_TEXT = By.XPATH, '//*[text()="Your Account Has Been Created!"]'

    def open(self):
        url = self.browser.current_url
        self.browser.get(url + self.PATH)

    def get_reg_title(self):
        return self.get_element(self.REG_TITLE)

    def get_firstname_input_field(self):
        return self.get_element(self.FIRSTNAME_FIELD)

    def get_lastname_input_field(self):
        return self.get_element(self.LASTNAME_FIELD)

    def get_email_input_field(self):
        return self.get_element(self.EMAIL_FIELD)

    def get_password_input_field(self):
        return self.get_element(self.PASSWORD_FIELD)

    def get_newsletter_checkbox(self):
        return self.get_element(self.NEWSLETTER_CHECKBOX)

    def get_agree_checkbox(self):
        return self.get_element(self.AGREE_CHECKBOX)

    def get_continue_button(self):
        return self.get_element(self.CONTINUE_BUTTON)

    def register_page_input_value(self, first_name, last_name, email, password):
        self.input_value(self.FIRSTNAME_FIELD, first_name)
        self.input_value(self.LASTNAME_FIELD, last_name)
        self.input_value(self.EMAIL_FIELD, email)
        self.input_value(self.PASSWORD_FIELD, password)
        return self

    def enter_checkboxes(self):
        self.click(self.NEWSLETTER_CHECKBOX)
        self.click(self.AGREE_CHECKBOX)
        return self

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)

    def check_registration(self):
        return self.get_element(self.COMPLETED_TEXT)
