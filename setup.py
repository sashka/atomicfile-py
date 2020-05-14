#!/usr/bin/env python

from setuptools import setup

with open('README.rst', 'r') as fh:
    long_description = fh.read()

setup(
    name='atomicfile',
    version='1.0.1',
    author='Alexander Saltanov',
    author_email='asd@mokote.com',
    url='http://github.com/sashka/atomicfile-py',
    license='MIT',
    description='Writeable file object that atomically updates a file.',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    py_modules=['atomicfile'],
    test_suite='tests',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
