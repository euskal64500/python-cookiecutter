import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][-_a-zA-Z0-9]+$'
AUTHOR_REGEX = r'^[a-zA-Z]+ [a-zA-Z]+$'
GITHUB_REGEX = r'^[_a-zA-Z][-_a-zA-Z0-9]+$'
EMAIL_REGEX = r'^[a-zA-Z0-9]+\.[a-zA-Z0-9]'

PROJECT_NAME = '{{ cookiecutter.project_name }}'
AUTHOR_NAME = '{{ cookiecutter.author }}'
GITHUB_USERNAME = '{{ cookiecutter.github_username }}'
AUTHOR_EMAIL = '{{ cookiecutter.email }}'


if not re.match(MODULE_REGEX, PROJECT_NAME):
    print('ERROR: The project {} is not a valid Python module name. Please do not use spaces'.format(APP_NAME))

    #Exit to cancel project
    sys.exit(1)

if not re.match(AUTHOR_REGEX, AUTHOR_NAME):
    print('ERROR: The author {} is not a valid name. Please use only 1 space between the first and last names'.format(AUTHOR_NAME))

    #Exit to cancel project
    sys.exit(1)

if not re.match(GITHUB_REGEX, GITHUB_USERNAME):
    print('ERROR: The github user {} is not a valid name. Please use only 1 space between the first and last names'.format(GITHUB_USERNAME))

    #Exit to cancel project
    sys.exit(1)

if not re.match(EMAIL_REGEX, AUTHOR_EMAIL):
    print('ERROR: The email {} is not a valid name. Please use only 1 space between the first and last names'.format(AUTHOR_EMAIL))

    #Exit to cancel project
    sys.exit(1)
