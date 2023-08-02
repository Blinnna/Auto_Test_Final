from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "URL does not contain login"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not presented"

    def open(self):
        self.browser.get(self.url)   
    
    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
        email_input.send_keys(email)
        password_inpit1 = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD)
        password_inpit1.send_keys(password)
        password_inpit2 = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_REPEAT)
        password_inpit2.send_keys(password)
        submit_button = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_SUBMIT_BUTTON)
        submit_button.click()         
        
        