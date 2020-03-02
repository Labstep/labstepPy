from setuptools import setup

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(name='labstep',
      version='2.2.3',
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
