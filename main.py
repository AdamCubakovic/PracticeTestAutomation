#imports
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pages import LoginPage
import time
import data

from data import LOGIN_URL, USERNAME, PASSWORD


#test class
class TestLoginPage:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    #test case 1
    def test_login(self):
        self.driver.get(LOGIN_URL)
        login_page = LoginPage(self.driver)
        username = USERNAME
        password = PASSWORD

        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_submit()
        time.sleep(2)

# Verify new page URL contains "practicetestautomation.com/logged-in-successfully/"

        new_url = "practicetestautomation.com/logged-in-successfully/"
        assert new_url in self.driver.current_url, "Page address is invalid!"

# Verify new page contains expected text ('Congratulations' or 'successfully logged in')

        page_source = self.driver.page_source
        strings_to_check = ["Congratulations", "successfully logged in"]
        for string in strings_to_check:
            assert string in page_source , "Page does not contain correct messages."

#Verify button Log out is displayed on the new page

        assert login_page.get_logout_button(), "Logout button not displayed."



    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
    #teardown class (cls)