from pages.register_page import RegisterPage as RP
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_register_page(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located(RP.CONTINUE)
    )
    browser.find_element(*RP.EMAIL)
    browser.find_element(*RP.AGREE)
    browser.find_element(*RP.PASSWORD)
    browser.find_element(*RP.LAST_NAME)
    browser.find_element(*RP.FIRST_NAME)
