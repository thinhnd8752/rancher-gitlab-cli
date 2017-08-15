# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="rancher-gitlab-cli",
    version="0.1.0",
    description="A painless rancher deployment tool support to your gitlab-ci",
    license="MIT",
    author="ducthinh993",
    packages=find_packages(),
    install_requires=[],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ]
)
