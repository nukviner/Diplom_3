import allure
from data import Urls


@allure.title('Проверки основного функционала')
class TestMainPage:

    @allure.title('Проверка перехода по клику на кнопку Конструктор')
    def test_click_to_constructor(self, main_page, login_in):
        main_page.click_constructor_button()

        assert main_page.wait_for_title_burger()

    @allure.title('Проверка перехода по клику на кнопку Лента заказов')
    def test_click_to_order_feed(self, main_page, login_in):
        curr_url = main_page.click_order_feed_button()

        assert curr_url == Urls.FEED_URL

    @allure.title('Проверка появления всплывающего окна с деталями по клику на ингредиент')
    def test_open_ingredient_details(self, main_page, login_in):
        main_page.click_ingredient()

        assert main_page.wait_popup_ingredient_details()

    @allure.title('Проверка закрытия всплывающего окна деталей кликом по крестику')
    def test_close_window_detail(self, main_page, login_in):
        main_page.click_ingredient()
        main_page.close_ingredients_window()
        assert main_page.wait_popup_ingredient_details() == False

    @allure.title('Проверка увеличения каунтера ингредиента при добавлении его в заказ')
    def test_add_ingredient_to_order(self, main_page, login_in):
        main_page.drag_and_drop_bun()

        assert main_page.check_number_ingredient() == '2'

    @allure.title('Проверка возможности оформления заказа залогиненным пользователем')
    def test_make_order_as_auth_user(self, main_page, login_in):
        main_page.drag_and_drop_bun()
        main_page.drag_and_drop_sauce()
        main_page.click_order_button()
        order_id = main_page.get_order_id_from_popup()

        assert main_page.wait_for_popup_order() and order_id is not None
