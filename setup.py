# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from pkg_resources import resource_string
from setuptools import find_packages
from setuptools import setup


setup(
    name='canopener',
    version='0.1.4',
    author='David Selassie',
    author_email='selassid@gmail.com',
    packages=find_packages(exclude=['tests']),
    url='https://github.com/selassid/canopener',
    license=resource_string(__name__, 'LICENSE.txt'),
    description=(
        'Python convenience function for opening compressed URLs and files.'
    ),
    keywords='open file s3 url bzip bz2 gzip gz',
    include_package_data=True,
    long_description=resource_string(__name__, 'README.rst'),
    setup_requires=['setuptools'],
    install_requires=[
        'boto',
        'pystaticconfiguration',
    ],
)
