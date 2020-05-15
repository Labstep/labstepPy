import os
import sys
from setuptools import setup
from setuptools.command.install import install

with open("README.rst", "r") as fh:
    long_description = fh.read()

VERSION = '2.3.1'


class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""
    description = 'verify that the git tag matches our version'

    def run(self):
        tag = os.getenv('CIRCLE_TAG')

        if tag != VERSION:
            info = "Git tag: {0} does not match the version of this app: {1}".format(
                tag, VERSION
            )
            sys.exit(info)


setup(name='labstep',
      version=VERSION,
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
