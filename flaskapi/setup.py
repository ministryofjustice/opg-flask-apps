from setuptools import setup, find_packages

setup(
    name="opgflaskapi",
    version="1.0",
    description="base flask api",
    install_requires=[
        "aws_xray_sdk>=2.8.0,<3",
        "flask>=2.1.0,<3",
        "sqlalchemy>=1.4,<2",
        "psycopg2-binary",
        "gunicorn>=20.1.0,<21",
    ],
    extras_require={
        "dev": [
            "pytest",
            "pytest-cov",
        ],
    },
    packages=["opgflaskapi"],
)
