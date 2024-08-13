from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CatalogPage(BasePage):
    HOME = (By.CSS_SELECTOR, ".fa-home")
    PRODUCT_COMPARE = (By.CSS_SELECTOR, "#compare-total")
    BUTTON_LIST = (By.CSS_SELECTOR, "#button-list")
    BUTTON_GRID = (By.CSS_SELECTOR, "#button-grid")
    INPUT_SORT = (By.CSS_SELECTOR, "#input-sort")
    TEXT_END = (By.CSS_SELECTOR, ".text-end")

    def open_cameras_page(self):
        self.browser.get(self.browser.url + "/en-gb/catalog/cameras")
