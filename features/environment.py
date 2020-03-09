from behave import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver

SELENIUM_NODE = "http://192.168.99.100:4444/wd/hub"


@fixture
def driver(context):
    chrome_options = Options()
    desired_capabilities = chrome_options.to_capabilities()
    context.driver = WebDriver(command_executor=SELENIUM_NODE, desired_capabilities=desired_capabilities)

    # context.driver = webdriver.Chrome("/usr/local/bin/chromedriver")
    yield context.driver
    context.driver.quit()


@fixture
def bike(context):
    context.bike = {"make": None, "model": None, "capacity": None}
    yield context.bike
    context.bike = None


def before_feature(context, feature):
    use_fixture(driver, context)
    use_fixture(bike, context)