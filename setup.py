import setuptools
from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='Pan',
    version='0.0.1',
    description='Pan game',
    license="MIT",
    long_description=long_description,
    author='Kamil Plucinski',
    author_email='kamil.plucinski97@gmail.com',
    packages=setuptools.find_packages(),
    install_requires=[
        'click',
        'pytest==3.6',
        'pytest-cov',
        'pyyaml',
        'flake8',
        'coveralls',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
