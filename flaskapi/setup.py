from setuptools import setup, find_packages

setup(name='opgflaskapi', 
        version='1.0', 
        description='base flask api',
        install_requires = ['flask-sqlalchemy', 'flask'],
        packages=['opgflaskapi'])
