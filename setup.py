import os

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
setup(
    name='Recko',
    description='Recko Recommendation engine',
    version="0.0.1",
    long_description=open('README.rst').read(),
    author='Haya Elayan',
    author_email='h.elayan@posrocket.com',
    # url='https://github.com/ahmadiga/django-files-library',
    package_dir={'recko': 'recko'},
    packages=find_packages(exclude='test_app'),
    include_package_data=True,
    install_requires=[
        "numpy == 1.15.4",
        "scipy == 1.2.0"
    ],
    tests_require=[],
    classifiers=[
    ],
)
