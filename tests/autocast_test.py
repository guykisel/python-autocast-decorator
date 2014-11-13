#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from autocast import autocast


@autocast
def return_a_type(input):
    return type(input)


def string_to_int_test():
    assert return_a_type('5') == int
    assert return_a_type('12345') == int


def string_to_float_test():
    assert return_a_type('3.5') == float
    assert return_a_type('1.0') == float


def string_to_string_test():
    assert return_a_type('hello world') == unicode
    assert return_a_type('Hello world!') == unicode
    assert return_a_type('Hello') == unicode
    assert return_a_type('Hello 12345') == unicode
    assert return_a_type(b'hello world') == str
    assert return_a_type(b'Hello world!') == str
    assert return_a_type(b'Hello') == str
    assert return_a_type(b'Hello 12345') == str
    assert return_a_type(r'Hello 12345') == unicode


def string_to_boolean_test():
    assert return_a_type('True') == bool
    assert return_a_type('False') == bool


def string_to_list_test():
    assert return_a_type('[1, 2, "3", 4.5]') == list
    assert return_a_type('[]') == list


def string_to_dict_test():
    assert return_a_type('{1: 2, "3": 4.5}') == dict
    assert return_a_type('{}') == dict


def string_to_tuple_test():
    assert return_a_type('(1, 2, 3, 4)') == tuple
