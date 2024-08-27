from pages.home_page import HomePage as HP
from pages.header_page import HeaderPage
import pytest
from allure_commons.types import Severity
import allure


@allure.feature("Check elements")
@allure.title("Check Home page elements")
@allure.severity(severity_level=Severity.NORMAL)
def test_home_page_elements(browser):
    home_page = HP(browser)
    home_page.get_element(HP.LOGO)
    home_page.get_element(HP.SEARCH)
    home_page.get_element(HP.MAGNIFIER)
    home_page.get_element(HP.CAROUSEL_INDICATORS)


@allure.feature("Change currency")
@allure.title("Change currency in home page")
@allure.severity(severity_level=Severity.NORMAL)
@pytest.mark.parametrize(
    "loc, cur",
    [(HP.EURO, "€"), (HP.USD, "$"), (HP.GBP, "£")],
    ids=("EURO", "USD", "GBP"),
)
def test_change_currency(browser, loc, cur):
    home_page = HP(browser)

    HeaderPage(browser).click_on_currency_switch()
    HeaderPage(browser).select_currency(loc)

    cart_button = HeaderPage(browser).get_element(HeaderPage.CART_BUTTON)
    home_page.check_text_in_element(cur, cart_button)

    new_prices = home_page.get_elements(HP.NEW_PRICES)
    tax_prices = home_page.get_elements(HP.TAX_PRICES)
    for price in new_prices + tax_prices:
        home_page.check_text_in_element(cur, price)
