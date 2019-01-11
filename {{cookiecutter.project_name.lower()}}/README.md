# {{ cookiecutter.project_name.lower()}}

This repo contains the source for the {{ cookiecutter.project_name.lower()}} project.

## Installation

You should have python 3.6.x installed before executing the installation steps below

``` bash
pip install {{ cookiecutter.project_name.lower()}}
cd {{ cookiecutter.project_name.lower()}}
pip install pip-tools
make requirements
```

## version control

The version of this repo should match the version of the {{ cookiecutter.project_name.lower()}} application under tests.
This is necessary to insure that the tests corresponds to existing functionalities in the app.


## tests: Test folder

The tests folder has all the test file.

- tests_{{ cookiecutter.project_name.lower().replace('-', '_')}}.py

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

## VS code editor
We encourage developer to use the Visual Studio Code as a python editor. It is free, light weight, extensible, supports multiple programming languages
and works on all platforms. The .vscode folder contains the configuration settings for this editor. VS code is automatically configured
to use pylint and flake8 to check PEP8 compliancy and automatically formats the code. This allows keeping a certainly consistency in the code format.
The .vscode folder contains also commands to launch the tests from the text editor.

## WebHook In GitHub:
- Sign in to github, then got to {{ cookiecutter.project_name.lower()}} repo
- Click on "Settings" on the right panel. (Must be admin)
- Then click on "Hooks" on the left panel.
- Click on the "Add WebHook" Button.
- Paste the service URL (jenkins or drone) in the URL form field.
- Select "application/json" as the content type.
- Select "Let me select individual events" and check "Issues".
- Leave the "Active" checkbox checked.
- Click on "Add webhook" to save the webhook.
