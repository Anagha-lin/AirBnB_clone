#!/usr/bin/python3
"""Test cases for BaseModel class."""

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class."""

    def test_base_model_instance(self):
        """Test creating an instance of BaseModel."""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)

    def test_str_method(self):
        """Test __str__ method of BaseModel."""
        my_model = BaseModel()
        self.assertEqual(
            str(my_model),
            "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        )

    def test_save_method(self):
        """Test save method of BaseModel."""
        my_model = BaseModel()
        original_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(original_updated_at, my_model.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method of BaseModel."""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        obj_dict = my_model.to_dict()

        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('id', obj_dict)
        self.assertIn('my_number', obj_dict)
        self.assertIn('name', obj_dict)

