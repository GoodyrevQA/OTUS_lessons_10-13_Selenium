import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.firefox.options import Options as FFOptions


# BASE_URL = "http://192.168.0.19:8081"


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--headless", action="store_true")
    parser.addoption(
        "--yadriver",
        default=r"C:\projects\python_projects\OTUS_lessons_10-13_Selenium\drivers\yandexdriver.exe",
    )
    parser.addoption("--url", action="store", default="http://192.168.0.22:8081")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    headless = request.config.getoption("--headless")
    yadriver = request.config.getoption("--yadriver")

    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("headless=new")
        driver = webdriver.Chrome(service=ChromiumService(), options=options)

    elif browser_name == "firefox":
        options = FFOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options, service=FFService())

    elif browser_name == "yandex":
        options = ChromeOptions()
        if headless:
            options.add_argument("headless=new")
        options.binary_location = (
            r"C:\Users\gie\AppData\Local\Yandex\YandexBrowser\Application\browser.exe"
        )
        driver = webdriver.Chrome(
            options=options, service=ChromiumService(executable_path=yadriver)
        )

    elif browser_name == "edge":
        options = ChromeOptions()
        if headless:
            options.add_argument("headless=new")
        driver = webdriver.Edge(service=ChromiumService(), options=options)

    else:
        raise Exception("Driver not supported")

    request.addfinalizer(driver.quit)
    driver.maximize_window()
    driver.get(url)
    driver.url = url

    return driver
