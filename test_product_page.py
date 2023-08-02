from selenium.webdriver.common.by import By
from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.locators import BasePageLocators
from .pages.locators import MainPageLocators
from .pages.locators import LoginPageLocators
from .pages.locators import ProductPageLocators
from .pages.locators import BasketPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest
import math

# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2"
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
login_page_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
def test_guest_can_add_product_to_basket(browser, link):
    page=ProductPage(browser, link)
    page.open()
    page.add_item_to_cart()
    time.sleep(1)
    page.solve_quiz_and_send_code()
    time.sleep(10)
    page.check_added_item()
    page.check_cart_price()

@pytest.mark.skip	
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page=ProductPage(browser, link)
    page.open()
    page.add_item_to_cart()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page=ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
   
def test_message_disappeared_after_adding_product_to_basket(browser):
    page=ProductPage(browser, link)
    page.open()
    page.add_item_to_cart()
    page.success_message_is_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.move_to_basket() # перемещаемся в корзину
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.empty_basket_should_have_empty_message()
    basket_page.empty_basket_should_not_have_items()  

   
@pytest.mark.need_review
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)    
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = "4$h1hFlBcC!6Vo9i"
        # password = "12345678"
        self.page=LoginPage(browser, login_page_link)
        self.page.open()
        self.page.register_new_user(email,password)
        self.page.should_be_authorized_user()    
        
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        self.page = ProductPage(browser, link)
        self.page.open()
        self.page.should_not_be_success_message()
     
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        self.page = ProductPage(browser, link)
        self.page.open()
        self.page.add_item_to_cart()
        self.page.check_added_item()
        self.page.check_cart_price()
    
    
    



    


    