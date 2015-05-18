#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

short_description = 'Decorator for automatically casting string inputs to ' \
                    'their most likely Python data types.'
try:
    description = open('README.rst').read()
except IOError:
    description = short_description

try:
    license = open('LICENSE').read()
except IOError:
    license = 'MIT License'

classifiers = """
Development Status :: 3 - Alpha
License :: OSI Approved :: MIT License
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3.3
Programming Language :: Python :: 3.4
""".strip().splitlines()

tests_require = ['nose']

setup(
    name='autocast',
    packages=['autocast'],  # this must be the same as the name above
    version='0.0.1dev0',
    description=short_description,
    author='Guy Kisel',
    author_email='guy.kisel@gmail.com',
    url='https://github.com/guykisel/python-autocast-decorator',
    download_url='https://pypi.python.org/pypi/python-autocast-decorator',
    keywords=('decorator autocast'),  # arbitrary keywords
    install_requires=['wrapt'],
    tests_require=tests_require,
    extras_require={'test': tests_require},
    long_description=description,
    license='MIT',
    classifiers=classifiers,
    platforms='any'
)
