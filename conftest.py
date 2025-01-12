import pytest
from selenium import webdriver
from helpers import register_user, delete_user
from pages.main_page import MainPage
from pages.home_page import HomePage
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.forget_password_page import ForgetPasswordPage
from pages.reset_password_page import ResetPasswordPage
from data import Urls


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    if request.param == 'firefox':
        driver = webdriver.Firefox()
    elif request.param == 'chrome':
        driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture()
def main_page(driver):
    page = MainPage(driver)
    page.get_page_url(Urls.MAIN_URL)
    return page

@pytest.fixture()
def home_page(driver):
    page = HomePage(driver)
    page.get_page_url(Urls.HOME_PAGE_URL)
    return page

@pytest.fixture()
def feed_page(driver):
    page = FeedPage(driver)
    page.get_page_url(Urls.FEED_URL)
    return page

@pytest.fixture()
def login_page(driver):
    page = LoginPage(driver)
    page.get_page_url(Urls.LOGIN_URL)
    return page

@pytest.fixture()
def forget_password_page(driver):
    page = ForgetPasswordPage(driver)
    page.get_page_url(Urls.FORGOT_PASSWORD_URL)
    return page

@pytest.fixture()
def reset_password_page(driver):
    page = ResetPasswordPage(driver)
    page.get_page_url(Urls.RESET_PASSWORD_URL)
    return page

@pytest.fixture()
def login():
    data_user, response = register_user()
    yield data_user
    access_token = data_user.get('accessToken')
    delete_user(access_token)

@pytest.fixture()
def login_in(login, login_page):
    email = login['email']
    password = login['password']
    login_page.set_email(email)
    login_page.set_password(password)
    login_page.click_log_in_button()

@pytest.fixture()
def order_id(main_page, login_in):
    main_page.drag_and_drop_bun()
    main_page.drag_and_drop_sauce()
    main_page.click_order_button()
    order_id = main_page.get_order_id_from_popup()
    main_page.close_ingredients_window()
    return order_id
