# test_sfp_stackoverflow.py
import pytest
import unittest

from modules.sfp_stackoverflow import sfp_stackoverflow
from sflib import SpiderFoot


@pytest.mark.usefixtures
class TestModuleStackoverflow(unittest.TestCase):
    """
    Test modules.sfp_stackoverflow
    """

    def test_opts(self):
        module = sfp_stackoverflow()
        self.assertEqual(len(module.opts), len(module.optdescs))

    def test_setup(self):
        """
        Test setup(self, sfc, userOpts=dict())
        """
        sf = SpiderFoot(self.default_options)

        module = sfp_stackoverflow()
        module.setup(sf, dict())

    def test_watchedEvents_should_return_list(self):
        module = sfp_stackoverflow()
        self.assertIsInstance(module.watchedEvents(), list)

    def test_producedEvents_should_return_list(self):
        module = sfp_stackoverflow()
        self.assertIsInstance(module.producedEvents(), list)
