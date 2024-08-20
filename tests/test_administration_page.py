from pages.administration_page import AdministrationPage as AP
from pages.alert_element import AlertSuccessElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import dotenv
import allure
from allure_commons.types import Severity


@allure.feature("Check elements")
@allure.title("Check Administration page elements")
@allure.severity(severity_level=Severity.NORMAL)
def test_administration_page_elements(browser):
    administration_page = AP(browser)
    administration_page.open()

    administration_page.get_element(AP.IMAGE)
    administration_page.get_element(AP.SUBMIT_BUTTON)
    administration_page.get_element(AP.OPENCART_LINK)
    administration_page.get_element(AP.PASSWORD_INPUT)
    administration_page.get_element(AP.USERNAME_INPUT)


@allure.feature("Authorization")
@allure.story("Valid credentials")
@allure.title("Authorization with valid credentials")
@allure.severity(severity_level=Severity.BLOCKER)
def test_login_logout(browser):
    administration_page = AP(browser)
    administration_page.open()

    username = os.getenv("USER_NAME")
    administration_page.fill_username(username)

    pssw = os.getenv("PASSWORD")
    administration_page.fill_password(pssw)

    administration_page.click_login_button()
    administration_page.get_element(AP.AUTHORIZED_USER)

    administration_page.click_logout_button()
    administration_page.get_element(AP.ALL_RIGHTS_RESERVED)
    # добавил проверку на несуществующий локатор для теста скриншотов аллюра
    administration_page.is_present(AP.WRONG_LOCATOR)


@allure.feature("Administration")
@allure.story("Products Administration")
@allure.title("Add product")
@allure.severity(severity_level=Severity.CRITICAL)
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


@allure.feature("Administration")
@allure.story("Products Administration")
@allure.title("Remove product")
@allure.severity(severity_level=Severity.NORMAL)
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
