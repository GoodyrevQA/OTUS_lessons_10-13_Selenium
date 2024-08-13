from pages.register_page import RegisterPage as RP
from pages.administration_page import AdministrationPage as AP
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker


def test_register_page_elements(browser):
    register_page = RP(browser)
    register_page.open()

    register_page.get_element(RP.EMAIL)
    register_page.get_element(RP.AGREE_BUTTON)
    register_page.get_element(RP.PASSWORD)
    register_page.get_element(RP.LAST_NAME)
    register_page.get_element(RP.FIRST_NAME)


def test_register_new_user(browser):
    register_page = RP(browser)
    register_page.open()
    fake = Faker()

    register_page.fill_first_name(fake.first_name())
    register_page.fill_last_name(fake.last_name())
    register_page.fill_email(fake.email())
    register_page.fill_password(fake.password())
    register_page.click_agree_privacy_policy_button()
    register_page.click_continue_button()
    register_page.get_element(RP.SUCCESS_REGISTRATION_MESSAGE)
