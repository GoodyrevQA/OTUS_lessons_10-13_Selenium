from pages.administration_page import AdministrationPage as AP
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_administration_page(browser):
    browser.get(browser.url + "/administration")
    WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located(AP.ALL_RIGHTS_RESERVED)
    )
    browser.find_element(*AP.IMAGE)
    browser.find_element(*AP.SUBMIT_BUTTON)
    browser.find_element(*AP.OPENCART_LINK)
    browser.find_element(*AP.PASSWORD_INPUT)
    browser.find_element(*AP.USERNAME_INPUT)
