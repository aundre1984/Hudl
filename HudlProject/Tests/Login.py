import unittest

from selenium import webdriver
from time import sleep
from HudlProject.Homepage.Homepage import Homepage
from HudlProject.Credentials.Credentials import Credentials
from HudlProject.Credentials.InvalidCredentials import InvalidCredentials


class Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('/users/admin/desktop/chromedriver')
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    # valid email - valid password login
    def test_login_valid(self):
        driver = self.driver
        driver.get('https://www.hudl.com')

        login = Homepage(driver)
        assert 'Hudl: We Help Teams and Athletes Win' in driver.title  # validating user is on homepage
        sleep(1)
        login.click_homepage_login_button()
        login.click_in_email_input()
        sleep(1)
        login.text_email_input(Credentials.email)
        sleep(1)
        login.text_password_input(Credentials.password)
        sleep(1)
        login.click_secondary_login_button()
        assert 'Feed' in login.login_validation  # validating text once user is logged in
        sleep(1)
        assert 'Trending' in login.login_2_validation  # validating text once user is logged in

    # valid email - invalid password login
    def test_login_invalid(self):
        driver = self.driver
        driver.get('https://www.hudl.com')

        login = Homepage(driver)
        assert 'Hudl: We Help Teams and Athletes Win' in driver.title  # validating user is on homepage
        sleep(1)
        login.click_homepage_login_button()
        login.click_in_email_input()
        sleep(1)
        login.text_email_input(InvalidCredentials.email)
        sleep(1)
        login.text_password_input(InvalidCredentials.password)
        sleep(1)
        login.click_secondary_login_button()
        sleep(1)
        assert 'login-error' in login.Invalid_login_validation #validating login error

    @classmethod
    def test_teardown(cls):
        cls.driver.quit()
