import allure
from data import Urls
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):

    @allure.step('Клик по кнопке История заказов')
    def click_order_history_button(self):
        self.click_on_element(HomePageLocators.ORDER_HISTORY_BUTTON)
        self.wait_until_url_loaded(Urls.ACCOUNT_ORDER_HISTORY_URL)
        return self.get_current_url()

    @allure.step('Клик на кнопку "Выход"')
    def click_logout_button(self):
        self.click_on_element(HomePageLocators.LOGOUT_BUTTON)
        self.wait_until_url_loaded(Urls.LOGIN_URL)
        return self.get_current_url()
