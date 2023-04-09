from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators
from .locators import MainPageLocators

class BasketPage(BasePage):
    def should_not_be_basket_items(self):
        """
        Метод для проверки наличия/отсутствия товаров в корзине
        """
        assert self.is_not_element_present(*MainPageLocators.BASKET_ITEMS), \
        "Basket items is presented, but should not be"
    
    def basket_should_be_empty_text(self):
        """
        Метод для проверки наличия/отсутствия сообщения о наличии товаров в корзине
        """
        basket_is_empty_text = self.browser.find_element(*MainPageLocators.BASKET_EMPTY_TEXT)
        assert "Your basket is empty. Continue shopping" == basket_is_empty_text.text, "There are products in the basket, but should not be"