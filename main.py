from selenium import webdriver
from pages import LoginPage
import time
from data import LOGIN_URL, USERNAME_VALID, PASSWORD_VALID, USERNAME_INVALID, PASSWORD_INVALID

#test class
class TestLoginPage:

    #setup class
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    #test case 1 - valid username and password
    def test_login_positive(self):
        self.driver.get(LOGIN_URL)
        login_page = LoginPage(self.driver)
        username_valid = USERNAME_VALID
        password_valid = PASSWORD_VALID

        # enter username and password. Click submit
        login_page.enter_username(username_valid)
        login_page.enter_password(password_valid)
        login_page.click_submit()
        time.sleep(2)

        # Verify new page URL
        new_url = "practicetestautomation.com/logged-in-successfully/"
        assert new_url in self.driver.current_url, "Page address is invalid!"

        # Verify expected text
        page_source = self.driver.page_source
        strings_to_check = ["Congratulations", "successfully logged in"]
        for string in strings_to_check:
            assert string in page_source , "Page does not contain correct messages."

        #Verify Log Out button is displayed on the new page
        assert login_page.get_logout_button(), "Logout button not displayed."

    # test case 2 - invalid username, valid password
    def test_invalid_username(self):
        self.driver.get(LOGIN_URL)
        login_page = LoginPage(self.driver)
        username_invalid = USERNAME_INVALID
        password_valid = PASSWORD_VALID

        # enter username and password. Click submit
        login_page.enter_username(username_invalid)
        login_page.enter_password(password_valid)
        login_page.click_submit()
        time.sleep(2)

        assert login_page.get_username_error_message(), "Username error message is not displayed."

    # test case 3 - valid username, invalid password
    def test_invalid_password(self):
        self.driver.get(LOGIN_URL)
        login_page = LoginPage(self.driver)
        username_valid = USERNAME_VALID
        password_invalid = PASSWORD_INVALID

        # enter username and password. Click submit
        login_page.enter_username(username_valid)
        login_page.enter_password(password_invalid)
        login_page.click_submit()
        time.sleep(2)

        assert login_page.get_password_error_message(), "Password error message is not displayed."

    # teardown class
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
