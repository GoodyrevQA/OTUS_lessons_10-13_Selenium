from selenium.webdriver.common.by import By


class HomePage:
    CURRENCY = (By.CSS_SELECTOR, "#form-currency")
    LOGO = (By.CSS_SELECTOR, "#logo")
    SEARCH = (By.CSS_SELECTOR, "#search")
    MAGNIFIER = (By.CSS_SELECTOR, ".fa-magnifying-glass")
    CART_BUTTON = (By.CSS_SELECTOR, ".d-grid")
    CAROUSEL_INDICATORS = (By.CSS_SELECTOR, "#carousel-banner-1 .carousel-indicators")

    MACBOOK = (By.CSS_SELECTOR, ".mb-3 [title=MacBook]")

    EURO = (By.CSS_SELECTOR, "[href=EUR]")

    NEW_PRICE = (By.CSS_SELECTOR, ".price-new")
    OLD_PRICE = (By.CSS_SELECTOR, ".price-old")
    TAX_PRICE = (By.CSS_SELECTOR, ".price-tax")
