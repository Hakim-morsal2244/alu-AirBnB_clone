#!/usr/bin/python3
""" """
from tests.models_tests.test_base_model import test_basemodel
from models.amenity import Amenity


class test_amenity(test_basemodel):
    """ """
    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)