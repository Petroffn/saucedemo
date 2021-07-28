import allure
from selenium.common.exceptions import NoSuchElementException
from locators.login_locators import LoginLocators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Open https://www.saucedemo.com/ Page')
    def open_login_page(self):
        self.driver.get('https://www.saucedemo.com/')

    @allure.step('Input User Name')
    def input_username(self, username):
        self.driver.find_element(*LoginLocators.user_name_field).send_keys(username)

    @allure.step('Input Password')
    def input_password(self, password):
        self.driver.find_element(*LoginLocators.user_password_field).send_keys(password)

    @allure.step('Click on the Login button')
    def click_login_button(self):
        self.driver.find_element(*LoginLocators.button_login).click()

    @allure.step('Wait for User name text')
    def wait_for_profile_page(self):
        try:
            self.driver.find_element_by_xpath('//a[@class="shopping_cart_link"]')
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), 'Screen shot before quit',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError('Log Out button is not found')

