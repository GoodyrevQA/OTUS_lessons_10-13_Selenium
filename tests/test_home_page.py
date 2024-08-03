from pages.home_page import HomePage as HP
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_home_page(browser):
    WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located(HP.CAROUSEL_INDICATORS)
    )
    browser.find_element(*HP.LOGO)
    browser.find_element(*HP.SEARCH)
    browser.find_element(*HP.CURRENCY)
    browser.find_element(*HP.MAGNIFIER)
    browser.find_element(*HP.CART_BUTTON)
