#!/usr/bin/python3
""" """
from tests.models_tests.test_base_model import test_basemodel
from models.place import Place


class test_place(test_basemodel):
    """ """
    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)