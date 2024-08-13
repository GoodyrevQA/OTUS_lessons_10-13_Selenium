from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    LOGO = (By.CSS_SELECTOR, "#logo")
    SEARCH = (By.CSS_SELECTOR, "#search")
    MAGNIFIER = (By.CSS_SELECTOR, ".fa-magnifying-glass")

    CAROUSEL_INDICATORS = (By.CSS_SELECTOR, "#carousel-banner-1 .carousel-indicators")

    MACBOOK = (By.CSS_SELECTOR, ".mb-3 [title=MacBook]")

    EURO = (By.CSS_SELECTOR, "[href=EUR]")
    GBP = (By.CSS_SELECTOR, "[href=GBP]")
    USD = (By.CSS_SELECTOR, "[href=USD]")

    NEW_PRICES = (By.CSS_SELECTOR, ".price-new")
    OLD_PRICES = (By.CSS_SELECTOR, ".price-old")
    TAX_PRICES = (By.CSS_SELECTOR, ".price-tax")

    FEATURED_PRODUCT_NAMES = (By.CSS_SELECTOR, ".col.mb-3 h4 a")

    def get_featured_product_name_by_index(self, index=0):
        return self.get_elements(self.FEATURED_PRODUCT_NAMES)[index].text

    def click_featured_product_by_index(self, index=0):
        self.get_elements(self.FEATURED_PRODUCT_NAMES)[index].click()
