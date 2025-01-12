import allure
from locators.password_reset_locators import PasswordResetLocators
from pages.base_page import BasePage


@allure.title('Описание методов страницы восстановления пароля')
class ResetPasswordPage(BasePage):

    @allure.step('Ожидание активации поля ввода пароля')
    def wait_for_password_input(self):
        return self.wait_element_located(PasswordResetLocators.PASSWORD_INPUT_BEFORE)

    @allure.step('Клик по кнопке Показать/Скрыть пароль')
    def click_password_visibility_button(self):
        self.click_on_element(PasswordResetLocators.PASSWORD_BUTTON)

    @allure.step('Проверка активации кнопки Показать/Скрыть пароль')
    def check_password_field_active(self):
        return self.wait_element_located(PasswordResetLocators.PASSWORD_INPUT_AFTER)
