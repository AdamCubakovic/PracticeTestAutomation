# imports
#rom selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
import time


# page class
class LoginPage:
    # locators
    USERNAME_LOCATOR = (By.ID, "username")
    PASSWORD_LOCATOR = (By.ID, "password")
    SUBMIT_LOCATOR = (By.ID, "submit")
    LOGOUT_LOCATOR = (By.XPATH, "//a[@class='wp-block-button__link has-text-color has-background has-very-dark-gray-background-color']")
    USERNAME_ERROR_LOCATOR = (By.ID, "error")
    PASSWORD_ERROR_LOCATOR = (By.ID, "error")

    # methods
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME_LOCATOR).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_LOCATOR).send_keys(password)

    def click_submit(self):
        self.driver.find_element(*self.SUBMIT_LOCATOR).click()
        time.sleep(2)

    def get_url(self):
        current_url = self.driver.current_url
        return current_url

    def get_logout_button(self):
        logout_button = self.driver.find_element(*self.LOGOUT_LOCATOR).is_displayed()
        return logout_button

    def get_username_error_message(self):
        username_error_message = self.driver.find_element(*self.USERNAME_ERROR_LOCATOR)
        return username_error_message

    def get_password_error_message(self):
        password_error_message = self.driver.find_element(*self.PASSWORD_ERROR_LOCATOR)
        return password_error_message
