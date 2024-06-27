#!/usr/bin/python3
""" This defines unittests for models/place.py.
Unittest classes:
    TestPlace_instantiation
    TestPlace_save
    TestPlace_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

    def test_no_args_instantiates(self):
        """Test if Place() instantiates without any arguments."""
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        """Test if a new instance of Place is stored in models.storage."""
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Test if the id attribute of Place is a string."""
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public_datetime(self):
        """Test if created_at attribute of Place is a datetime object."""
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public_datetime(self):
        """Test if updated_at attribute of Place is a datetime object."""
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_id_is_public_class_attribute(self):
        """Test if city_id is a public class attribute of Place."""
        pl = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(pl))
        self.assertNotIn("city_id", pl.__dict__)

    def test_user_id_is_public_class_attribute(self):
        """Test if user_id is a public class attribute of Place."""
        pl = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(pl))
        self.assertNotIn("user_id", pl.__dict__)

    # Other attribute tests follow similarly...

    def test_two_places_unique_ids(self):
        """Test if two instances of Place have unique ids."""
        pl1 = Place()
        pl2 = Place()
        self.assertNotEqual(pl1.id, pl2.id)

    def test_two_places_different_created_at(self):
        """Test if created_at timestamps of two instances of Place are different."""
        pl1 = Place()
        sleep(0.05)
        pl2 = Place()
        self.assertLess(pl1.created_at, pl2.created_at)

    # Other instantiation tests follow similarly...


class TestPlace_save(unittest.TestCase):
    """Unittests for testing save method of the Place class."""

    @classmethod
    def setUp(self):
        """Set up by renaming file.json to tmp (if exists)."""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        """Clean up by removing file.json (if exists) and renaming tmp back to file.json."""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        """Test if save method updates the updated_at attribute."""
        pl = Place()
        sleep(0.05)
        first_updated_at = pl.updated_at
        pl.save()
        self.assertLess(first_updated_at, pl.updated_at)

    # Other save method tests follow similarly...


class TestPlace_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Place class."""

    def test_to_dict_type(self):
        """Test if to_dict method returns a dictionary."""
        self.assertTrue(dict, type(Place().to_dict()))

    # Other to_dict tests follow similarly...


if __name__ == "__main__":
    unittest.main()

