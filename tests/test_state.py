#!/usr/bin/python3
"""Testing State module."""
import unittest
import pep8
from models.state import State


class TestState(unittest.TestCase):
    """Check State class."""

    def test_pep8(self):
        """Test PEP 8 style."""
        pep8style = pep8.StyleGuide(quiet=True)
        path_state = 'models/state.py'
        result = pep8style.check_files([path_state])
        self.assertEqual(result.total_errors, 0, "Found code style errors.")

    # Add more test methods as needed for other functionalities of the State class
    # Example:
    # def test_state_attributes(self):
    #     state = State()
    #     self.assertEqual(state.name, "")
    #     ...

if __name__ == '__main__':
    unittest.main()

