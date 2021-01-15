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

```python3 setup.py sdist```
