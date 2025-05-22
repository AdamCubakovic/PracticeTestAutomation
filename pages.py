# imports
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import data
from data import USERNAME, PASSWORD


# page class
class LoginPage:
    # locators
    USERNAME_LOCATOR = (By.ID, "username")
    PASSWORD_LOCATOR = (By.ID, "password")
    SUBMIT_LOCATOR = (By.ID, "submit")

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


