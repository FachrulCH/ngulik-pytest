import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class InventoryPage(BasePage):
    URL = 'https://www.saucedemo.com/inventory.html'
    INVENTORY = (By.ID, 'inventory_container')
    CART_BADGE = (By.CSS_SELECTOR, '.shopping_cart_badge')
    SIDE_MENU = (By.CSS_SELECTOR, '.bm-burger-button button')
    LOGOUT_MENU = (By.ID, 'logout_sidebar_link')
    BTNs_ADD_CART = (By.CSS_SELECTOR, '.btn_inventory')
    TXT_SHOPPING_CART_BADGE = (By.CSS_SELECTOR, '.shopping_cart_badge')

    def __init__(self, driver: webdriver.Remote):
        super(InventoryPage, self).__init__(driver)
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def should_loaded(self):
        assert self.driver.title == 'Swag Labs'
        assert self.element(self.INVENTORY).is_displayed()
        assert len(self.driver.find_elements(*self.CART_BADGE)) == 0
        assert self.driver.current_url == self.URL

    def user_logout(self):
        self.element(self.SIDE_MENU).click()
        time.sleep(1)  # wait animation open menu
        self.element(self.LOGOUT_MENU).click()
        time.sleep(1)
        assert self.driver.current_url == 'https://www.saucedemo.com/index.html'

    def btn_add_cart(self):
        return self.driver.find_elements(*self.BTNs_ADD_CART)

    def get_shopping_cart_counter(self):
        return int(self.element(self.TXT_SHOPPING_CART_BADGE).text)



