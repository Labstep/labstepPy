from setuptools import setup, find_namespace_packages

version = {}

with open("labstep/constants/version.py") as fp:
    exec(fp.read().strip(), version)

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(name='labstep',
      version=version['VERSION'],
      description='Python SDK for working with the Labstep API',
      long_description=long_description,
      url='http://github.com/Labstep/labstepPy',
      author='Labstep',
      author_email='dev@labstep.com',
      license='MIT',
      packages=find_namespace_packages(include=['labstep', 'labstep.*']),
      install_requires=['requests', 'python-dotenv',
                        'beautifulsoup4', 'Deprecated', 'pathvalidate', 'pandas'],
      tests_require=["pytest"],
      zip_safe=False)
