import allure
from locators.forget_password_locators import ForgetPasswordLocators
from pages.base_page import BasePage
from data import Urls


@allure.title('Описание методов восстановления пароля')
class ForgetPasswordPage(BasePage):

    @allure.step('Заполнение поля email')
    def set_email(self, email):
        self.find_element(ForgetPasswordLocators.EMAIL_FIELD).send_keys(email)

    @allure.step('Клик по кнопке Восстановить пароль')
    def click_reset_password_button(self):
        self.click_on_element(ForgetPasswordLocators.RESET_BUTTON)
        self.wait_until_url_loaded(Urls.RESET_PASSWORD_URL)
        return self.get_current_url()
