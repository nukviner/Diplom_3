import allure
from data import Urls, TestData


class TestPassRecovery:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке Восстановить пароль')
    def test_password_recovery_button(self, login_page):
        curr_url = login_page.click_reset_password_button()

        assert curr_url == Urls.FORGOT_PASSWORD_URL

    @allure.title('Проверка перехода на страницу Восстановления пароля по кнопке Восстановить после ввода почты')
    def test_password_recovery_button_from_email(self, forget_password_page):
        email = TestData.TEST_EMAIL
        forget_password_page.set_email(email)
        curr_url = forget_password_page.click_reset_password_button()

        assert curr_url ==  Urls.RESET_PASSWORD_URL

    @allure.title('Проверка активности поля при клике по кнопке Показать/скрыть пароль')
    def test_password_field_activation(self, forget_password_page, reset_password_page):
        email = TestData.TEST_EMAIL
        forget_password_page.set_email(email)
        forget_password_page.click_reset_password_button()
        reset_password_page.wait_for_password_input()
        reset_password_page.click_password_visibility_button()

        assert reset_password_page.check_password_field_active()
