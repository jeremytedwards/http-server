# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='http-server',
    description='HTTP Server assignment',
    version=0.1,
    author='Paul Sheirdan and Jeremy Edwards',
    author_email='paul.sheridan@me.com and jeremytedwards@gmail.com',
    license='MIT',
    py_modules=['client'],
    package_dir={'': 'src'},
    extras_require={'test': ['pytest', 'pytest-xdist', 'tox']},
)
