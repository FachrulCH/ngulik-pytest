import pytest
from selenium import webdriver

from pages.login import LoginPage


def take_screenshot(driver, test_name):
    screenshot_dir = "report"
    screenshot_file = f"{screenshot_dir}/{test_name}.png"
    print(f"Test Failed, taking screenshot {screenshot_file}")
    driver.save_screenshot(screenshot_file)


@pytest.fixture()
def browser(request):
    driver = webdriver.Chrome()
    yield driver
    if request.session.testsfailed:
        test_name = request.node.name
        take_screenshot(driver, test_name)
    driver.quit()


def login(browser):
    login_page = LoginPage(browser)
    login_page.load()
    login_page.login_with('standard_user', 'secret_sauce')