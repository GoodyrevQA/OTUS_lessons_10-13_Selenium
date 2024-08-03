from selenium.webdriver.common.by import By


class AdministrationPage:
    USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    OPENCART_LINK = (By.XPATH, "//*[text()='OpenCart']")
    ALL_RIGHTS_RESERVED = (By.XPATH, "//*[text()=' © 2009-2024 All Rights Reserved.']")
    IMAGE = (By.CSS_SELECTOR, "img")
    AUTHORIZED_USER = (By.CSS_SELECTOR, ".d-lg-inline")
    LOGOUT = (By.CSS_SELECTOR, ".fa-sign-out")
