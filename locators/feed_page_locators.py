from selenium.webdriver.common.by import By


class FeedPageLocators:
    CONSTRUCTOR_BUTTON = By.XPATH, "//p[text()='Конструктор']"
    HOME_PAGE = By.XPATH, "//p[text()='Личный Кабинет']"
    ORDER_FEED_ITEM_BY_ID = By.XPATH, "//p[contains(@class, 'text_type_digits-default') and contains(text(), '{order_id}')]"
    ORDER_lIST_WINDOW_POPUP = By.CLASS_NAME, "Modal_modal__container__Wo2l_"
    READY_ORDER = By.CSS_SELECTOR, ".OrderFeed_orderListReady__1YFem .text_type_digits-default"
    LAST_ORDER_IN_HISTORY = By.XPATH, f"(//p[contains(@class, 'text_type_digits-default')])[last()]"
    TOTAL_TODAY = [By.XPATH, ".//div[not(@class)]/p[@class = 'OrderFeed_number__2MbrQ text text_type_digits-large']"]
    TOTAL_ALL = [By.XPATH, "//div[@class = 'undefined mb-15']/p[@class = 'OrderFeed_number__2MbrQ text text_type_"
                           "digits-large']"]
