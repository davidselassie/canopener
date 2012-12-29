# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='canopener',
    version='0.1.0',
    author='David Selassie',
    author_email='selassid@gmail.com',
    packages=['canopener', 'canopener.tests'],
    url='https://github.com/selassid/canopener',
    license='LICENSE.txt',
    description='Python convenience function for opening compressed URLs and files.',
    long_description=open('README.txt').read(),
    install_requires=[],
)
