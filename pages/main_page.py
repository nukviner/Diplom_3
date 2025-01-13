import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from data import Urls


class MainPage(BasePage):

    @allure.step('Клик на кнопку Личный кабинет')
    def click_lk_button(self):
        self.click_on_element(MainPageLocators.LK_BUTTON)
        self.wait_until_url_loaded(Urls.HOME_PAGE_URL)
        return self.get_current_url()

    @allure.step('Клик на кнопку Конструктор')
    def click_constructor_button(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Клик на кнопку Лента заказов')
    def click_order_feed_button(self):
        self.click_on_element(MainPageLocators.ORDER_FEED_BUTTON)
        self.wait_until_url_loaded(Urls.FEED_URL)
        return self.get_current_url()

    @allure.step('Клик на кнопку Ингредиент')
    def click_ingredient(self):
        self.click_on_element(MainPageLocators.BURGER_INGREDIENT_BUN)

    @allure.step('Ожидание всплывающего окна с деталями ингредиента')
    def wait_popup_ingredient_details(self):
        return self.wait_element_located(MainPageLocators.POPUP_WINDOW)

    @allure.step('Добавление булки в заказ')
    def drag_and_drop_bun(self):
        return self.drag_and_drop_element(MainPageLocators.BURGER_INGREDIENT_BUN, MainPageLocators.BURGER_CONSTRUCTOR_BASKET)

    @allure.step('Добавление соуса в заказ')
    def drag_and_drop_sauce(self):
        return self.drag_and_drop_element(MainPageLocators.BURGER_INGREDIENT_SAUCE, MainPageLocators.BURGER_CONSTRUCTOR_BASKET)

    @allure.step('Проверка количества ингредиентов')
    def check_number_ingredient(self):
        return self.get_text_from_element(MainPageLocators.COUNTER_BUN)

    @allure.step('Клик на кнопку Оформить заказ')
    def click_order_button(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON)

    @allure.step('Закрытие окна ингредиентов')
    def close_ingredients_window(self):
        self.click_on_element(MainPageLocators.CLOSE_BUTTON)

    @allure.step('Получение ID заказа')
    def get_order_id_from_popup(self):
        self.wait_for_text(
            MainPageLocators.ORDER_ID_TITLE,
            initial_text="9999")
        el = self.find_element(MainPageLocators.ORDER_ID_TITLE)
        order_id = el.text
        return order_id

    @allure.step('Ожидание заголовка Соберите Бургер')
    def wait_for_title_burger(self):
        return self.wait_element_located(MainPageLocators.MAKE_BURGER_TITLE)

    @allure.step('Ожидание всплывающего окна заказа')
    def wait_for_popup_order(self):
        return self.wait_element_located(MainPageLocators.POPUP_ORDER)

    @allure.step("Создание заказа")
    def create_order(self):
        self.drag_and_drop_bun()
        self.drag_and_drop_sauce()
        self.click_order_button()
        self.get_order_id_from_popup()
        self.close_ingredients_window()
