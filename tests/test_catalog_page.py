from pages.catalog_page import CatalogPage as CP
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_catalog_page(browser):
    browser.get(browser.url + "/en-gb/catalog/cameras")
    WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located(CP.TEXT_END)
    )
    browser.find_element(*CP.HOME)
    browser.find_element(*CP.INPUT_SORT)
    browser.find_element(*CP.BUTTON_GRID)
    browser.find_element(*CP.BUTTON_LIST)
    browser.find_element(*CP.PRODUCT_COMPARE)
