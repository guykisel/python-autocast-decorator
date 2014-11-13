# -*- coding: utf-8 -*-

"""
Based partly on the discussion at:
https://stackoverflow.com/questions/7019283/automatically-type-cast-parameters-in-python
"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import ast

import wrapt


def _str_to_data(string):
    try:
        return ast.literal_eval(str(string).strip())
    except Exception:
        return string


@wrapt.decorator
def autocast(f, instance, args, kwargs):
    args = [_str_to_data(arg) for arg in args]
    kwargs = dict(
        (arg_name, _str_to_data(arg)) for arg_name, arg in kwargs.items())
    result = f(*args, **kwargs)
    return result
