# Installing locally

Navigate to folder containing `setup.py` and run:

```pip install -e .```

# Testing

To run the test suite use the command:

```pytest```

To include coverage report, use:

```pytest --cov-report html --cov=labstep tests/```

# Building the Docs

```
cd docs
./build_documentation.sh
```

# Building the Package 

```python setup.py sdist```


# Publishing

Before publishing you may have to increment the verison number in `setup.py`.

First publish to Test PyPi by running:

```twine upload --repository-url https://test.pypi.org/legacy/ dist/*```

When you are ready to publish to PyPi...

```twine upload dist/*```

# Reviewing the Release

Check out the updated docs at https://labsteppy.readthedocs.io/en/develop

In a fresh python environment run

```pip install -i https://test.pypi.org/simple/ labstep```
