import allure
from pages.login_page import LoginPage


class TestLogin:
    @allure.title('Check that user can login')
    def test_user_can_login_with_valid_fields(self, login, driver):
        login_page = LoginPage(driver)

        login_page.wait_for_profile_page()


