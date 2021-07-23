import allure


class LogoutPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Open menu')
    def move_to_menu(self):
        self.driver.find_element_by_xpath('//button[@id="react-burger-menu-btn"]').click()

    @allure.step('Click on the Logout button')
    def click_logout_button(self):
        self.driver.find_element_by_xpath('//a[@id="logout_sidebar_link"]').click()

    @allure.step('Wait for Login button')
    def wait_for_login_button(self):
        self.driver.find_element_by_xpath('//input[@id="login-button"]').click()
