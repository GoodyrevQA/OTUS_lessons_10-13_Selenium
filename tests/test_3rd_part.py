from pages.administration_page import AdministrationPage as AP
from pages.home_page import HomePage as HP
from pages.product_page import ProductPage as PP
from pages.catalog_page import CatalogPage as CP
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_logout(browser):
    browser.get(browser.url + "/administration")
    WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located(AP.ALL_RIGHTS_RESERVED)
    )

    username = browser.find_element(*AP.USERNAME_INPUT)
    username.clear()
    username.send_keys("user")

    password = browser.find_element(*AP.PASSWORD_INPUT)
    password.clear()
    password.send_keys("bitnami")

    login = browser.find_element(*AP.SUBMIT_BUTTON)
    login.click()

    WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located(AP.AUTHORIZED_USER)
    )

    logout = browser.find_element(*AP.LOGOUT)
    logout.click()

    WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located(AP.ALL_RIGHTS_RESERVED)
    )


def test_add_product_to_the_cart(browser):
    WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located(HP.CAROUSEL_INDICATORS)
    )

    macbook = browser.find_element(*HP.MACBOOK)
    macbook.click()

    add_to_cart = browser.find_element(*PP.ADD_TO_CART)
    add_to_cart.click()

    # ????? я этот алерт с успешным успехом сумел отловить только с помощью скриншота
    # ????? но если бы он был чуть быстрее, я бы не успел
    # ????? а как правильно нужно с такими штуками бороться?
    WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located(PP.CLOSE_SUCCESS)
    )
    close_success = browser.find_element(*PP.CLOSE_SUCCESS)
    close_success.click()

    cart_button = browser.find_element(*HP.CART_BUTTON)
    cart_button.click()

    WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located(PP.MACBOOK_IN_THE_CART)
    )


def test_change_currency_on_the_home_page(browser):
    WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located(HP.CAROUSEL_INDICATORS)
    )

    currency = browser.find_element(*HP.CURRENCY)
    currency.click()

    euro = browser.find_element(*HP.EURO)
    euro.click()

    cart_button = browser.find_element(*HP.CART_BUTTON)
    assert "€" in cart_button.text

    new_prices = browser.find_elements(*HP.NEW_PRICE)
    old_prices = browser.find_elements(*HP.OLD_PRICE)
    tax_prices = browser.find_elements(*HP.TAX_PRICE)

    for price in new_prices:
        assert "€" in price.text

    for price in old_prices:
        assert "€" in price.text

    for price in tax_prices:
        assert "€" in price.text


def test_change_currency_on_the_cartalog_page(browser):
    browser.get(browser.url + "/en-gb/catalog/desktops")
    WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located(CP.TEXT_END)
    )

    currency = browser.find_element(*HP.CURRENCY)
    currency.click()

    euro = browser.find_element(*HP.EURO)
    euro.click()

    cart_button = browser.find_element(*HP.CART_BUTTON)
    assert "€" in cart_button.text

    new_prices = browser.find_elements(*HP.NEW_PRICE)
    old_prices = browser.find_elements(*HP.OLD_PRICE)
    tax_prices = browser.find_elements(*HP.TAX_PRICE)

    for price in new_prices:
        assert "€" in price.text

    for price in old_prices:
        assert "€" in price.text

    for price in tax_prices:
        assert "€" in price.text
