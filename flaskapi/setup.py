from setuptools import setup, find_packages

setup(
    name="opgflaskapi",
    version="1.0",
    description="base flask api",
    install_requires=[
        "aws_xray_sdk",
        "flask-sqlalchemy",
        "flask",
        "psycopg2-binary",
        "gunicorn",
    ],
    packages=["opgflaskapi"],
)
