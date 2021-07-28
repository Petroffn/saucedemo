from selenium.webdriver.common.by import By


class LoginLocators:
    user_name_field = (By.ID, "user-name")
    user_password_field = (By.ID, "password")
    login_button = (By.ID, "login-button")
