from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AlertSuccessElement(BasePage):
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success")
    CLOSE_SUCCESS = (By.CSS_SELECTOR, ".btn-close")

    def close_alert(self):
        return self.click(self.CLOSE_SUCCESS)
