python setup.py sdist --formats=gztar upload -r local
python setup.py sdist --formats=zip upload -r local
python setup.py bdist_wheel upload -r local
