import pytest
from selenium import webdriver


def take_screenshot(driver, test_name):
    screenshot_dir = "report"
    screenshot_file = f"{screenshot_dir}/{test_name}.png"
    driver.save_screenshot(screenshot_file)


@pytest.fixture()
def browser(request):
    driver = webdriver.Chrome()
    yield driver
    if request.session.testsfailed:
        test_name = request.node.name
        take_screenshot(driver, test_name)
    driver.quit()
