#!/usr/bin/python3
"""Test cases for BaseModel class."""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import os


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class."""

    def setUp(self):
        """Set up for the test."""
        self.my_model = BaseModel()

    def tearDown(self):
        """Clean up after each test."""
        del self.my_model

    def test_instance_creation(self):
        """Test creating an instance of BaseModel."""
        self.assertIsInstance(self.my_model, BaseModel)

    def test_attributes(self):
        """Test attributes of the BaseModel instance."""
        self.assertTrue(hasattr(self.my_model, 'id'))
        self.assertTrue(hasattr(self.my_model, 'created_at'))
        self.assertTrue(hasattr(self.my_model, 'updated_at'))

    def test_save_method(self):
        """Test the save method of BaseModel."""
        original_updated_at = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(original_updated_at, self.my_model.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method of BaseModel."""
        obj_dict = self.my_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('__class__', obj_dict)

    def test_str_method(self):
        """Test the __str__ method of BaseModel."""
        str_representation = str(self.my_model)
        self.assertIsInstance(str_representation, str)
        self.assertIn(self.my_model.id, str_representation)

    def test_created_at_type(self):
        """Test the type of created_at attribute."""
        self.assertIsInstance(self.my_model.created_at, datetime)

    def test_updated_at_type(self):
        """Test the type of updated_at attribute."""
        self.assertIsInstance(self.my_model.updated_at, datetime)

    def test_save_method_with_storage(self):
        """Test the save method with storage."""
        self.my_model.save()
        file_path = "file.json"
        self.assertTrue(os.path.isfile(file_path))
        os.remove(file_path)


if __name__ == "__main__":
    unittest.main()

