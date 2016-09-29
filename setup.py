#!/usr/bin/env python
from setuptools import setup, find_packages

with open('VERSION') as version_file:
    version = version_file.read().strip()

with open('README.rst') as readme_file:
    readme = readme_file.read()

install_requires = [
    'boto3>=1.4.0',
]

setup(
    name='marquee',
    version=version,
    description='A simple Python logging formatter and handler for CloudWatch Events',
    long_description=readme,
    author='Herkermer Sherwood',
    author_email='theherk@gmail.com',
    packages=find_packages(),
    platforms=['all'],
    install_requires=install_requires,
    setup_requires=['pytest-runner'],
    tests_require=[
        'mock',
        'pytest'
    ]
)
