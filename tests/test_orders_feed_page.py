import allure


class TestFeedPage:

    @allure.title('Проверка отображения деталей заказа')
    def test_order_details_window(self, main_page, feed_page, order_id):
        main_page.click_order_feed_button()
        feed_page.find_and_click_order_by_id(order_id)

        assert feed_page.wait_of_order_list()

    @allure.title('Проверка отображения заказа из раздела История заказов в ленте заказов')
    def test_display_order_from_history(self, main_page, feed_page, home_page, order_id):
        main_page.click_order_feed_button()
        order_id_feed = feed_page.find_order_by_id(order_id)
        feed_page.click_homepage()
        home_page.click_order_history_button()
        feed_page.scroll_order_in_history()
        history_order_id = feed_page.find_order_by_id(order_id)

        assert order_id_feed == history_order_id

    @allure.title('Проверка увеличения счетчика Выполнено за все время при создании нового заказа')
    def test_increase_total_count(self, main_page, feed_page, home_page, order_id):
        main_page.click_order_feed_button()
        count_total_all = feed_page.get_count_total_all()
        main_page.click_constructor_button()
        main_page.create_order()
        main_page.click_constructor_button()
        main_page.click_order_feed_button()
        count_total_all_after_order = feed_page.get_count_total_all()

        assert count_total_all_after_order >= str(int(count_total_all))

    @allure.title('Проверка увеличения счетчика Выполнено за сегодня при создании нового заказа')
    def test_increase_today_count(self, main_page, feed_page, home_page, order_id):
        main_page.click_order_feed_button()
        count_total_today = feed_page.get_count_total_today()
        main_page.click_constructor_button()
        main_page.create_order()
        main_page.click_constructor_button()
        main_page.click_order_feed_button()
        count_total_today_after_order = feed_page.get_count_total_today()

        assert count_total_today_after_order >= str(int(count_total_today))

    @allure.title('Проверка отображения id созданного заказа в разделе В работе')
    def test_display_id_order(self, main_page, feed_page, order_id):
        main_page.click_order_feed_button()
        feed_page.wait_for_orders_id(order_id)

        assert f'0{order_id}' in  feed_page.get_order_from_list()
