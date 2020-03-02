from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from page_objects.home import HomePage


class LoginPage(BasePage):
    input_email = (By.XPATH, "//input[@id='email']")
    input_pass = (By.XPATH, "//input[@type='password']")
    btn_login = (By.XPATH, "//button[@id='SubmitLogin']")
    link_login_page = (By.XPATH, "//a[contains(@class,'login')]")
    title = "Login - My Store"
    error = (By.CLASS_NAME, "alert-danger")

    def __init__(self, driver):
        self.driver = driver
        self.home = HomePage(driver)
        super().__init__(driver)

    def input_login(self, login):
        email_input = self.driver.find_element(*self.input_email)
        email_input.send_keys(login)

    def input_password(self, password):
        pw_input = self.driver.find_element(*self.input_pass)
        pw_input.send_keys(password)

    def click_login(self):
        button = self.driver.find_element(*self.btn_login)
        button.click()

    # noinspection PyIncorrectDocstring
    def login_as(self, login, password, valid_login):
        """

        :param valid_login: define if user should proceed to homepage or expect an error
        :rtype valid_login: Bool

        """
        link = self.driver.find_element(*self.link_login_page)
        link.click()
        self.home.wait_for_title(self.title)
        self.input_login(login)
        self.input_password(password)
        self.click_login()
        if valid_login:
            self.wait_for_title("My account - My store")
            # above must be used to pass in the state as is, because page object for My Account page doesn't exist
            # self.wait_for_title(account.title)

    def open_home_and_login(self, login, password, valid_login):
        self.home.open_home()
        self.login_as(login, password, valid_login)

