from selenium.webdriver.common.by import By


class ForgetPasswordLocators:
    EMAIL_FIELD = By.XPATH, "//input[@name='name']"
    RESET_BUTTON = By.XPATH, "//button[text()='Восстановить']"
