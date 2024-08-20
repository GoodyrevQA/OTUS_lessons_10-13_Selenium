from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from datetime import datetime
import allure


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
    WRONG_LOCATOR = (By.CSS_SELECTOR, ".fa-floppy-disk11111111111")

    @allure.step("Open Administration page")
    def open(self):
        self.browser.get(self.browser.url + "/administration")

    @allure.step("Input username - {value}")
    def fill_username(self, value: str):
        self.input_value(self.USERNAME_INPUT, value)

    @allure.step("Input password - {value}")
    def fill_password(self, value: str):
        self.input_value(self.PASSWORD_INPUT, value)

    @allure.step("Click button LOGIN")
    def click_login_button(self):
        self.click(self.SUBMIT_BUTTON)

    @allure.step("Click catalog menu")
    def click_menu_catalog(self):
        self.click(self.MENU_CATALOG)

    @allure.step("Click catalog menu Products")
    def click_menu_catalog_products(self):
        self.click(self.MENU_CATALOG_PRODUCTS)

    @allure.step("Click button ADD product")
    def click_add_product_button(self):
        self.click(self.ADD_PRODUCT_BUTTON)

    @allure.step("Click tab Data")
    def click_tab_data(self):
        self.click(self.TAB_DATA)

    @allure.step("Click tab SEO")
    def click_tab_seo(self):
        self.click(self.TAB_SEO)

    @allure.step("Click button SAVE")
    def click_save_button(self):
        self.click(self.SAVE_BUTTON)

    @allure.step("Close notification")
    def click_notification_close(self):
        try:
            self.click(self.NOTIFICATION_CLOSE)
        except Exception:
            pass

    @allure.step("Click checkbox № {index}")
    def click_checkbox_by_index(self, index=1):
        checkboxes = self.get_elements(self.CHECKBOXES)
        checkboxes[index].click()

    @allure.step("Click button BIN")
    def click_bin(self):
        self.click(self.BIN)

    def fill_new_product_name(self, value: str = "$"):
        if value == "$":
            value = f"product_{datetime.now()}"
        with allure.step(f"Fill new product name - {value}"):
            self.input_value(self.INPUT_PRODUCT_NAME, value)

    @allure.step("Fill meta tag title - {value}")
    def fill_meta_tag_title(self, value: str = "example_meta_tag"):
        self.input_value(self.INPUT_META_TAG_TITLE, value)

    @allure.step("Fill model name - {value}")
    def fill_model(self, value: str = "example_model"):
        self.input_value(self.INPUT_MODEL, value)

    def fill_keywords(self, value: str = "$"):
        if value == "$":
            value = f"key{int(datetime.now().timestamp())}"
        with allure.step(f"Fill keywords - {value}"):
            self.input_value(self.INPUT_KEYWORDS, value)

    @allure.step("Click button LOGOUT")
    def click_logout_button(self):
        self.click(self.LOGOUT)
