import allure
from pages.inventory_page import InventoryPage


class TestGoods:
    @allure.title('Check that user can add to cart')
    def test_user_can_logout(self, login, driver):
        goods_page = InventoryPage(driver)
        goods_page.check_backpack_button_status_is_add_to_cart()
        goods_page.add_backpack_to_cart()
        goods_page.button_change_status()
        goods_page.check_cart_changed_to_one()
        goods_page.delete_backpack_from_cart()
        goods_page.check_backpack_button_status_is_add_to_cart()
