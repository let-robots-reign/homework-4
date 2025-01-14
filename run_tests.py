import unittest
import sys

from tests.feed import FeedTestSuite
from tests.login import LoginTestSuite
from tests.main_page import MainPageTestSuite
from tests.movie import MovieTestSuite
from tests.profile import ProfileTestSuite
from tests.settings import SettingsTestSuite
from tests.signup import SignupTestSuite


def main():
    suite = unittest.TestSuite((
        unittest.makeSuite(LoginTestSuite),
        unittest.makeSuite(SignupTestSuite),
        unittest.makeSuite(ProfileTestSuite),
        unittest.makeSuite(FeedTestSuite),
        unittest.makeSuite(SettingsTestSuite),
        unittest.makeSuite(MainPageTestSuite),
        unittest.makeSuite(MovieTestSuite)
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())


if __name__ == '__main__':
    main()
