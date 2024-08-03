from pages.product_page import ProductPage as PP
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_product_page(browser):
    browser.get(browser.url + "/en-gb/product/cameras/nikon-d300")
    WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located(PP.PRODUCT_DESCRIPTION)
    )
    browser.find_element(*PP.IMAGE)
    browser.find_element(*PP.HEART)
    browser.find_element(*PP.ADD_TO_CART)
    browser.find_element(*PP.INPUT_QUANTITY)
    browser.find_element(*PP.COMPARE_PRODUCT)
