import pytest
from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
from selenium.webdriver.common.by import By
import time 


@pytest.mark.product_in_basket
class TestBasketFromAnyPage():
    @pytest.mark.need_review
    @pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                      pytest.param(7, marks=pytest.mark.xfail),
                                      8, 9])
    def test_guest_can_add_product_to_basket(self, browser, link):
        """
        Проверка успешного добавления продукта в корзину незалогиненного пользователя
        Ожидаемый результат:
        1) Сообщение о том, что товар добавлен в корзину.
        Название товара в сообщении должно совпадать с тем товаром, который был действительно добавлен
        2) Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.
        """
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
        page = ProductPage(browser, link)
        page.open()
        page.click_add_to_basket_button()
        page.solve_quiz_and_get_code()  
        page.should_be_product_in_basket()
        page.price_in_basket_should_be_match()
    
    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        """
        Открываем страницу товара;
        Проверяем, что есть сообщение об успешном добавлении продукта в корзину с помощью is_not_element_present, хотя не должно.
        """
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.click_add_to_basket_button()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        """
        Открываем страницу товара;
        Проверяем, что нет сообщения об успехе с помощью is_not_element_present.
        """
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
    
    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        """
        Открываем страницу товара;
        Кликаем на кнопку добавления товара в корзину;
        Проверяем, что есть сообщение об успехе с помощью is_disappeared, хотя не должно.
        """
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.click_add_to_basket_button()
        page.should_dissapear_of_success_message()
    
    @pytest.mark.need_review    
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self,browser):
        """
        Проверка пустой корзины незалогиненного пользователя
        Ожидаемый результат:
        1) Гость открывает страницу товара;
        2) Переходит в корзину по кнопке в шапке ;
        3) Ожидаем, что в корзине нет товаров;
        4) Ожидаем, что есть текст о том что корзина пуста; 
        """
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = BasketPage(browser, link)
        page.open()
        page.click_to_basket_button()
        page.should_not_be_basket_items()
        page.basket_should_be_empty_text()

@pytest.mark.login_link
class TestLoginFromProductPage():
    def test_guest_should_see_login_link_on_product_page(self,browser):
        """
        Открываем страницу товара;
        Проверяем, что на странице есть кнопка для входа/регистрации.
        """
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()
    
    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page (self,browser):
        """
        Открываем страницу товара;
        Проверяем, что мы можем перейти на страницу для входа/регистрации.
        """
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        
@pytest.mark.add_to_basket
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        """
        Открыть страницу регистрации;
        Зарегистрировать нового пользователя;
        Проверить, что пользователь залогинен.
        """
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        page.register_new_user(email, password)
        page.should_be_authorized_user()
        
    def test_user_cant_see_success_message(self, browser):
        """
        Открываем страницу товара;
        Проверяем, что нет сообщения об успехе с помощью is_not_element_present.
        """
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
    
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        """
        Проверка успешного добавления продукта в корзину залогиненного пользователя
        Ожидаемый результат:
        1) Сообщение о том, что товар добавлен в корзину.
        Название товара в сообщении должно совпадать с тем товаром, который был действительно добавлен
        2) Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.
        """
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.click_add_to_basket_button()  
        page.should_be_product_in_basket()
        page.price_in_basket_should_be_match()