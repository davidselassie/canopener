# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from setuptools import setup


setup(
    name='canopener',
    version='0.1.2',
    author='David Selassie',
    author_email='selassid@gmail.com',
    package='canopener',
    url='https://github.com/selassid/canopener',
    license='LICENSE.txt',
    description=(
        'Python convenience function for opening compressed URLs and files.'
    ),
    long_description=open('README.rst').read(),
    setup_requires=['setuptools'],
    install_requires=[
        'boto',
        'pystaticconfiguration',
    ],
)
