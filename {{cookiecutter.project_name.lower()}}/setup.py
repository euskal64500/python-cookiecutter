#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open('requirements.in') as requirements_file:
    requirements = requirements_file.read().splitlines()

with open('requirements_dev.in') as requirements_dev_file:
    development_requirements = requirements_dev_file.read().splitlines()

setup_requirements = [
    'pytest-runner'
],

test_requirements = [
    'pytest'
]

setup(
    name='{{cookiecutter.project_name.lower()}}',
    version='0.1.0',
    description='{{cookiecutter.project_name.lower()}}',
    long_description=readme + '\n\n' + history,
    author="{{cookiecutter.author.replace('\"', '\\\"')}}",
    author_email='{{cookiecutter.email}}',
    packages=find_packages(),
    {%- if 'no' not in cookiecutter.command_line_interface|lower %}
    entry_points={
        'console_scripts': [
            '{{cookiecutter.project_name.lower()}}={{ cookiecutter.project_name.lower().replace('-', '_') }}.cli:{{ cookiecutter.project_name.lower().replace('-', '_') }}'
        ]
    },
    {%- endif %}
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='{{cookiecutter.project_name.lower()}}',
    classifiers=[
        'Development Status :: Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    extras_require={
        'dev': development_requirements,
    },    
)
