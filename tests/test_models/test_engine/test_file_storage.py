#!/usr/bin/python3
"""Tests on FileStorage"""
import unittest
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from os import path, stat
from models import storage


class Test_attributes_methods_FileStorage(unittest.TestCase):
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

        self.assertEqual(my_storage.all(), my_objects)

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

    def test_save(self):
        """@FileStorage.save runs?"""
        my_model = BaseModel()
        my_model.save()
        storage.save()
        with open('file.json', mode='r', encoding='utf-8') as my_json:
            a_dict = json.load(my_json)
            self.assertEqual(
                    my_model.to_dict(), a_dict.get(f"BaseModel.{my_model.id}"))

    def test_reload(self):
        """@FileStorage.reload works"""
        my_model = BaseModel()
        key = f"BaseModel.{my_model.id}"
        storage.save()
        self.assertTrue(path.isfile('file.json'))
        storage.reload()
        self.assertTrue(key in storage.all().keys())
        self.assertEqual(my_model.id, storage.all().get(key).id)

if __name__ == "__main__":
    unittest.main()
