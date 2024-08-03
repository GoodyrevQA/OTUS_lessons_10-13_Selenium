from selenium.webdriver.common.by import By


class ProductPage:
    HEART = (By.CSS_SELECTOR, "button .fa-heart")
    COMPARE_PRODUCT = (By.CSS_SELECTOR, ".fa-arrow-right-arrow-left")
    ADD_TO_CART = (By.CSS_SELECTOR, ".btn-primary.btn-lg")
    INPUT_QUANTITY = (By.CSS_SELECTOR, "#input-quantity")
    IMAGE = (By.CSS_SELECTOR, ".img-thumbnail.mb-3")
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, "#tab-description.show")

    MACBOOK_IN_THE_CART = (By.CSS_SELECTOR, ".mb-2 [title=MacBook]")
    CLOSE_SUCCESS = (By.CSS_SELECTOR, ".btn-close")
