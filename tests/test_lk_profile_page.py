import allure
from data import Urls


class TestLkProfilePage:

    @allure.title('Проверка перехода по клику на Личный кабинет')
    def test_click_lk_button(self, main_page, login_in):
        current_url = main_page.click_lk_button()

        assert current_url == Urls.HOME_PAGE_URL

    @allure.title('Проверка перехода в раздел История заказов')
    def test_click_history_button(self, login_in, home_page):
        current_url = home_page.click_order_history_button()

        assert current_url == Urls.ACCOUNT_ORDER_HISTORY_URL

    @allure.title('Проверка выхода из аккаунта')
    def test_logout_account_button(self, login_in, home_page):
        current_url = home_page.click_logout_button()

        assert current_url == Urls.LOGIN_URL
