# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from setuptools import find_packages
from setuptools import setup
import codecs


with codecs.open('LICENSE.txt', 'r', 'utf8') as lf:
    license_str = lf.read()

with codecs.open('README.rst', 'r', 'utf8') as rf:
    long_description_str = rf.read()


setup(
    name='canopener',
    version='0.1.6',
    author='David Selassie',
    author_email='selassid@gmail.com',
    packages=find_packages(exclude=['tests']),
    url='https://github.com/selassid/canopener',
    license=license_str,
    description=(
        'Python convenience function for opening compressed URLs and files.'
    ),
    keywords='open file s3 url bzip bz2 gzip gz',
    include_package_data=True,
    long_description=long_description_str,
    setup_requires=['setuptools'],
    install_requires=[
        'boto',
        'pystaticconfiguration',
    ],
)
