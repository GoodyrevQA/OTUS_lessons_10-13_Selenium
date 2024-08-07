from selenium.webdriver.common.by import By


class CatalogPage:
    HOME = (By.CSS_SELECTOR, ".fa-home")
    PRODUCT_COMPARE = (By.CSS_SELECTOR, "#compare-total")
    BUTTON_LIST = (By.CSS_SELECTOR, "#button-list")
    BUTTON_GRID = (By.CSS_SELECTOR, "#button-grid")
    INPUT_SORT = (By.CSS_SELECTOR, "#input-sort")
    TEXT_END = (By.CSS_SELECTOR, ".text-end")
