from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    URL = "https://www.saucedemo.com/"
    USER_NAME = (By.ID, 'user-name')
    PASSWORD = (By.ID, 'password')
    BTN_LOGIN = (By.CSS_SELECTOR, '.btn_action')
    ERROR = (By.CSS_SELECTOR, 'h3[data-test="error"]')
    ERROR_TEXT = "Username and password do not match any user in this service"
    INVENTORY = (By.ID, 'inventory_container')

    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        
    def load(self):
        self.driver.get(self.URL)
        
    def login_with(self, username: str, passwd: str):
        self.driver.find_element(*self.USER_NAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(passwd)
        self.driver.find_element(*self.BTN_LOGIN).click()

    def should_failed_login(self):
        assert self.ERROR_TEXT in self.driver.find_element(*self.ERROR).text
        assert self.driver.current_url == self.URL

    def should_success(self):
        assert self.driver.find_element(*self.INVENTORY).is_displayed()
        assert self.driver.current_url == 'https://www.saucedemo.com/inventory.html'