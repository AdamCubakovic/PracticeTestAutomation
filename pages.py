# imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import data
from data import USERNAME, PASSWORD


# page class
class LoginPage:
    # locators
    USERNAME_LOCATOR = (By.ID, "username")
    PASSWORD_LOCATOR = (By.ID, "password")
    SUBMIT_LOCATOR = (By.ID, "submit")
    LOGOUT_LOCATOR = (By.XPATH, "//a[@class='wp-block-button__link has-text-color has-background has-very-dark-gray-background-color']")

    # methods
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        username = USERNAME
        self.driver.find_element(*self.USERNAME_LOCATOR).send_keys(username)

    def enter_password(self, password):
        password = PASSWORD
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

