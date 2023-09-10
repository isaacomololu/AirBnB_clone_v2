#!/usr/bin/python3
"""Defines unnittests for models/state.py."""
import unittest
import os
from os import getenv
from models.state import State
from models.base_model import BaseModel
from models.engine.db_storage import DBStorage
import pep8


class TestState(unittest.TestCase):
    """Unittests for testing the State class."""

    @classmethod
    def setUpClass(cls):
        """State testing setup."""
        cls.state = State()
        cls.state.name = "CA"

    @classmethod
    def teardown(cls):
        """State testing teardown."""
        del cls.state

    def tearDown(self):
        """Test methods teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_Review(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/state.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_State(self):
        """Check for docstrings"""
        self.assertIsNotNone(State.__doc__)

    def test_attributes_State(self):
        """Check if State have attributes"""
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)
        self.assertTrue('name' in self.state.__dict__)

    def test_is_subclass_State(self):
        """Test if State is subclass of BaseModel"""
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_attribute_types_State(self):
        """Test attribute type for State"""
        self.assertEqual(type(self.state.name), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db', 'DB')
    def test_save_State(self):
        """Test save method."""
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_to_dict_State(self):
        """Test to_dict method."""
        self.assertEqual('to_dict' in dir(self.state), True)


if __name__ == "__main__":
    unittest.main()
