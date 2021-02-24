import os
from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name="questiongenerator", install_requires=required)
