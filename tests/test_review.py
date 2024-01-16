#!/usr/bin/python3
"""Testing Review module."""
import unittest
import pep8
from models.review import Review


class TestReview(unittest.TestCase):
    """Check Review class."""

    def test_pep8(self):
        """Test PEP 8 style."""
        pep8style = pep8.StyleGuide(quiet=True)
        path_review = 'models/review.py'
        result = pep8style.check_files([path_review])
        self.assertEqual(result.total_errors, 0, "Found code style errors.")

    # Add more test methods as needed for other functionalities of the Review class
    # Example:
    # def test_review_attributes(self):
    #     review = Review()
    #     self.assertEqual(review.place_id, "")
    #     self.assertEqual(review.user_id, "")
    #     ...

if __name__ == '__main__':
    unittest.main()

