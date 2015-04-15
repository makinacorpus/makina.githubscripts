import unittest2 as unittest

from makina.githubscripts.testing import (
    MAKINA_GITHUBSCRIPTS_FIXTURE as UNIT_TESTING,
    MAKINA_GITHUBSCRIPTS_INTEGRATION_TESTING as INTEGRATION_TESTING,
    MAKINA_GITHUBSCRIPTS_FUNCTIONAL_TESTING as FUNCTIONAL_TESTING,
)


class TestCase(unittest.TestCase):
    """We use this base class for all the tests in this package.
    If necessary, we can put common utility or setup code in here.
    """
    layer = UNIT_TESTING

    def setUp(self):
        super(TestCase, self).setUp()


class IntegrationTestCase(TestCase):
    """Integration base TestCase."""
    layer = INTEGRATION_TESTING


class FunctionalTestCase(TestCase):
    """Functionnal base TestCase."""
    layer = FUNCTIONAL_TESTING

# vim:set ft=python:
