import allure
import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOption
from selenium.webdriver.safari.options import Options as SafariOption

def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", choices=["chrome", "firefox", "safari"])
    parser.addoption("--url", default="http://192.168.0.104:8081/")
    parser.addoption("--log_level", action="store", default="INFO")
    parser.addoption("--executor", action="store", default="192.168.0.104")
    parser.addoption("--vnc", action="store_true")
    parser.addoption("--logs", action="store_true")
    parser.addoption("--video", action="store_true")
    parser.addoption("--bv")

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
    base_url = request.config.getoption("--url")
    log_level = request.config.getoption("--log_level")
    executor = request.config.getoption("--executor")
    vnc = request.config.getoption("--vnc")
    version = request.config.getoption("--bv")
    logs = request.config.getoption("--logs")
    video = request.config.getoption("--video")

    executor_url = f"http://{executor}:4444/wd/hub"

    logger = logging.getLogger(request.node.name)
    ch = logging.FileHandler(filename=f"tests/logs/{request.node.name}.log")
    ch.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.setLevel(level=log_level)
    logger.addHandler(ch)

    if browser_name == "chrome":
        options = ChromeOptions()
    elif browser_name == "firefox":
        options = FirefoxOption()
    elif browser_name == "safari":
        options = SafariOption()
    else:
        raise ValueError(f"Browser {browser_name} not supported ")

    caps = {
        "browserName": browser_name,
        "browserVersion": version,
        "selenoid:options": {
            "enableVNC": vnc,
            "name": request.node.name,
            "screenResolution": "1280x720",
            "enableVideo": video,
            "enableLog": logs,
            "sessionTimeout": "30m"
        },
        "acceptInsecureCerts": True,
    }

    for k, v in caps.items():
        options.set_capability(k, v)

    driver = webdriver.Remote(
        command_executor=executor_url,
        options=options
    )

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
