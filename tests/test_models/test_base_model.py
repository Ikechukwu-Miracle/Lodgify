import unittest
from datetime import datetime
from time import sleep
from unittest.mock import patch
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test BaseModel class"""

    @patch("models.storage")
    def test_init_no_kwargs(self, mock_storage):
        """Test initialization without kwargs"""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        mock_storage.new.assert_called_once_with(model)

    @patch("models.storage")
    def test_init_wuth_kwargs(self, mock_storage):
        """Test initialization with kwargs"""
        time_fmt = "%Y-%m-%dT%H:%M:%S.%f"
        creation = datetime.now()
        model =  BaseModel(id="123", created_at=creation.isoformat(), updated_at=creation.isoformat())
        self.assertEqual(model.id, "123")
        self.assertEqual(model.created_at, creation)
        self.assertEqual(model.updated_at, creation)
        mock_storage.new.assert_not_called()

    def test_str(self):
        """Test the __str__ method"""
        model = BaseModel()
        model_str = str(model)
        self.assertIn(f"[BaseModel] ({model.id})", model_str)
        self.assertIn(f"'id': '{model.id}", model_str)
        self.assertIn(f"'created_at': {repr(model.created_at)}", model_str)
        self.assertIn(f"'updated_at': {repr(model.updated_at)}", model_str)

    @patch("models.storage")
    def test_save(self, mock_storage):
        """Test the save method"""
        model = BaseModel()
        sleep(0.01)
        old_updated_at = model.updated_at
        model.save()
        self.assertGreater(model.updated_at, old_updated_at)
        mock_storage.save.assert_called_once()

    def tets_to_dict(self):
        """Test the to_dict method"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict["id"], model.id)
        self.assertEqual(model_dict["created_at"], model.created_at.isoformat())
        self.assertEqual(model_dict["__class__"], "BaseModel")


if __name__ == "__main__":
    unittest.main()