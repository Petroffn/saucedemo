import allure
import pytest
from selenium import webdriver
from pages.login_page import LoginPage


@pytest.fixture()
def driver(request):
    with allure.step('Open Browser'):
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.implicitly_wait(5)
        request.addfinalizer(driver.quit)
        return driver


@pytest.fixture()
def login(driver):
    login_page = LoginPage(driver)

    username = 'standard_user'
    password = 'secret_sauce'

    login_page.open_login_page()
    login_page.input_username(username)
    login_page.input_password(password)
    login_page.click_login_button()
    login_page.wait_for_profile_page()
