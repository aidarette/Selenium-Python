from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") #кнопка для входа/регистрации
    BASKET_BTN = (By.CSS_SELECTOR, ".btn-group .btn-default") # кнопка для перехода в корзину пользователя
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items") #выбирает все товары в корзине
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner") #текст, об отсутствии товаров в корзине
       
class LoginPageLocators():
    LOGIN_FORM = (By.ID, "id_login-username") #форма для авторизации
    REGISTRATION_FORM = (By.ID, "id_registration-email") #форма для регистрации
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email") #поле для email'a
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1") #поле для пароля
    REGISTRATION_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2") #поле для подтверждения пароля
    REGISTER_BTN = (By.NAME, "registration_submit") #кнопка для отправки формы регистрации
    
class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CLASS_NAME, "btn-add-to-basket") #кнопка добавления товара в корз
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, "p.price_color") #цена продукта
    TOTAL_PRICE = (By.CSS_SELECTOR, ".alertinner p strong") #общая сумма корзины, после добавления товаров в неё
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, "h1") #наименование товара
    SECOND_NAME_OF_PRODUCT = (By.CSS_SELECTOR, ".alertinner strong") #наименования товара/ов, добавленных в корзину
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner") #сообщение об успешном добавлении товаров в корзину
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") #кнопка для входа/регистрации
    USER_ICON = (By.CSS_SELECTOR, ".icon-user") #иконка залогиненного пользователя
