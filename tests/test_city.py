#!/usr/bin/python3
"""Testing City module."""
import unittest
import pep8
from models.city import City


class TestCity(unittest.TestCase):
    """Check City class."""

    def test_pep8(self):
        """Test PEP 8 style."""
        pep8style = pep8.StyleGuide(quiet=True)
        path_city = 'models/city.py'
        result = pep8style.check_files([path_city])
        self.assertEqual(result.total_errors, 0, "Found code style errors.")

    # Add more test methods as needed for other functionalities of the City class
    # Example:
    # def test_city_attributes(self):
    #     city = City()
    #     self.assertEqual(city.name, "")
    #     ...

if __name__ == '__main__':
    unittest.main()

