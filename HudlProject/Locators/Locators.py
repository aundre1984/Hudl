


class Locators():
    # login/Home Page locators

    # buttons
    homepage_login_button = '/html/body/div[1]/header/div/a[2]'
    email_input = "//input[@id='email']"
    password_input = "//input[@id='password']"
    secondary_login_button = "//button[@id='logIn']"

    # other
    homepage = 'https://www.hudl.com/'
    login_validation = "//span[normalize-space()='Feed']"
    login_2_validation = "//span[normalize-space()='Trending']"
    Invalid_login_validation = 'body > div.super-wrap > form.login-container > div.login-error.fade-in-expand > div > p > a'
