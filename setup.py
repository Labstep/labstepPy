from setuptools import setup

version = {}

with open("labstep/version.py") as fp:
    exec(fp.read().strip(), version)

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(name='labstep',
      version=version['version'],
      description='Python SDK for working with the Labstep API',
      long_description=long_description,
      url='http://github.com/Labstep/labstepPy',
      author='Barney Walker',
      author_email='barney@labstep.com',
      license='MIT',
      packages=['labstep'],
      install_requires=['requests', 'python-dotenv'],
      tests_require=["pytest"],
      zip_safe=False)
