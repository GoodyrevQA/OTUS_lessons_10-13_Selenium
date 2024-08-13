from pages.product_page import ProductPage as PP
from pages.home_page import HomePage as HP
from pages.header_page import HeaderPage
from pages.alert_element import AlertSuccessElement
from pages.shopping_cart_page import ShoppingCartPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_product_page_elements(browser):
    home_page = HP(browser)
    product_page = PP(browser)

    home_page.click_featured_product_by_index(index=0)

    product_page.get_element(PP.IMAGE)
    product_page.get_element(PP.HEART)
    product_page.get_element(PP.ADD_TO_CART_BUTTON)
    product_page.get_element(PP.INPUT_QUANTITY)
    product_page.get_element(PP.COMPARE_PRODUCT)


def test_add_product_to_the_cart(browser):
    home_page = HP(browser)
    product_page = PP(browser)

    product_name = home_page.get_featured_product_name_by_index(index=0)
    home_page.click_featured_product_by_index(index=0)
    product_page.add_to_cart()
    AlertSuccessElement(browser).close_alert()
    product_page.click(HeaderPage(browser).CART_BUTTON)

    product_name_in_the_cart = ShoppingCartPage(browser).get_first_product_name()
    assert product_name == product_name_in_the_cart
