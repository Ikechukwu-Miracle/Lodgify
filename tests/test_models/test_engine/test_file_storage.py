import unittest
import json
from unittest.mock import patch, mock_open
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class."""

    @patch('models.engine.file_storage.FileStorage._FileStorage__objects', new={})
    def test_all(self):
        """Test the all method."""
        storage = FileStorage()
        self.assertEqual(storage.all(), {})

    @patch('models.engine.file_storage.FileStorage._FileStorage__objects', new={})
    def test_new(self):
        """Test the new method."""
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, storage.all())
        self.assertEqual(storage.all()[key], obj)

    @patch('models.engine.file_storage.FileStorage._FileStorage__objects', new={})
    def test_save(self):
        """Test the save method."""
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        expected_content = json.dumps({key: obj.to_dict()})

        with patch("builtins.open", mock_open()) as mocked_file:
            storage.save()
            mocked_file.assert_called_once_with("file.json", "w")
            handle = mocked_file()
            written_content = ''.join(call.args[0] for call in handle.write.mock_calls)
            self.assertEqual(written_content, expected_content)

    @patch('models.engine.file_storage.FileStorage._FileStorage__objects', new={})
    @patch("builtins.open", new_callable=mock_open, read_data='{}')
    def test_reload(self, mocked_file):
        """Test the reload method."""
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        obj_dict = {key: obj.to_dict()}

        mocked_file.return_value.read.return_value = json.dumps(obj_dict)

        storage.reload()
        mocked_file.assert_called_once_with("file.json")
        self.assertIn(key, storage.all())
        self.assertEqual(storage.all()[key].id, obj.id)


if __name__ == "__main__":
    unittest.main()