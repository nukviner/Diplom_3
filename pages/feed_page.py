import allure
from data import Urls
from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


@allure.title('Описание методов заказов')
class FeedPage(BasePage):

    @allure.step('Клик по "Конструктору"')
    def click_on_constructor(self):
        self.click_on_element(FeedPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Поиск заказа и клик по нему')
    def click_on_order(self):
        el = By.XPATH, FeedPageLocators.ORDER_FEED_ITEM_BY_ID[0]
        return self.click_on_element(el)

    @allure.step('Ожидание всплывающего окна с заказами')
    def wait_of_order_list(self):
        return self.wait_element_located(FeedPageLocators.ORDER_lIST_WINDOW_POPUP)

    @allure.step('Получение заказа из списка заказов')
    def get_order_from_list(self):
        el = self.find_element(FeedPageLocators.READY_ORDER)
        order_id = el.text.strip()
        return order_id

    @allure.step('Переход в личный кабинет')
    def click_homepage(self):
        self.click_on_element(FeedPageLocators.HOME_PAGE)
        self.wait_until_url_loaded(Urls.HOME_PAGE_URL)
        return self.get_current_url()

    @allure.step('Поиск и клик по элементу')
    def find_and_click_order_by_id(self, order_id):
        locator = By.XPATH, FeedPageLocators.ORDER_FEED_ITEM_BY_ID[1].format(order_id=order_id)
        return self.click_on_element(locator)

    @allure.step("Cкролл до созданного заказа в истории заказов")
    def scroll_order_in_history(self):
        self.scroll_into_view(FeedPageLocators.LAST_ORDER_IN_HISTORY)

    @allure.step('Поиск элемента по ID')
    def find_order_by_id(self, order_id):
        locator = By.XPATH, f"//p[contains(@class, 'text_type_digits-default') and text()='#0{order_id}']"
        el = self.find_element(locator)
        assert el, f"Заказ с ID {order_id} не найден."

    @allure.step('Ожидание заказа в статусе "В работе"')
    def wait_for_orders_id(self, expected_order_id):
        self.wait_for_text_change(
            locator = FeedPageLocators.READY_ORDER,
            expected_text = f'0{expected_order_id}'
        )

    @allure.step('Получение количества "Выполнено за все время')
    def get_count_total_all(self):
        total_all = self.find_element(FeedPageLocators.TOTAL_ALL).text
        return total_all

    @allure.step('Получение количества "Выполнено за сегодня"')
    def get_count_total_today(self):
        total_today = self.find_element(FeedPageLocators.TOTAL_TODAY).text
        return total_today
