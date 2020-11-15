#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class MyDict(dict):

    # This class has the same behaviour to dict,
    # but we can use attribute format to access the value
    # e.g. my_dict_1 = MyDict(a=1, b=2)
    # my_dict_1[a] is 1
    # my_dict_1.a is also 1

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'MyDict' object does not have the attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

# we then use a unit test class to conduct unit test
# the unit test module is my_dict_test.py