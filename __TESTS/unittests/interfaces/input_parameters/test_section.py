# coding: utf8
# Copyright 2014-2020 CERN. This software is distributed under the
# terms of the GNU General Public Licence version 3 (GPL Version 3),
# copied verbatim in the file LICENCE.md.
# In applying this licence, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization or
# submit itself to any jurisdiction.
# Project website: http://blond.web.cern.ch/

"""
Unit-test for blond_common.interfaces.input_parameters.ring_section.py
:Authors: **Alexandre Lasheen**
"""

# General imports
# ---------------
import sys
import unittest
import numpy as np
import os

this_directory = os.path.dirname(os.path.realpath(__file__)) + "/"

# BLonD_Common imports
# --------------------
if os.path.abspath(this_directory + '../../../../../') not in sys.path:
    sys.path.insert(0, os.path.abspath(this_directory + '../../../../../'))

from blond_common.interfaces.input_parameters.ring_section import Section


class TestSection(unittest.TestCase):

    # Initialization ----------------------------------------------------------

    def setUp(self):

        pass

    def assertIsNaN(self, value, msg=None):
        """
        Fail if provided value is not NaN
        """

        standardMsg = "%s is not NaN" % str(value)

        if not np.isnan(value):
            self.fail(self._formatMessage(msg, standardMsg))

    # Input test --------------------------------------------------------------

    def test_simple_input(self):
        # Test if 'ring length size' RuntimeError gets thrown for wrong number
        # of rf sections
        num_sections = 1    # only one rf-section!
        
        section_length = 300
        alpha_0 = 1e-3
        momentum = 26e9

        section = Section(section_length, alpha_0, momentum)

        with self.subTest('Simple input - section_length'):    
                np.testing.assert_equal(
                    section_length, section.section_length)

        with self.subTest('Simple input - momentum'):    
                np.testing.assert_equal(
                    momentum, section.synchronous_data)

        with self.subTest('Simple input - alpha_0'):    
                np.testing.assert_equal(
                    alpha_0, section.alpha_0)

if __name__ == '__main__':

    unittest.main()