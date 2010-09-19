#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-directory-list',
    version='1.0'
    author='Object Syndicate',
    author_email='support@objectsyndicate.com',
    url='http://github.com/objectsyndicate/django-directory-list',
    description = 'Takes a directory path and lists the files as hyperlinks in a template',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'Django>=1.0.4'
    ],
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)