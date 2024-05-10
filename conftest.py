import allure
import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption("--browser", default="ch", choices=["sf", "ch", "ya"])
    parser.addoption("--headless", action="store_true")
    parser.addoption("--yandexdriver", default="/Users/sergeyfrolkin/Documents/GitHub/FSB2/venv/yandexdriver")
    parser.addoption("--yandexapp", default="/Applications/Yandex.app")
    parser.addoption("--url", default="http://192.168.0.104:8081/")
    parser.addoption("--log_level", action="store", default="INFO")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome != 'passed':
        item.status = 'failed'
    else:
        item.status = 'passed'

@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless_mode = request.config.getoption("--headless")
    yandexdriver = request.config.getoption("--yandexdriver")
    yandexapp = request.config.getoption("--yandexapp")
    base_url = request.config.getoption("--url")
    log_level = request.config.getoption("--log_level")

    logger = logging.getLogger(request.node.name)
    ch = logging.FileHandler(filename=f"tests/logs/{request.node.name}.log")
    ch.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.setLevel(level=log_level)
    logger.addHandler(ch)

    if browser_name == "sf":
        """Safari not supported Headless mode - https://discussions.apple.com/thread/251837694?sortBy=best"""
        driver = webdriver.Safari()
    elif browser_name == "ch":
        options = Options()
        if headless_mode:
            options.add_argument("headless=new")
        driver = webdriver.Chrome(service=Service(), options=options)
    elif browser_name == "ya":
        yaoptions = Options()
        if headless_mode:
            yaoptions.add_argument("headless=new")
        yaoptions.binary_location = yandexapp
        service = Service(executable_path=yandexdriver)
        driver = webdriver.Chrome(service=service, options=yaoptions)
    else:
        raise ValueError(f"Browser {browser_name} not supported ")

    driver.maximize_window()

    driver.get(base_url)
    driver.url = base_url

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    logger.info("Browser %s started" % browser)

    yield driver

    if request.node.status == 'failed':
        allure.attach(
            name="failure_screenshot",
            body=driver.get_screenshot_as_png(),
            attachment_type=allure.attachment_type.PNG
        )

    request.addfinalizer(driver.close)