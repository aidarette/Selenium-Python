from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
   
class LoginPageLocators():
    LOGIN_FORM = (By.ID, "id_login-username")
    REGISTRATION_FORM = (By.ID, "id_registration-email")

class ProductPageLocators():
    BASKET_BTN = (By.CLASS_NAME, "btn-add-to-basket")
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, "p.price_color")
    TOTAL_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, "h1")
    SECOND_NAME_OF_PRODUCT = (By.CSS_SELECTOR, ".alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")
    
