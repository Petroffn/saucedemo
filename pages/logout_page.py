import allure
from locators.logout_locators import LogoutLocators
from locators.login_locators import LoginLocators

class LogoutPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Open menu')
    def move_to_menu(self):
        self.driver.find_element(*LogoutLocators.button_menu).click()

    @allure.step('Click on the Logout button')
    def click_logout_button(self):
        self.driver.find_element(*LogoutLocators.button_logout).click()

    @allure.step('Wait for Login button')
    def wait_for_login_button(self):
        self.driver.find_element(*LoginLocators.button_login).click()
