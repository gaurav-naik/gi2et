# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from pip.req import parse_requirements

version = '1.0.0'
requirements = parse_requirements("requirements.txt", session="")

setup(
	name='gi2et',
	version=version,
	description='Pull Github Issues into Project Tasks',
	author='MN Technique',
	author_email='support@castlecraft.in',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=[str(ir.req) for ir in requirements],
	dependency_links=[str(ir._link) for ir in requirements if ir._link]
)
