# {{cookiecutter.project_name.lower()}}
This repo contains the source for the {{cookiecutter.project_name.lower()}} application.

## Installation
You should have python 3.6.x installed before executing the installation steps below

``` bash
git clone git@github.com:SNEI/{{ cookiecutter.project_name.lower()}}
cd {{ cookiecutter.project_name.lower() }}
```

## version control
The version of this repo should match the version of the {{cookiecutter.project_name.lower()}} application under tests.
This is necessary to insure that the tests corresponds to existing functionalities in the app.


## tests: Test folder
The test folder has all the application e2e tests. It contains all the files necessary for pytest testing.
* conftest.py: test directory specific hook implementations.
* pytest.ini: command line configuration file for pytest. Determines pytest root directory.
* test_sample.py: example of pytest test

## Makefile
The makefiles contains shortcut commands. Among others:

clean                remove all build, test, pytest artifacts
format               uses yapf to automatically format
lint                 check style with flake8 and pylint
test                 runs all the tests in the tests folder with pytest
release              builds the package and uploads it to artifactory
dist                 builds source and wheel package (no upload to artifactory)
install              installs the package for development

To execute a command on macos or linux, do:
```bash
make format
```

To execute a command on macos or linux, do:
```bash
.\Make.ps1 format
```

## CI/CD
### drone
* .drone.yml Runs flake8 and pylint every time a PR is merged to master. A PR cannot be merged if flake8 and pylint detect compliance errors with PEP8
* QA user can (and should) add tests in drone. These tests will be executed before a merge.
Note: There is a plan to use Jenkins instead of drone for RNPS projects.

## Jenkinsfile
* Not supported yet
* Plan is to add Jenkins 2.0 template groovy scripts for smoke, regression and stress e2e tests. The jenkins script automatically pull a PUP format
sorror, uploads it to the devkit, executes the e2e tests and uploads the test results to the dashboards.

## VS code editor
We encourage testers to use the Visual Studio Code as a python editor. It is free, light weight, extensible, supports multiple programming languages
and works on all platforms. The .vscode folder contains the configuration settings for this editor. VS code is automatically configured
to use pylint and flake8 to check PEP8 compliancy and automatically formats the code. This allows keeping a certainly consistency in the code format.
The .vscode folder contains also commands to launch the tests from the text editor.
