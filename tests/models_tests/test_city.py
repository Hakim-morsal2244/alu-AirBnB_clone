#!/usr/bin/python3
""" """
from tests.models_tests.test_base_model import test_basemodel
from models.city import City


class test_city(test_basemodel):
    """ """
    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)