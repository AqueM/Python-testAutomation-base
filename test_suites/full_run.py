import unittest
import HtmlTestRunner


def suite():
    loader = unittest.TestLoader()
    suites = loader.discover("../tests")
    return suites

# TODO: add argparser and parametrize full run to be able to run any list of tests,
#  and use other vars like base URL or browser


if __name__ == '__main__':
    runner = HtmlTestRunner.HTMLTestRunner(output="../reports", open_in_browser=True,
                                           combine_reports=True, add_timestamp=True)
    runner.run(suite())
