#imports
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pages import LoginPage
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

        new_url = "practicetestautomation.com/logged-in-successfully/"
        get_url = self.driver.current_url
        assert new_url in get_url
        # need to Verify new page contains
        # expected text ('Congratulations' or 'successfully logged in')
        # need to Verify button Log out is displayed on the new page


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
    #teardown class (cls)