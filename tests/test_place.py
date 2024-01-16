#!/usr/bin/python3
"""Testing Place module."""
import unittest
import pep8
from models.place import Place


class TestPlace(unittest.TestCase):
    """Check Place class."""

    def test_pep8(self):
        """Test PEP 8 style."""
        pep8style = pep8.StyleGuide(quiet=True)
        path_place = 'models/place.py'
        result = pep8style.check_files([path_place])
        self.assertEqual(result.total_errors, 0, "Found code style errors.")

    # Add more test methods as needed for other functionalities of the Place class
    # Example:
    # def test_place_attributes(self):
    #     place = Place()
    #     self.assertEqual(place.city_id, "")
    #     self.assertEqual(place.user_id, "")
    #     ...

if __name__ == '__main__':
    unittest.main()

