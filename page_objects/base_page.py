from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import *


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def wait_for_title(self, title):
        WebDriverWait(self.driver, 10).until(ec.title_contains(title))

    def click_to_new_page(self, link, new_url):
        # Selenium doesn't wait for page to load after clicking, so needed a wrapper
        link.click()
        WebDriverWait(self.driver, 10).until(ec.url_contains(new_url))

    def wait_for_element(self, element_by):
        WebDriverWait(self.driver, 10).until(ec.presence_of_all_elements_located(element_by))

    def scroll_element_into_view(self, element_by):
        # hack for scrolling as the built-in function doesn't always work
        element = self.driver.find_element(*element_by)
        self.driver.execute_script("arguments[0].scrollIntoView()", element)

    def check_if_element_exists(self, element_by):
        try:
            self.driver.find_element(*element_by)
        except NoSuchElementException:
            return False
        return True

    def got_to_new_page(self, url, title):
        # wrapper in case page has some delay between page load and frontend appearance
        self.driver.get(url)
        self.wait_for_title(title)

    def wait_for_element_disappear(self, element_by):
        WebDriverWait(self.driver, 10).until_not(ec.presence_of_all_elements_located(element_by))