# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 Sony Interactive Entertainment Intl., all rights reserved.
"""Console script for {{cookiecutter.project_name.lower().replace('-', '_')}}."""

import click
import pkg_resources

def get_version():
    """Displays the {{ cookiecutter.project_name.lower().replace('-', '_')}} version"""
    try:
        return pkg_resources.require("{{ cookiecutter.project_name.lower().replace('-', '_')}}")[0].version
    except pkg_resources.DistributionNotFound:
        click.echo("{{ cookiecutter.project_name.lower().replace('-', '_') }} is not installed")

@click.command()
@click.version_option(version=get_version())
def {{ cookiecutter.project_name.lower().replace('-', '_') }}(args=None):
    """Console script for {{ cookiecutter.project_name.lower() }}."""
    click.echo("Replace this message by putting your code into "
               "{{ cookiecutter.project_name.lower().replace('-', '_') }}.cli.{{ cookiecutter.project_name.lower().replace('-', '_') }}")
    click.echo("See click documentation at http://click.pocoo.org/")


if __name__ == "__main__":
    {{ cookiecutter.project_name.lower().replace('-', '_') }}()
