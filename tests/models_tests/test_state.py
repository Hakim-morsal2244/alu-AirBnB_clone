#!/usr/bin/python3
""" """
from tests.models_tests.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ """
    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)