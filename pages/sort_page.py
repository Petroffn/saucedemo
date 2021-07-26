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
