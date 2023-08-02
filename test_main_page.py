from selenium.webdriver.common.by import By
from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.locators import BasePageLocators
from .pages.locators import MainPageLocators
from .pages.locators import LoginPageLocators
from .pages.locators import ProductPageLocators
from .pages.locators import BasketPageLocators
from selenium.common.exceptions import TimeoutException
import time
import pytest

link = "http://selenium1py.pythonanywhere.com/"
login_page_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

def test_login_page_url(browser): 
    page=LoginPage(browser, login_page_link)
    page.open()
    page.should_be_login_url()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser): # Гость, при открытии корзины - кордина пустая. 
    page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес  
    page.open() # открываем страницу
    page.move_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.empty_basket_should_have_empty_message()
    basket_page.empty_basket_should_not_have_items()
    time.sleep(10)    


@pytest.mark.login_guest
class TestLoginFromMainPage():
    # не забываем передать первым аргументом self                       
    def test_guest_can_go_to_login_page(self, browser):     
         # реализация теста
        page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу
        page.go_to_login_page() # переходим на строницу логина
        login_page = LoginPage(browser, browser.current_url) # копируем текущий url в переменную
        login_page.should_be_login_page() # проверяем, что ссылка содержит слово логин

    def test_guest_should_see_login_link(self, browser):
        # реализация теста    
        page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open() # открываем страницу
        page.should_be_login_link() # проверяем есть ли на странице ссылка на страницу авторизации