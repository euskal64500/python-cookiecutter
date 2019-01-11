Param([string]$cmd)
$tgt = {{ cookiecutter.project_name.lower().replace('-', '_')}}
$msg = @"
clean                remove all build, test, coverage and Python artifacts
clean-build          remove build artifacts
clean-pyc            remove Python file artifacts
clean-test           remove test and coverage artifacts
format               automatically formats the python files to comply with PEP8
lint                 check style with flake8 and pylint
test                 run tests quickly with the default Python
test-all             run tests on every Python version with tox
coverage             check code coverage quickly with the default Python
docs                 generate Sphinx HTML documentation, including API docs
servedocs            compile the docs watching for changes
release              package and upload a release
dist                 builds source and wheel package
install              install the package to the active Python's site-packages
develop              creates .egg-link to our local development directory in the site-packages directory
requirements         updates the requirements*.txt and sync up installed libraries
"@
function make-clean-build
{
    del build\ -force -recurse -erroraction ignore
    del dist\ -force -recurse -erroraction ignore
    del .eggs\ -force -recurse -erroraction ignore
    del *.egg-info -force -recurse -erroraction ignore
    del *.egg -force -recurse -erroraction ignore
}
function make-clean-pyc
{
    del *.pyc -force -recurse -erroraction ignore
    del *.pyo -force -recurse -erroraction ignore
    del *~ -force -recurse -erroraction ignore
    dir . -filter __pycache__ -recurse -directory | del -force -recurse -erroraction ignore
    dir . -filter .mypy_cache -recurse -directory | del -force -recurse -erroraction ignore
}
function make-clean-test
{
    del .tox\  -force -recurse -erroraction ignore
    del .coverage  -force -erroraction ignore
    del htmlcov\  -force -recurse -erroraction ignore
}
function make-clean
{
    make-clean-build
    make-clean-pyc
    make-clean-test
}
function make-format
{
    yapf "$tgt" --max-line-length 120 --recursive --in-place --verbose
    yapf tests/ --max-line-length 120 --recursive --in-place --verbose

}
function make-lint
{
    flake8 "$tgt"
    pylint "$tgt"
    flake8 tests
    pylint tests
}
function make-test
{
    pytest
}
function make-test-all
{
    tox
}
function make-coverage
{
    coverage run --source "$tgt" -m pytest
    coverage report -m
    coverage html
    start htmlcov/index.html
}
function make-docs
{
    del docs\"$tgt".rst
    del .\docs\modules.rst
    sphinx-apidoc -o docs/ "$tgt"
    $dir = pwd
    try {
        cd docs
        .\make.bat clean
        .\make.bat html
    } finally {
        cd $dir
    }
    start docs/_build/html/index.html
}
function make-servedocs
{
    make-docs
    $dir = pwd
    try {
        cd docs
        watchmedo shell-command -p '*.rst' -c '.\make.bat html' -R -D .
    } finally {
        cd $dir
    }
}
function make-release
{
    make-clean
    python setup.py sdist --formats=gztar upload -r local
    python setup.py sdist --formats=zip upload -r local
    python setup.py bdist_wheel upload -r local
}
function make-dist
{
    make-clean
    python setup.py sdist --formats=zip
    python setup.py sdist --formats=gztar
    python setup.py bdist_wheel
    ls -l dist
}
function make-install-dependencies
{
    make-clean
    pip install -r requirements_dev.txt
}
function make-install
{
    make-clean
    pip install -r requirements.txt
    python setup.py install
}
function make-develop
{
    make-clean
    pip install -e .[dev]
}
function make-requirements
{
    Remove-Item requirements.txt -Force
    Remove-Item requirements_dev.txt -Force
    pip-compile -v --output-file requirements.txt requirements.in
    pip-compile -v --output-file requirements_dev.txt requirements.in requirements_dev.in
    pip-sync requirements_dev.txt
}
try {
    if ($null -eq $cmd) { throw }
    Invoke-Expression make-"$cmd"
} catch {
    $msg
}
