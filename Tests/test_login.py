import allure
from pages.login_page import LoginPage


class TestLogin:
    @allure.title('Check user with locked credential')
    def test_user_cant_login_with_invalid_fields(self, login2, driver):
        login_page = LoginPage(driver)

        login_page.wait_for_profile_page()

    @allure.title('Check user with valid credentials')
    def test_user_can_login_with_valid_fields(self, login, driver):
        login_page = LoginPage(driver)

        login_page.wait_for_profile_page()


