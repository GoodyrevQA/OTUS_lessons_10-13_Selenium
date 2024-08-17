from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HeaderPage(BasePage):
    CURRENCY = (By.CSS_SELECTOR, "#form-currency")
    CART_BUTTON = (By.CSS_SELECTOR, ".d-grid")

    def click_on_currency_switch(self):
        self.get_element(self.CURRENCY).click()

    def select_currency(self, cur: tuple):
        """cur: locator of currency"""
        self.get_element(cur).click()
