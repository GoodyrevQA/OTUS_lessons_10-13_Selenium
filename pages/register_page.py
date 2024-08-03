from selenium.webdriver.common.by import By


class RegisterPage:
    FIRST_NAME = (By.CSS_SELECTOR, "#input-firstname")
    LAST_NAME = (By.CSS_SELECTOR, "#input-lastname")
    PASSWORD = (By.CSS_SELECTOR, "#input-password")
    EMAIL = (By.CSS_SELECTOR, "#input-email")
    AGREE = (By.CSS_SELECTOR, "[name=agree]")
    CONTINUE = (By.CSS_SELECTOR, "[type=submit]")
