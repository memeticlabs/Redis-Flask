# -*- coding: utf-8 -*-

"""
Redis-Flask
-----------
Redis-Flask provides redis support for a Flask application. It gives the
ability to configure the connection to the Redis database based on some
flask configuration variables.

"""


from setuptools import setup
from distutils.core import setup

setup(
    name = 'Redis-Flask',
    version = '0.1',
    description = 'Redis support for Flask.',
    author = 'Rishabh Verma',
    author_email = 'me@rishabhverma.me',
    long_description = __doc__,
    py_modules = ['flask_redis'],
    zip_safe = False,
    platforms = 'any',
    install_requires=[
        'Flask',
        'redis'
    ]
)
