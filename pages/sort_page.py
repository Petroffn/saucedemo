import time

import allure


class SortPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Open sort dropdown')
    def click_sort_button(self):
        self.driver.find_element_by_xpath('//select[@data-test="product_sort_container"]').click()

    @allure.step('Select sort Z to A')
    def click_sort_button_z_to_a(self):
        self.driver.find_element_by_xpath(
            '//select[@class="product_sort_container"]/option[text()="Name (Z to A)"]').click()
        names = []

        for name in self.driver.find_elements_by_class_name('inventory_item_name'):
            names.append(name.text)
        reverse = sorted(names, reverse=True)
        assert names == reverse

    @allure.step('Open sort dropdown')
    def click_sort_button(self):
        self.driver.find_element_by_xpath('//select[@data-test="product_sort_container"]').click()

    @allure.step('Select sort A to Z')
    def click_sort_button_a_to_z(self):
        self.driver.find_element_by_xpath(
            '//select[@class="product_sort_container"]/option[text()="Name (A to Z)"]').click()

        names = []

        for name in self.driver.find_elements_by_class_name('inventory_item_name'):
            names.append(name.text)
        sorts = sorted(names)
        assert names == sorts

    @allure.step('Select sort Price (low to high)')
    def click_sort_button_low_to_high(self):
        self.driver.find_element_by_xpath(
            '//select[@class="product_sort_container"]/option[text()="Price (low to high)"]').click()
        prices = []
        i = 0
        time.sleep(3)
        for item in self.driver.find_elements_by_class_name('inventory_item_price'):
            number = float(item.text[1:])
            prices.append(number)
        while i < len(prices) - 1:
            assert prices[i] <= prices[i + 1]
            i += 1

    @allure.step('Select sort Price (low to high)')
    def click_sort_button_high_to_low(self):
        self.driver.find_element_by_xpath(
            '//select[@class="product_sort_container"]/option[text()="Price (high to low)"]').click()
        prices = []
        i = 0
        time.sleep(3)
        for item in self.driver.find_elements_by_class_name('inventory_item_price'):
            number = float(item.text[1:])
            prices.append(number)
        while i < len(prices) - 1:
            assert prices[i] >= prices[i + 1]
            i += 1
