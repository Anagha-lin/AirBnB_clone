#!/usr/bin/python3
"""Testing User module."""
import unittest
import pep8
from models.user import User


class TestUser(unittest.TestCase):
    """Check User class."""

    def test_pep8(self):
        """Test PEP 8 style."""
        pep8style = pep8.StyleGuide(quiet=True)
        path_user = 'models/user.py'
        result = pep8style.check_files([path_user])
        self.assertEqual(result.total_errors, 0, "Found code style errors.")

    # Add more test methods as needed for other functionalities of the User class
    # Example:
    # def test_user_attributes(self):
    #     user = User()
    #     self.assertEqual(user.email, "")
    #     self.assertEqual(user.password, "")
    #     ...

if __name__ == '__main__':
    unittest.main()

