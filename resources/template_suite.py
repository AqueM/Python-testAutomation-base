import unittest
import HtmlTestRunner

from test_cases.test_login import TestLogin


def suite():
    # loader = unittest.TestLoader()
    suite_to_run = unittest.TestSuite()
    # login_suite1 = loader.loadTestsFromTestCase(TestLogin)      # add entire test case class
    login_suite2 = [TestLogin('testLogin'),
                    TestLogin('testInvalidLogin')]      # add specific test cases
    # login_suite3 = loader.discover("../test_cases")  # add entire test folder
    # suite_to_run.addTests(login_suite1)
    suite_to_run.addTests(login_suite2)
    return suite_to_run


if __name__ == '__main__':
    runner = HtmlTestRunner.HTMLTestRunner(output="../reports", open_in_browser=True,
                                           combine_reports=True, add_timestamp=True)
    runner.run(suite())

