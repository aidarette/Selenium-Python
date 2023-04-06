from selenium.common.exceptions import NoAlertPresentException
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import math 

class ProductObject(BasePage, ProductPageLocators):
    def click_to_basket_button(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BTN)
        basket_button.click()
        
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
  
    def should_be_product_in_basket(self):
        name = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT)
        second_name = self.browser.find_element(*ProductPageLocators.SECOND_NAME_OF_PRODUCT)
        assert name.text == second_name.text, 'Naming is the same'
    
    def price_in_basket_should_be_match(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT)
        second_price = self.browser.find_element(*ProductPageLocators.TOTAL_PRICE)
        assert price.text == second_price.text, 'Price is the same'
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"
    
    def should_dissapear_of_success_message()(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is not disappeared"