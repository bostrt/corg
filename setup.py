#!/usr/bin/env python3
from setuptools import setup, find_packages
from corg.version import __version__

# NOTE: Update the __version__ flag in corg/version.py for release.

setup(
    name='corg',
    version=__version__,
    packages=find_packages(),
    author='rbost',
    entry_points = {
        'console_scripts': [
            'corg=corg.corg:cli',
            ]
    },
    description='',
    license='',
    url='https://gitlab.cee.redhat.com/rbost/corg',
    install_requires=[
        'click', 
        'graphviz',
        ]
)
