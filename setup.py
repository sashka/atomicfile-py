#!/usr/bin/env python

from setuptools import setup

setup(
    name='atomicfile',
    version='1.0',
    author='Alexander Saltanov',
    author_email='asd@mokote.com',
    url='http://github.com/sashka/atomicfile',
    license='MIT',
    description='Writeable file object that atomically updates a file.',
    py_modules=['atomicfile'],
    test_suite='tests',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
