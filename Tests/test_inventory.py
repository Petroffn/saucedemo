import allure
from pages.inventory_page import InventoryPage


class TestGoods:
    @allure.title('Check that user can add to cart')
    def test_user_can_logout(self, login, driver):
        inventory_page = InventoryPage(driver)
        inventory_page.check_backpack_button_status_is_add_to_cart()
        inventory_page.add_backpack_to_cart()
        inventory_page.button_change_status()
        inventory_page.check_cart_changed_to_one()
        inventory_page.delete_backpack_from_cart()
        inventory_page.check_backpack_button_status_is_add_to_cart()


