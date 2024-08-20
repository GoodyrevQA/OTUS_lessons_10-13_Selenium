from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class ProductPage(BasePage):
    HEART = (By.CSS_SELECTOR, "button .fa-heart")
    COMPARE_PRODUCT = (By.CSS_SELECTOR, ".fa-arrow-right-arrow-left")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-primary.btn-lg")
    INPUT_QUANTITY = (By.CSS_SELECTOR, "#input-quantity")
    IMAGE = (By.CSS_SELECTOR, ".img-thumbnail.mb-3")
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, "#tab-description.show")

    @allure.step("Click button ADD to cart")
    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)
