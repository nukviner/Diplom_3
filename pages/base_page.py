import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common import TimeoutException


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Поиск элемента с ожиданием')
    def find_element(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Пролистывание до видимости элемента')
    def scroll_into_view(self, locator):
        el = self.find_element(locator)
        ActionChains(self.driver).move_to_element(el).perform()

    @allure.step('Ожидание кликабельности элемента')
    def wait_until_element_clickable(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    @allure.step('Клик на элемент')
    def click_on_element(self, locator):
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).click().perform()

    @allure.step('Получение текста элемента')
    def get_text_from_element(self, locator):
        element = self.find_element(locator)
        return element.text

    @allure.step('Ожидание загрузки страницы')
    def wait_until_url_loaded(self, url):
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(url))

    @allure.step('Получение URL страницы')
    def get_page_url(self, url):
        self.driver.get(url)

    @allure.step('Получить текущий URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Ожидание появления элемента')
    def wait_element_located(self, locator):
        try:
            WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step('Ожидание получения текста, который будет изменён')
    def wait_for_text(self, locator, initial_text):
        WebDriverWait(self.driver, 3).until(lambda driver: self.find_element(locator).text != initial_text)

    @allure.step('Ожидание изменения текста')
    def wait_for_text_change(self, locator, expected_text):
        WebDriverWait(self.driver, 3).until(lambda driver: self.find_element(locator).text == expected_text)

    @allure.step('Cкрипт на JS для перетаскивания элементов')
    def drag_and_drop_element(self, source_locator, target_locator):
        from_element = self.find_element(source_locator)
        to_element = self.find_element(target_locator)

        self.driver.execute_script("""
            const [from_element, to_element] = arguments;
            const dataTransfer = new DataTransfer();

            ['dragstart', 'dragover', 'drop', 'dragend'].forEach(eventType => {
                const event = new DragEvent(eventType, { bubbles: true, cancelable: true, dataTransfer });
                (eventType === 'dragstart' ? from_element : to_element).dispatchEvent(event);
            });
        """, from_element, to_element)
