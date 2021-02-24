import os
from setuptools import setup, find_packages

print(find_packages())
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name="questiongenerator", packages=find_packages(), install_requires=required)
