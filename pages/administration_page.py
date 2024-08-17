from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from datetime import datetime


class AdministrationPage(BasePage):
    USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    OPENCART_LINK = (By.XPATH, "//*[text()='OpenCart']")
    ALL_RIGHTS_RESERVED = (By.XPATH, "//*[text()=' © 2009-2024 All Rights Reserved.']")
    IMAGE = (By.CSS_SELECTOR, "img")
    AUTHORIZED_USER = (By.CSS_SELECTOR, ".d-lg-inline")
    LOGOUT = (By.CSS_SELECTOR, ".fa-sign-out")

    MENU_CATALOG = (By.CSS_SELECTOR, "#menu-catalog")
    MENU_CATALOG_PRODUCTS = (By.XPATH, "//*[@id='menu-catalog']//*[text()='Products']")
    ADD_PRODUCT_BUTTON = (By.CSS_SELECTOR, ".btn .fa-plus")
    NOTIFICATION_CLOSE = (By.CSS_SELECTOR, ".cke_notification_close")
    INPUT_PRODUCT_NAME = (By.CSS_SELECTOR, "#input-name-1")
    INPUT_META_TAG_TITLE = (By.CSS_SELECTOR, "#input-meta-title-1")
    TAB_DATA = (By.XPATH, "//*[@id='form-product']//*[text()='Data']")
    INPUT_MODEL = (By.CSS_SELECTOR, "#input-model")
    TAB_SEO = (By.XPATH, "//*[@id='form-product']//*[text()='SEO']")
    INPUT_KEYWORDS = (By.CSS_SELECTOR, "#input-keyword-0-1")

    CHECKBOXES = (By.CSS_SELECTOR, "[type=checkbox]")
    BIN = (By.CSS_SELECTOR, ".fa-trash-can")

    SAVE_BUTTON = (By.CSS_SELECTOR, ".fa-floppy-disk")

    def open(self):
        self.browser.get(self.browser.url + "/administration")

    def fill_username(self, value: str):
        self.input_value(self.USERNAME_INPUT, value)

    def fill_password(self, value: str):
        self.input_value(self.PASSWORD_INPUT, value)

    def click_login_button(self):
        self.click(self.SUBMIT_BUTTON)

    def click_menu_catalog(self):
        self.click(self.MENU_CATALOG)

    def click_menu_catalog_products(self):
        self.click(self.MENU_CATALOG_PRODUCTS)

    def click_add_product_button(self):
        self.click(self.ADD_PRODUCT_BUTTON)

    def click_tab_data(self):
        self.click(self.TAB_DATA)

    def click_tab_seo(self):
        self.click(self.TAB_SEO)

    def click_save_button(self):
        self.click(self.SAVE_BUTTON)

    def click_notification_close(self):
        try:
            self.click(self.NOTIFICATION_CLOSE)
        except Exception:
            pass

    def click_checkbox_by_index(self, index=1):
        checkboxes = self.get_elements(self.CHECKBOXES)
        checkboxes[index].click()

    def click_bin(self):
        self.click(self.BIN)

    def get_featured_product_name_by_index(self, index=0):
        return self.get_elements(self.FEATURED_PRODUCT_NAMES)[index].text

    def fill_new_product_name(self, value: str = "$"):
        if value == "$":
            value = f"product_{datetime.now()}"
        self.input_value(self.INPUT_PRODUCT_NAME, value)

    def fill_meta_tag_title(self, value: str = "example_meta_tag"):
        self.input_value(self.INPUT_META_TAG_TITLE, value)

    def fill_model(self, value: str = "example_model"):
        self.input_value(self.INPUT_MODEL, value)

    def fill_keywords(self, value: str = "$"):
        if value == "$":
            value = f"key{int(datetime.now().timestamp())}"
        self.input_value(self.INPUT_KEYWORDS, value)

    def click_logout_button(self):
        self.click(self.LOGOUT)
