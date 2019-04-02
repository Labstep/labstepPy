from setuptools import setup

with open("README.md", "r") as fh:
  long_description = fh.read()


setup(name='labstep',
  version='0.1',
  description='Python Wrapper around the Labstep API',
  long_description=long_description,
  long_description_content_type="text/markdown",
  url='http://github.com/Labstep/labstepPy',
  author='Barney Walker',
  author_email='barney@labstep.com',
  license='MIT',
  packages=['labstep'],
  install_requires=['requests','json'],
  zip_safe=False)