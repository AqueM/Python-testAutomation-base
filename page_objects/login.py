from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from page_objects.home import HomePage
from page_objects.my_account_menu import MyAccountMenu


class LoginPage(BasePage):
    login_input = (By.XPATH, "//input[@type='email']")
    pass_input = (By.XPATH, "//input[@type='password']")
    login_button = (By.XPATH, "//button[@type='submit']")
    login_link = (By.XPATH, "//a[contains(@href,'login')]")
    login_title = "Login"
    error = (By.CLASS_NAME, "alert-danger")

    def __init__(self, driver):
        self.driver = driver
        self.home = HomePage(driver)
        self.account = MyAccountMenu(driver)
        super().__init__(driver)

    def input_login(self, login):
        email_input = self.driver.find_element(*self.login_input)
        email_input.send_keys(login)

    def input_password(self, password):
        pw_input = self.driver.find_element(*self.pass_input)
        pw_input.send_keys(password)

    def click_login(self):
        button = self.driver.find_element(*self.login_button)
        button.click()

    # noinspection PyIncorrectDocstring
    def login_as(self, login, password, valid_login):
        """

        :param valid_login: define if user should proceed to homepage or expect an error
        :rtype valid_login: Bool

        """
        link = self.driver.find_element(*self.login_link)
        link.click()
        self.home.wait_for_title(self.login_title)
        self.input_login(login)
        self.input_password(password)
        self.click_login()
        if valid_login:
            self.wait_for_title("Homepage")

    def open_home_and_login(self, login, password, valid_login):
        self.home.open_home()
        self.login_as(login, password, valid_login)

    def assert_error_text(self, text):
        self.wait_for_element(self.error)
        error_displayed = self.driver.find_element(*self.error).text
        assert text in error_displayed,\
            "Expected error message to include '" + text + "' but it was '" + error_displayed + "'."
