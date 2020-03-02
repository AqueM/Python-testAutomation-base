from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class HomePage(BasePage):
    home_url = "http://automationpractice.com"
    home_title = "Homepage"
    greeting = (By.CLASS_NAME, "cx-login-greet")
    login = "menover30@test.com"
    password = "12341234"

    def open_home(self):
        self.driver.get(self.home_url)
        # wait for some element that signifies page is done loading
        self.wait_for_title(self.home_title)

    def click_to_home(self, link):
        # """Selenium doesn't wait for page to load after clicking, so needed a wrapper,
        # and homepage doesn't have a specific URL"""
        link.click()
        self.wait_for_title(self.home_title)

    def assert_text_in_greeting(self, text):
        self.wait_for_element(self.greeting)
        greet = self.driver.find_element(*self.greeting).text
        assert text in greet, \
            "Expected greeting text to include '" + text + "' but it was '" + greet + "'."
