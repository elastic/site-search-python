#!/usr/bin/env python

from setuptools import setup, find_packages

from elastic_site_search.version import VERSION

setup(
    name = 'elastic-site-search',
    version = VERSION,
    description = 'Elastic Site Search API Client for Python',
    author = 'Elastic',
    author_email = 'support@elastic.co',
    url = 'https://github.com/elastic/site-search-python',
    packages = find_packages(),
    install_requires = ["anyjson", "six"],
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
