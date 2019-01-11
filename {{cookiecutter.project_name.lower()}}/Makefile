.DEFAULT_GOAL := help
define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT
export PYTHONPATH := $(shell pwd)

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT
BROWSER := python -c "$$BROWSER_PYSCRIPT"

.PHONY: help
help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

.PHONY: clean
clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

.PHONY: clean-build
clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

.PHONY: clean-pyc
clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

.PHONY: clean-test
clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

.PHONY: format
format: ## perform yapf formatting
	yapf --recursive -i {{cookiecutter.project_name.lower().replace('-', '_')}}/ --verbose
	yapf --recursive -i tests/ --verbose

.PHONY: lint
lint: ## check style with flake8
	flake8 {{cookiecutter.project_name.lower().replace('-', '_')}}
	pylint {{cookiecutter.project_name.lower().replace('-', '_')}}
	flake8 tests
	pylint tests

.PHONY: test
test: ## run tests quickly with the default Python
	pytest

.PHONY: test-all
test-all: ## run tests on every Python version with tox
	tox

.PHONY: coverage
coverage: ## check code coverage quickly with the default Python
	coverage run --source {{cookiecutter.project_name.lower().replace('-', '_')}} -m pytest
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

.PHONY: docs
docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/{{cookiecutter.project_name.lower()}}.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ {{cookiecutter.project_name.lower()}}
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

.PHONY: servedocs
servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

.PHONY: release
release: clean ## package and upload a release
	python setup.py sdist upload -r local
	python setup.py bdist_wheel upload -r local

.PHONY: dist
dist: clean ## builds source and wheel package
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

.PHONY: install
install: clean ## install the package to the active Python's site-packages
	pip install -r requirements.txt
	python setup.py install

.PHONY: develop
develop: clean ## creates .egg-link to our local development directory in the site-packages directory
	pip install -e .[dev]

.PHONY: clean-requirements
clean-requirements:
	rm -f requirements.txt requirements_dev.txt

.PHONY: compile-requirements
compile-requirements:
	pip-compile -v --output-file requirements.txt requirements.in
	pip-compile -v --output-file requirements_dev.txt requirements.in requirements_dev.in

.PHONY: sync-requirements
sync-requirements:
	pip-sync requirements_dev.txt

.PHONY: requirements
requirements: clean-requirements compile-requirements sync-requirements
