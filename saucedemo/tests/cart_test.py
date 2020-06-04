import time

from conftest import login
from pages.inventory import InventoryPage


def test_add_to_cart_inventory(browser):
    login(browser)
    inventory_page = InventoryPage(browser)
    inventory_page.should_loaded()
    btns_add_cart = inventory_page.btn_add_cart()
    btns_add_cart[0].click()
    assert btns_add_cart[0].text == 'REMOVE'
    assert inventory_page.get_shopping_cart_counter() == 1

