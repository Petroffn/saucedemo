import allure

from pages.sort_page import SortPage


class TestSort:
    @allure.title('Check that user can logout')
    def test_sort(self, login, driver):
        sort_page = SortPage(driver)
        sort_page.click_sort_button()
        sort_page.click_sort_button_z_to_a()

        sort_page.click_sort_button()
        sort_page.click_sort_button_a_to_z()

        sort_page.click_sort_button()
        sort_page.click_sort_button_low_to_high()

        sort_page.click_sort_button()
        sort_page.click_sort_button_high_to_low()
