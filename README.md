# python-project-cookiecutter

This repo is a cookie cutter template for python packages. Below are the instructions to use this cookie-cutter template.

* Step 1: Install cookiecutter

``` python
pip install cookiecutter
```

* Step 2: Create local python project folder using the cyborg-cookiecutter template

``` bash
cookiecutter https://github.com/euskal64500/python-cookiecutter
```

* Step 3: Answer the questions

``` bash
project_name [python_project]: sample
author [First Last]: John Smith
email [your_email]: john_smith@hotmail.com
maintainer [john_smith@hotmail.com]: 
github_username [jsmith]: jsmith
Select command_line_interface:
1 - Click
2 - No command-line interface
Choose from 1, 2 [1]: 
```

* Step 4: Add WebHook In GitHub

- Go to your newly created project in github repo.
- Click on "Settings" on the right panel. (Must be admin).
- Then click on "Hooks" on the left panel.
- Click on the "Add WebHook" Button.
- Paste the service URL (jennkis or drone) in the URL form field.
- Select "application/json" as the content type.
- Select "Let me select individual events" and check "Issues".
- Leave the "Active" checkbox checked.
- Click on "Add webhook" to save the webhook.
