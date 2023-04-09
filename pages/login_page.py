from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators
from .locators import MainPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        
    def go_to_login_page(self):
        """
        Метод для перехода на страницу входа/регистрации
        """
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        
    def should_be_login_url(self):
        """
        Метод для проверки наличия/отсутствия ключевого слова "login" в url 
        """
        assert "login" in self.browser.current_url, "Login is not in current url"

    def should_be_login_form(self):
        """
        Метод для проверки наличия/отсутствия формы авторизации
        """
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_registration_form(self):
        """
        Метод для проверки наличия/отсутствия формы регистрации
        """
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"
    
    def register_new_user(self, email, password):
        """
        Метод для заполнения формы регистрации нового пользователя
        """
        email_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_input.send_keys(email)
        create_password = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        create_password.send_keys(password)
        confirm_password = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM)
        confirm_password.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        register_button.click()
 