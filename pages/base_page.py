from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import logging
import allure
import selenium
import os
from datetime import datetime


class BasePage:
    def __init__(self, browser, wait=3):
        self.browser = browser
        self.wait = WebDriverWait(browser, wait)
        self.class_name = type(self).__name__
        self.__config_logger()

    def __config_logger(self):
        self.logger = logging.getLogger(self.class_name)
        handler = logging.StreamHandler()

        handler.setFormatter(
            logging.Formatter(
                "%(asctime)s - %(levelname)s - %(filename)s - %(message)s"
            )
        )

        self.logger.addHandler(handler)
        self.logger.setLevel(level=self.browser.log_level)

    def get_element(self, locator: tuple, timeout=3):
        self.logger.debug(f"{self.class_name}: Getting element {locator}")
        return WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def get_elements(self, locator: tuple, timeout=3):
        self.logger.debug(f"{self.class_name}: Getting elements {locator}")
        return WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

    def click(self, locator: tuple):
        ActionChains(self.browser).move_to_element(self.get_element(locator)).pause(
            0.3
        ).click().perform()
        self.logger.debug(f"{self.class_name}: Clicking element {locator}")

    def input_value(self, locator: tuple, text: str):
        self.logger.debug(f"{self.class_name}: Inputing {text} in {locator}")
        self.get_element(locator).click()
        self.get_element(locator).clear()
        for l in text:
            self.get_element(locator).send_keys(l)

    def check_text_in_element(self, text, element):
        self.logger.debug(f"{self.class_name}: Checking {text} in {element}")
        assert text in element.text

    def accept_alert(self):
        self.logger.debug(f"{self.class_name}: Accepting alert")
        confirm = self.browser.switch_to.alert
        confirm.accept()

    @allure.step("Checking if locator {locator} is present")
    def is_present(self, locator):
        try:
            self.logger.debug(f"Checking if {locator} is present")
            return self.wait.until(EC.visibility_of_element_located(locator))
        except selenium.common.exceptions.TimeoutException as e:
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot_image_from_base_page_method_is_present",
                attachment_type=allure.attachment_type.PNG,
            )
            raise AssertionError(e.msg)
