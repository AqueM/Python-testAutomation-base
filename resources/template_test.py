import unittest
from datetime import datetime

from selenium import webdriver


class TestTemplate(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        # TODO: manage webdriver choice with a variable in argparser
        # self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        # NOTE: In addCleanup, the first in, is executed last.
        self.addCleanup(self.driver.quit)
        self.addCleanup(self.screenshot_on_fail)
        self.driver.implicitly_wait(5)
        print("Finished test " + unittest.TestCase.id(self))

    def screenshot_on_fail(self):
        # Take a Screen-shot of the drive homepage, when it Failed.
        # Screenshot solution from https://stackoverflow.com/a/49303484
        for method, error in self._outcome.errors:
            if error:
                now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                filename = now + "_" + "FailScreenshot_" + self.id() + ".png"
                # Remember this makes it mandatory to only have tests and suites in single-tiered filepath
                #  otherwise screenshots won't get saved
                filepath = "../screenshots/" + filename
                self.driver.save_screenshot(filepath)

