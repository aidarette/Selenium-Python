from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

link = "http://selenium1py.pythonanywhere.com"

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        """
        Открываем главную страницу;
        Проверяем, что мы можем перейти на страницу для входа/регистрации.
        """
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
   
    def test_guest_should_see_login_link(self, browser):
        """
        Открываем главную страницу;
        Проверяем, что мы видим страницу для входа/регистрации.
        """
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

@pytest.mark.login_form
class TestLoginFromMainPages():
    def test_guest_should_see_login_url(self,browser):
        """
        Открываем страницу для входа/регистрации;
        Проверяем, что мы видим правильный url для входа/регистрации.
        """
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.should_be_login_url()
 
    def test_guest_should_see_login_form(self,browser):
        """
        Открываем страницу для входа/регистрации;
        Проверяем, что мы видим форму для входа.
        """
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.should_be_login_form()
   
    def test_guest_should_see_registration_form(self,browser):
        """
        Открываем страницу для входа/регистрации;
        Проверяем, что мы видим форму для регистрации.
        """
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.should_be_registration_form()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """
    Проверка пустой корзины незалогиненного пользователя
    Ожидаемый результат:
    1) Гость открывает страницу товара;
    2) Переходит в корзину по кнопке в шапке ;
    3) Ожидаем, что в корзине нет товаров;
    4) Ожидаем, что есть текст о том что корзина пуста; 
    """
    page = BasketPage(browser, link)
    page.open()
    page.click_to_basket_button()
    page.should_not_be_basket_items()
    page.basket_should_be_empty_text()