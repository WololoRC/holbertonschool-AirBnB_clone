#!/usr/bin/python3
"""Tests on FileStorage"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from os import path


class Test_attributes_methods_FileStroage(unittest.TestCase):
    """Lets rock"""
    def test___file_path(self):
        """__file_path exists?"""
        my_storage = FileStorage()
        my_storage.save()
        self.assertTrue(path.exists('file.json'))

    def test___objects(self):
        """__objects exists?"""
        my_storage = FileStorage()
        my_objects = my_storage.all()
        print(my_objects)

        self.assertEqual({}, my_objects)

    def test_all(self):
        """@FileStorage.all runs?"""
        my_storage = FileStorage()

        self.assertTrue(type(my_storage.all()) == dict)

    def test_new(self):
        """@FileStorage.new runs?"""
        my_storage = FileStorage()
        my_objs = my_storage.all().copy()
        my_model = BaseModel()
        my_storage.new(my_model)

        self.assertTrue(my_objs != my_storage.all())


if __name__ == "__main__":
    unittest.main()