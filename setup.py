#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='Google Plus blog',
    version='0.1',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask',
                      'Flask-Script',
                      'markdown2'],

    entry_points = {'console_scripts': ['blog=gplusblog:main']},
)
