from HudlProject.Locators.Locators import Locators


class Homepage():
    # 1. this class creates all the objects on the home page - objects meaning buttons and text fields
    # 2. this class also creates all the actions that will be needed to be performed on all the objects -
    # such as click the button and enter the text within the fields
    def __init__(self, driver):
        self.driver = driver

        self.homepage_login_button = Locators.homepage_login_button
        self.email_input = Locators.email_input
        self.password_input = Locators.password_input
        self.secondary_login_button = Locators.secondary_login_button
        self.login_validation = Locators.login_validation
        self.login_2_validation = Locators.login_2_validation
        self.Invalid_login_validation = Locators.Invalid_login_validation

    def click_homepage_login_button(self):
        self.driver.find_element_by_xpath(self.homepage_login_button).click()

    def click_in_email_input(self):
        self.driver.find_element_by_xpath(self.email_input).click()

    def text_email_input(self, email):
        self.driver.find_element_by_xpath(self.email_input).send_keys(email)

    def click_in_password_input(self):
        self.driver.find_element_by_xpath(self.password_input).click()

    def text_password_input(self, password):
        self.driver.find_element_by_xpath(self.password_input).send_keys(password)

    def click_secondary_login_button(self):
        self.driver.find_element_by_xpath(self.secondary_login_button).click()

    def login_validation(self):
        self.driver.find_element_by_xpath(self.login_validation).text()

    def login_2_validation(self):
        self.driver.find_element_by_xpath(self.login_2_validation).text()

    def Invalid_login_validation(self):
        self.driver.find_element_by_xpath(self.Invalid_login_validation).text()
