#!/usr/bin/env python

from os import path
from setuptools import setup


version = '1.4.0'

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: Other/Proprietary License",
    "Programming Language :: Python",
    "Operating System :: OS Independent",
    "Topic :: Software Development :: Libraries",
    "Topic :: Utilities",
    "Environment :: Web Environment",
    "Framework :: Django",
]


root_dir = path.dirname(path.abspath(__file__))
long_desc = open(root_dir + '/README.rst').read()


setup(
    name='django-redactoreditor',
    version=version,
    url='https://github.com/mazelife/django-redactoreditor',
    author='James Stevenson',
    author_email='james.m.stevenson at gmail dot com',
    license='CC licence, see LICENSE.txt',
    packages=['redactor'],
    package_data={
        'redactor': ["*.css", "*.js"]
    },
    description=(
        'Integrates the Redactor Javascript WYSIWYG editor with Django.'
    ),
    classifiers=classifiers,
    long_description=long_desc,
    install_requires=['django>=1.3.1'],
    include_package_data=True,
    zip_safe=False
)
