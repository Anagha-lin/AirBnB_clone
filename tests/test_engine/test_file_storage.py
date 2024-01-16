#!/usr/bin/python3
"""Test for FileStorage module."""
import unittest
import json
import os
from models.base_model import BaseModel
from models.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test FileStorage class."""

    def setUp(self):
        """Set up the test environment."""
        # Create a temporary file for testing
        self.temp_file_path = "temp_file.json"
        FileStorage._FileStorage__file_path = self.temp_file_path
        self.storage = FileStorage()

    def tearDown(self):
        """Tear down the test environment."""
        # Remove the temporary file after testing
        if os.path.exists(self.temp_file_path):
            os.remove(self.temp_file_path)

    def test_all(self):
        """Test the all() method."""
        # Initially, __objects should be an empty dictionary
        self.assertEqual(self.storage.all(), {})

        # Add a BaseModel instance and check if it's present in __objects
        obj = BaseModel()
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.storage.new(obj)
        self.assertEqual(self.storage.all(), {key: obj})

    def test_new(self):
        """Test the new() method."""
        # Add a BaseModel instance and check if it's present in __objects
        obj = BaseModel()
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.storage.new(obj)
        self.assertEqual(self.storage.all(), {key: obj})

    def test_save_reload(self):
        """Test the save() and reload() methods."""
        # Add a BaseModel instance, save, reload, and check if still present
        obj = BaseModel()
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        self.assertEqual(self.storage.all(), {key: obj})

    def test_save_file_contents(self):
        """Test if the saved file contents are correct."""
        # Add a BaseModel instance, save, and check if file contents are correct
        obj = BaseModel()
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.storage.new(obj)
        self.storage.save()

        with open(self.temp_file_path, 'r', encoding='utf-8') as file:
            file_contents = json.load(file)

        expected_contents = {key: obj.to_dict()}
        self.assertEqual(file_contents, expected_contents)


if __name__ == '__main__':
    unittest.main()

