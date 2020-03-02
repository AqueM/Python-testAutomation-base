from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage

import resources.environment


class HomePage(BasePage):
    title = "My Store"
    txt_header_name = (By.CLASS_NAME, "account")

    def open_home(self):
        self.driver.get(resources.environment.base_url)
        # wait for some element that signifies page is done loading
        self.wait_for_title(self.title)

    def click_to_home(self, link):
        # """Selenium doesn't wait for page to load after clicking, so needed a wrapper,
        # and homepage doesn't have a specific URL"""
        link.click()
        self.wait_for_title(self.title)

    def assert_text_in_header(self, text):
        self.wait_for_element(self.txt_header_name)
        greet = self.driver.find_element(*self.txt_header_name).text
        assert text in greet, \
            "Expected greeting text to include '" + text + "' but it was '" + greet + "'."
