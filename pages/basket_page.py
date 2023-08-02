from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from .locators import BasketPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

class BasketPage(BasePage):
    def empty_basket_should_have_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_NOTIFICATION), \
            "Empty message is missing"
    
    def empty_basket_should_not_have_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM_LIST_TITLE), \
            "Something in the basket, but should not be"   