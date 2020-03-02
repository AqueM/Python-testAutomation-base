import unittest

from page_objects.login import LoginPage
from page_objects.home import HomePage
from resources.template_test import TestTemplate


class TestLogin(TestTemplate):

    def testLogin(self):
        driver = self.driver
        self.home = HomePage(driver)
        self.login = LoginPage(driver)

        self.login.open_home_and_login(self.user[0], self.user[1], True)
        self.home.assert_text_in_header(self.user[2])

    def testInvalidLogin(self):
        driver = self.driver
        self.login = LoginPage(driver)
        self.home = HomePage(driver)

        self.login.open_home_and_login("invalidlogin@test.com", self.user[1], False)
        self.login.assert_error_text(self.login.error, "Bad credentials. Please login again.")


if __name__ == "__main__":
    unittest.main()
