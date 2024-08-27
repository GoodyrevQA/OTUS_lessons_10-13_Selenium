from pages.catalog_page import CatalogPage as CP
from pages.home_page import HomePage as HP
from pages.header_page import HeaderPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from allure_commons.types import Severity
import allure


@allure.feature("Check elements")
@allure.title("Check Catalog page elements")
@allure.severity(severity_level=Severity.NORMAL)
def test_catalog_page_elements(browser):
    catalog_page = CP(browser)
    catalog_page.open_cameras_page()

    catalog_page.get_element(CP.HOME)
    catalog_page.get_element(CP.INPUT_SORT)
    catalog_page.get_element(CP.BUTTON_GRID)
    catalog_page.get_element(CP.BUTTON_LIST)
    catalog_page.get_element(CP.PRODUCT_COMPARE)


@allure.feature("Change currency")
@allure.title("Change currency in catalog page")
@allure.severity(severity_level=Severity.NORMAL)
@pytest.mark.parametrize(
    "loc, cur",
    [(HP.EURO, "€"), (HP.USD, "$"), (HP.GBP, "£")],
    ids=("EURO", "USD", "GBP"),
)
def test_change_currency_from_catalog_page(browser, loc, cur):
    home_page = HP(browser)
    catalog_page = CP(browser)
    catalog_page.open_cameras_page()

    HeaderPage(browser).click_on_currency_switch()
    HeaderPage(browser).select_currency(loc)

    cart_button = HeaderPage(browser).get_element(HeaderPage.CART_BUTTON)
    home_page.check_text_in_element(cur, cart_button)

    new_prices = home_page.get_elements(HP.NEW_PRICES)
    tax_prices = home_page.get_elements(HP.TAX_PRICES)
    for price in new_prices + tax_prices:
        home_page.check_text_in_element(cur, price)
