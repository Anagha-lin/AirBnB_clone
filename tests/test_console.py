import unittest
from unittest.mock import patch
from io import StringIO
import sys
from your_alternative_module_name import HBNBCommand

class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.hbnb_command = HBNBCommand()

    def test_create(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_command.onecmd('create BaseModel')
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output.isalnum())  # Check if the output is alphanumeric (ID)

    def test_show(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_command.onecmd('create BaseModel')
            output_create = mock_stdout.getvalue().strip()
            object_id = output_create.split()[-1]

            with patch('sys.stdout', new_callable=StringIO) as mock_stdout_show:
                self.hbnb_command.onecmd(f'show BaseModel {object_id}')
                output_show = mock_stdout_show.getvalue().strip()

            self.assertIn(object_id, output_show)  # Check if the object ID is present in the output

    def test_destroy(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_command.onecmd('create BaseModel')
            output_create = mock_stdout.getvalue().strip()
            object_id = output_create.split()[-1]

            with patch('sys.stdout', new_callable=StringIO) as mock_stdout_destroy:
                self.hbnb_command.onecmd(f'destroy BaseModel {object_id}')
                output_destroy = mock_stdout_destroy.getvalue().strip()

            self.assertFalse(storage.all())  # Check if the storage is empty after destroy

    # Add more tests for other commands as needed

if __name__ == '__main__':
    unittest.main()

