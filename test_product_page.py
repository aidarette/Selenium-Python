from pages.product_page import ProductObject
from selenium.webdriver.common.by import By
import pytest

#@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
#                                  pytest.param(7, marks=pytest.mark.xfail),
#                                  8, 9])
#def test_guest_can_add_product_to_basket(browser, link):
#    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
#    page = ProductObject(browser, link)
#    page.open()
#    page.click_to_basket_button()
#    page.solve_quiz_and_get_code()  
#    page.should_be_product_in_basket()
 #   page.price_in_basket_should_be_match()
 
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductObject(browser, link)
    page.open()
    page.click_to_basket_button()
    page.should_not_be_success_message()
    
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductObject(browser, link)
    page.open()
    page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductObject(browser, link)
    page.open()
    page.click_to_basket_button()
    page.should_dissapear_of_success_message()()