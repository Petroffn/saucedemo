import allure
from pages.logout_page import LogoutPage


class TestLogout:
    @allure.title('Check that user can logout')
    def test_user_can_logout(self, login, driver):
        logout_page = LogoutPage(driver)
        logout_page.move_to_menu()
        logout_page.click_logout_button()


