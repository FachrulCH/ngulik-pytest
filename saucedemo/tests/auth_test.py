import time
from selenium import webdriver

from pages.inventory import InventoryPage
from pages.login import LoginPage


def test_invalid_login(browser: webdriver.Remote):
    login_page = LoginPage(browser)
    login_page.load()
    login_page.login_with('asal', 'passwd')
    login_page.should_failed_login()
    time.sleep(2)


def test_valid_login(browser):
    login_page = LoginPage(browser)
    inventory_page = InventoryPage(browser)

    login_page.load()
    login_page.login_with('standard_user', 'secret_sauce')
    inventory_page.should_loaded()


def test_logout_success(browser):
    login_page = LoginPage(browser)
    inventory_page = InventoryPage(browser)

    login_page.load()
    login_page.login_with('standard_user', 'secret_sauce')
    inventory_page.should_loaded()
    inventory_page.user_logout()