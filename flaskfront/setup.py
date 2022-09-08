from setuptools import setup, find_packages

setup(
    name="opgflaskfront",
    version="1.0",
    description="base flask front app",
    install_requires=[
        "aws_xray_sdk>=2.8.0,<3",
        "flask>=2.1.0,<3",
        "gunicorn>=20.1.0,<21",
        "govuk-frontend-jinja>=2.0.0",
        "govuk-frontend-wtf>=0.3.0",
        "flask-assets>=2.0",
        "flask-compress>=1.9.0",
        "flask-talisman>=0.7.0",
        "flask-wtf>=1.0.0",
    ],
    packages=["opgflaskfront"],
    include_package_data=True,
)
