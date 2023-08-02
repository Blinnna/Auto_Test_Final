from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_BUTTON = (By.XPATH, '//span//a[contains(@href, "basket")]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    pass     

class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_FORM_EMAIL = (By.XPATH, '//input[@name="registration-email"]')
    REGISTER_FORM_PASSWORD = (By.XPATH, '//input[@name="registration-password1"]')
    REGISTER_FORM_PASSWORD_REPEAT = (By.XPATH, '//input[@name="registration-password2"]')
    REGISTER_FORM_SUBMIT_BUTTON = (By.XPATH, '//button[@name="registration_submit"]')
    
class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    CURRENT_GOOD_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    ALERT_ADDED_GOOD_NAME = (By.XPATH, '//div[contains(@class, "alert-succes")][1]//strong')
    CURRENT_GOOD_PRICE = (By.XPATH, '//div[contains(@class, "product_main")]//p[@class="price_color"]')
    ALERT_ADDED_GOOD_PRICE = (By.XPATH, '//div[contains(@class, "alert-info")]//strong')
    
class BasketPageLocators():
    EMPTY_BASKET_NOTIFICATION = (By.XPATH, '//div[@id="content_inner"]//p')
    BASKET_ITEM_LIST_TITLE = (By.XPATH, '//div[contains(@class, "basket-title")]//h2')
    

    