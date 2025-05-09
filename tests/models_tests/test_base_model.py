#!/usr/bin/python3
""" """
from tests.models_tests.test_base_model import test_basemodel
from models.base_model import BaseModel


class test_base_model(test_basemodel):
    """ """
    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "BaseModel"
        self.value = BaseModel

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)