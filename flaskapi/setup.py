from setuptools import setup, find_packages

setup(
    name="opgflaskapi",
    version="1.0",
    description="base flask api",
    install_requires=[
        "aws_xray_sdk = 2.8.0",
        "flask-sqlalchemy",
        "flask = 2.0.0",
        "psycopg2-binary",
        "gunicorn = 20.1.0",
    ],
    packages=["opgflaskapi"],
)
