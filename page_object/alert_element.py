from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class AlertElement(BasePage):
    SUCCESS_ALERT = By.XPATH, '//*[@class="alert alert-success alert-dismissible"]'

    def get_success_alert(self):
        return self.get_element(self.SUCCESS_ALERT)