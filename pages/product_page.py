from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

class ProductPage(BasePage):
    def add_item_to_cart(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()
    
    def check_added_item(self):
        added_item = self.browser.find_element(*ProductPageLocators.CURRENT_GOOD_NAME)
        added_item_text = added_item.text
    
        alert_item = self.browser.find_element(*ProductPageLocators.ALERT_ADDED_GOOD_NAME)
        alert_item_text = alert_item.text
        assert added_item_text == alert_item.text, "Added item does not mach the alert"
    
    def check_cart_price(self):
        added_item_price = self.browser.find_element(*ProductPageLocators.CURRENT_GOOD_PRICE)
        added_item_price_text = added_item_price.text
        
        alert_item_price = self.browser.find_element(*ProductPageLocators.ALERT_ADDED_GOOD_PRICE)
        alert_item_price_text = alert_item_price.text
        assert added_item_price_text == alert_item_price_text, "Item price does not mach the alert"
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_ADDED_GOOD_NAME), \
            "Success message is presented, but should not be"

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_ADDED_GOOD_NAME), \
            "Success message is presented, but should not be"