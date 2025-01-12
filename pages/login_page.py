import allure
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from data import Urls


@allure.title('Описание методов страницы логина')
class LoginPage(BasePage):

    @allure.step('Клик по кнопке Восстановить пароль')
    def click_reset_password_button(self):
        self.click_on_element(LoginPageLocators.RESET_BUTTON)
        self.wait_until_url_loaded(Urls.FORGOT_PASSWORD_URL)
        return self.get_current_url()

    @allure.step('Заполнение поля email')
    def set_email(self, email):
        self.find_element(LoginPageLocators.EMAIL_FIELD).send_keys(email)

    @allure.step('Заполнение поля Пароль')
    def set_password(self, password):
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(password)

    @allure.step('Клик по кнопке логина')
    def click_log_in_button(self):
        self.click_on_element(LoginPageLocators.LOGIN_BUTTON)
        self.wait_until_url_loaded(Urls.MAIN_URL)
        return self.get_current_url()
