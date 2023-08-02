from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from .locators import MainPageLocators
from .login_page import LoginPage

class MainPage(BasePage):
    
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
       