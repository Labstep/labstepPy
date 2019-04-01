# Installing locally

Navigate to folder containing `setup.py` and run:

```pip install -e .```

# Building Package 

```python setup.py sdist```

# Publishing

Before publishing you may have to increment the verison number in `setup.py`.

First publish to Test PyPi by running:

```twine upload --repository-url https://test.pypi.org/legacy/ dist/*```

When you are ready to publish to PyPi...

```twine upload dist/*```