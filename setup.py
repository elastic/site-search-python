#!/usr/bin/env python

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

about = {}
with open(path.join(here, 'elastic_site_search', 'version.py'), 'r', 'utf-8') as f:
    exec(f.read(), about)

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'elastic-site-search',
    version = about['VERSION'],
    description = 'Elastic Site Search API Client for Python',
    license = 'Apache 2.0',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author = 'Elastic',
    author_email = 'support@elastic.co',
    url = 'https://github.com/elastic/site-search-python',
    packages = find_packages(exclude=['tests', 'fixtures']),
    install_requires = ["six"],
    tests_require=['nose', 'vcrpy', 'mock', 'unittest2'],
    test_suite='nose.collector',
    classifiers = [
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: Apache Software License',
    ],
)
