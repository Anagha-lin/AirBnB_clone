#!/usr/bin/python3
"""Testing Amenity module."""
import unittest
import pep8
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Check Amenity class."""

    def test_pep8(self):
        """Test PEP 8 style."""
        pep8style = pep8.StyleGuide(quiet=True)
        path_amenity = 'models/amenity.py'
        result = pep8style.check_files([path_amenity])
        self.assertEqual(result.total_errors, 0, "Found code style errors.")

    # Add more test methods as needed for other functionalities of the Amenity class
    # Example:
    # def test_amenity_attributes(self):
    #     amenity = Amenity()
    #     self.assertEqual(amenity.name, "")
    #     ...

if __name__ == '__main__':
    unittest.main()

