from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
from .locators import MainPageLocators

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        
    def open(self):
        self.browser.get(self.url)
        
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    
    def is_element_present(self, how, what):
        """
        Метод для проверки наличия чего либо на странице
        """
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
    
    def is_not_element_present(self, how, what, timeout=4):
        """
        Метод для проверки отсутствия чего либо на странице
        """
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False
    
    def is_disappeared(self, how, what, timeout=4):
        """
        Метод для проверки наличия/отсутствия чего либо на странице
        """
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True
        
    def go_to_login_page(self):
        """
        Метод для перехода на страницу входа/регистрации
        """
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        """
        Метод для проверки наличия/отсутствия кнопки входа/регистрации 
        """
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
        
    def click_to_basket_button(self):
        """
        Метод для перехода в корзину пользователя
        """
        basket_button = self.browser.find_element(*MainPageLocators.BASKET_BTN)
        basket_button.click()
            
    def should_be_authorized_user(self):
        """
        Метод для проверки авторизован ли пользователь
        """
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"