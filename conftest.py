import csv
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

    accounts = []
    with open('../TestData/standard_user_credential.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            accounts.append(line)
            print(accounts)

    username = (line[0])
    password = (line[1])

    login_page.open_login_page()
    login_page.input_username(username)
    login_page.input_password(password)
    login_page.click_login_button()
    login_page.wait_for_profile_page()


@pytest.fixture()
def login2(driver):
    login_page = LoginPage(driver)

    accounts = []
    with open('../TestData/locked_out_user_credential.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            accounts.append(line)
            print(accounts)

    username = (line[0])
    password = (line[1])

    login_page.open_login_page()
    login_page.input_username(username)
    login_page.input_password(password)
    login_page.click_login_button()
    login_page.wait_for_profile_page()
