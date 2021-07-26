import allure
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Find "Add to cart" button for backpack to cart')
    def check_backpack_button_status_is_add_to_cart(self):
        try:
            self.driver.find_element_by_xpath('//button[@id="add-to-cart-sauce-labs-backpack"]')
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), 'Screen shot before quit',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError('Element is not found')


    @allure.step('Add backpack to cart')
    def add_backpack_to_cart(self):
        self.driver.find_element_by_xpath('//button[@id="add-to-cart-sauce-labs-backpack"]').click()

    @allure.step('Find "Remove" button backpack delete from cart')
    def button_change_status(self):
        try:
            self.driver.find_element_by_xpath('//button[@id="remove-sauce-labs-backpack"]')
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), 'Screen shot before quit',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError('Element is not found')

    @allure.step('Cart displayed with 1')
    def check_cart_changed_to_one(self):
        element = self.driver.find_element_by_xpath('//span[@class="shopping_cart_badge"]')
        assert element.text == '1'

    @allure.step('Delete backpack from cart')
    def delete_backpack_from_cart(self):
        self.driver.find_element_by_xpath('//button[@id="remove-sauce-labs-backpack"]').click()

    @allure.step('Find "Add to cart" button for backpack to cart')
    def check_backpack_button_status_is_add_to_cart(self):
        try:
            self.driver.find_element_by_xpath('//button[@id="add-to-cart-sauce-labs-backpack"]')
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), 'Screen shot before quit',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError('Element is not found')