from pages.administration_page import AdministrationPage as AP
from pages.alert_element import AlertSuccessElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import dotenv


def test_administration_page_elements(browser):
    administration_page = AP(browser)
    administration_page.open()

    administration_page.get_element(AP.IMAGE)
    administration_page.get_element(AP.SUBMIT_BUTTON)
    administration_page.get_element(AP.OPENCART_LINK)
    administration_page.get_element(AP.PASSWORD_INPUT)
    administration_page.get_element(AP.USERNAME_INPUT)


def test_login_logout(browser):
    administration_page = AP(browser)
    administration_page.open()

    administration_page.fill_username(os.getenv("USER_NAME"))
    administration_page.fill_password(os.getenv("PASSWORD"))

    administration_page.click_login_button()
    administration_page.get_element(AP.AUTHORIZED_USER)

    administration_page.click_logout_button()
    administration_page.get_element(AP.ALL_RIGHTS_RESERVED)


def test_add_new_product(browser):
    administration_page = AP(browser)
    alert_page = AlertSuccessElement(browser)
    administration_page.open()

    administration_page.fill_username(os.getenv("USER_NAME"))
    administration_page.fill_password(os.getenv("PASSWORD"))

    administration_page.click_login_button()
    administration_page.get_element(AP.AUTHORIZED_USER)

    administration_page.click_menu_catalog()
    administration_page.click_menu_catalog_products()
    administration_page.click_add_product_button()
    administration_page.click_notification_close()
    administration_page.fill_new_product_name()
    administration_page.fill_meta_tag_title()
    administration_page.click_tab_data()
    administration_page.fill_model()
    administration_page.click_tab_seo()
    administration_page.fill_keywords()
    administration_page.click_save_button()

    alert = alert_page.get_element(alert_page.SUCCESS_ALERT)

    administration_page.check_text_in_element(
        "Success: You have modified products!", alert
    )


def test_remove_product(browser):
    administration_page = AP(browser)
    alert_page = AlertSuccessElement(browser)
    administration_page.open()

    administration_page.fill_username(os.getenv("USER_NAME"))
    administration_page.fill_password(os.getenv("PASSWORD"))

    administration_page.click_login_button()
    administration_page.get_element(AP.AUTHORIZED_USER)

    administration_page.click_menu_catalog()
    administration_page.click_menu_catalog_products()

    administration_page.click_checkbox_by_index()
    administration_page.click_bin()

    administration_page.accept_alert()

    alert = alert_page.get_element(alert_page.SUCCESS_ALERT)

    administration_page.check_text_in_element(
        "Success: You have modified products!", alert
    )
